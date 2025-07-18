import csv
import sys
import time
import json
from pathlib import Path

csv.field_size_limit(sys.maxsize)

# ---- Paths ----
INPUT_DIR = Path(".")
OUTPUT_DIR = Path("subset")
OUTPUT_DIR.mkdir(exist_ok=True)

MRDEF_PATH = INPUT_DIR / "MRDEF.RRF"
MRREL_PATH = INPUT_DIR / "MRREL.RRF"
MRCONSO_PATH = INPUT_DIR / "MRCONSO.RRF"

# mapping of endpoint names to categories
ENDPOINT_CATEGORIES = {
    "Search - basic": "search",
    "Search - basic - high page size": "search",
    "Search - exact": "search",
    "Search - return a CODE": "search",
    "Search - input CODE, return CUIs": "search",
    "Search - input CUI, return CODE": "search",
    "Search - left truncation": "search",
    "Search - right truncation": "search",
    "Search - normalized string": "search",
    "Search - normalized words": "search",
    "Concept": "concept",
    "Concept Atoms": "concept",
    "Concept Definitions": "concept_def",
    "Concept Relations": "concept_rel",
    "Code": "code",
    "Code Attributes": "code",
    "Code Children": "code_child",
    "Code Parents": "code_parent",
    "Code Ancestors": "code_parent",
    "Code Descendants": "code_child",
    "Code Relations": "code_rel",
    "Code Atoms": "code",
    "Code Default Preferred Atom": "code",
    "Code Crosswalk": "code_rel",
}


def sanitize(name: str) -> str:
    return name.replace(" ", "_").replace("/", "_")


# ---- Step 1: Extract CUIs with Definitions ----
def extract_cuis_with_definitions(def_path: Path):
    cuis = set()
    with open(def_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            if len(row) >= 7 and row[6] == "N":
                cuis.add(row[0])
    return cuis


# ---- Step 2: Identify AUIs with parent/child relations ----
def get_aui_relations(mrrel_path: Path, cuis):
    has_parent = set()
    has_child = set()
    with open(mrrel_path, "r", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="|"):
            if len(row) < 17 or row[14] != "N":
                continue
            sab, rela, rel = row[10], row[7], row[3]
            if rela in {"mapped_from"} or sab in {
                "RXNORM", "RCD", "SNMI", "MEDCIN", "SNOMEDCT_VET", "MTHMST", "AOD",
                "HPO", "SNM", "MSH", "ULT", "WHO",
            } or (sab == "GO" and row[2] == "SDUI") or (sab == "SNOMEDCT_US" and rela == "referred_to_by"):
                continue
            if row[0] in cuis or row[4] in cuis:
                if rel in {"CHD", "RN"}:  # AUI1 has child, AUI2 has parent
                    has_child.add(row[1])
                    has_parent.add(row[5])
                elif rel in {"PAR", "RB"}:  # AUI1 has parent, AUI2 has child
                    has_parent.add(row[1])
                    has_child.add(row[5])
    return has_parent, has_child


# ---- Step 3: Extract Atoms from MRCONSO ----
def extract_atoms(mrconso_path: Path):
    atoms = []
    with open(mrconso_path, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile, delimiter="|")
        for row in reader:
            if (
                len(row) >= 18
                and row[1] == "ENG"
                and row[16] == "N"
                and row[13] != "NOCODE"
            ):
                atoms.append(
                    {
                        "CUI": row[0],
                        "STR": row[14],
                        "SAB": row[11],
                        "CODE": row[13],
                        "AUI": row[7],
                        "first4": row[14][:4],
                        "last4": row[14][-4:],
                    }
                )
    return atoms


# ---- Main Execution ----
def main():
    start = time.time()

    print(f"📘 Reading {MRDEF_PATH.name} to extract CUIs with definitions...")
    cuis_with_defs = extract_cuis_with_definitions(MRDEF_PATH)
    print(f"✔️  CUIs with definitions: {len(cuis_with_defs):,}")

    print(f"📘 Analyzing MRREL to gather parent/child relations...")
    auis_with_parent, auis_with_child = get_aui_relations(MRREL_PATH, cuis_with_defs)
    print(
        f"✔️  AUIs with parents: {len(auis_with_parent):,}, with children: {len(auis_with_child):,}"
    )

    print(f"📘 Extracting atoms from MRCONSO...")
    atoms = extract_atoms(MRCONSO_PATH)
    print(f"✔️  Candidate atoms extracted: {len(atoms):,}")

    # Build candidate lists by category
    all_atoms = atoms
    concept_atoms = [a for a in atoms if a["CUI"] in cuis_with_defs]
    concept_def_atoms = concept_atoms  # since concept_atoms already require definitions
    concept_rel_atoms = [a for a in atoms if a["AUI"] in auis_with_parent or a["AUI"] in auis_with_child]
    code_atoms = atoms
    code_parent_atoms = [a for a in atoms if a["AUI"] in auis_with_parent]
    code_child_atoms = [a for a in atoms if a["AUI"] in auis_with_child]
    code_rel_atoms = [a for a in atoms if a["AUI"] in auis_with_parent or a["AUI"] in auis_with_child]

    category_map = {
        "search": all_atoms,
        "concept": concept_atoms,
        "concept_def": concept_def_atoms,
        "concept_rel": concept_rel_atoms,
        "code": code_atoms,
        "code_parent": code_parent_atoms,
        "code_child": code_child_atoms,
        "code_rel": code_rel_atoms,
    }

    print("💾 Saving per-endpoint candidate files...")
    for endpoint, category in ENDPOINT_CATEGORIES.items():
        atoms_list = category_map.get(category, [])
        out_file = OUTPUT_DIR / f"{sanitize(endpoint)}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(atoms_list, f, indent=2)
        print(f"   - {endpoint}: {len(atoms_list):,} candidates -> {out_file.name}")

    print(f"\n⏱️ Completed in {time.time() - start:.2f} seconds")


if __name__ == "__main__":
    main()
