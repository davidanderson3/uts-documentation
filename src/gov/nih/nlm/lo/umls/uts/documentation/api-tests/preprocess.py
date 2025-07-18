import csv
import sys
import time
import json
from pathlib import Path

csv.field_size_limit(sys.maxsize)

# ---- Paths ----
INPUT_DIR    = Path(".")
OUTPUT_DIR   = Path("subset")
OUTPUT_DIR.mkdir(exist_ok=True)

MRDEF_PATH   = INPUT_DIR / "MRDEF.RRF"
MRREL_PATH   = INPUT_DIR / "MRREL.RRF"
MRSAT_PATH   = INPUT_DIR / "MRSAT.RRF"
MRCONSO_PATH = INPUT_DIR / "MRCONSO.RRF"
OUTPUT_FILE  = OUTPUT_DIR  / "valid_codes.json"

# Endpoint names from test.py. Each will get its own list of candidate atoms.
ENDPOINT_NAMES = [
    "Search - basic",
    "Search - basic - high page size",
    "Search - exact",
    "Search - return a CODE",
    "Search - input CODE, return CUIs",
    "Search - input CUI, return CODE",
    "Search - left truncation",
    "Search - right truncation",
    "Search - normalized string",
    "Search - normalized words",
    "Concept",
    "Concept Atoms",
    "Concept Definitions",
    "Concept Relations",
    "Code",
    "Code Attributes",
    "Code Children",
    "Code Parents",
    "Code Ancestors",
    "Code Descendants",
    "Code Relations",
    "Code Atoms",
    "Code Default Preferred Atom",
    "Code Crosswalk",
]

# ---- Step 1: Extract CUIs with Definitions ----
def extract_cuis_with_definitions(def_path):
    cuis = set()
    with open(def_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            # def suppression flag in MRDEF is in column 6
            if len(row) >= 7 and row[6] == "N":
                cuis.add(row[0])
    return cuis

# ---- Step 2: Identify Valid AUIs from MRREL ----
def get_valid_auis_from_mrrel(mrrel_path, cuis):
    parents  = set()
    children = set()
    with open(mrrel_path, "r", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="|"):
            # only non‐suppressed relationships
            if len(row) < 17 or row[14] != "N":
                continue
            sab, stype2, rela, rel = row[10], row[6], row[7], row[3]
            # skip unwanted source/relation combos
            if rela == "mapped_from" or sab in {
                "RXNORM","RCD","SNMI","MEDCIN","SNOMEDCT_VET","MTHMST",
                "AOD","HPO","SNM","MSH","ULT","WHO"
            } or (sab == "GO" and row[2] == "SDUI") \
             or (sab == "SNOMEDCT_US" and rela == "referred_to_by"):
                continue
            # only keep where concept participates
            if row[0] in cuis or row[4] in cuis:
                if rel in {"CHD", "RN"}:
                    parents.add(row[5])
                elif rel in {"PAR", "RB"}:
                    children.add(row[5])
    return parents & children

# ---- Step 3: Identify AUIs that actually have attributes in MRSAT ----
def get_auis_with_attributes(mrsat_path):
    auis = set()
    with open(mrsat_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            # need at least 13 columns for MRSAT
            if len(row) < 13:
                continue
            stype    = row[4]   # e.g. "AUI", "CUI", "RUI", etc.
            suppress = row[11]  # "N" means not suppressed
            if stype == "AUI" and suppress == "N":
                auis.add(row[3])  # METAUI holds the AUI value
    return auis

# ---- Step 4: Extract Valid Atoms from MRCONSO (excluding HL7V3.0) ----
def extract_valid_atoms(mrconso_path, valid_auis, cuis):
    valid_codes = []
    with open(mrconso_path, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile, delimiter="|")
        for row in reader:
            # row[11] is the SAB; skip HL7V3.0 here
            if (
                len(row) >= 18 and
                row[1] == "ENG" and      # English strings
                row[16] == "N" and       # not suppressed in MRCONSO
                row[7] in valid_auis and # AUI in our filtered set
                row[0] in cuis and       # CUI in our definition set
                row[13] != "NOCODE" and  # code exists
                row[11] != "HL7V3.0"     # exclude HL7V3.0 atoms
            ):
                valid_codes.append({
                    "CUI":   row[0],
                    "STR":   row[14],
                    "SAB":   row[11],
                    "CODE":  row[13],
                    "AUI":   row[7],
                    "first4": row[14][:4],
                    "last4":  row[14][-4:]
                })
    return valid_codes

# ---- Main Execution ----
def main():
    start = time.time()

    print(f"📘 Reading {MRDEF_PATH.name} to extract CUIs with definitions...")
    cuis = extract_cuis_with_definitions(MRDEF_PATH)
    print(f"✔️  CUIs with definitions: {len(cuis):,}")

    print(f"📘 Analyzing {MRREL_PATH.name} to find valid AUIs...")
    valid_auis_mrrel = get_valid_auis_from_mrrel(MRREL_PATH, cuis)
    print(f"✔️  AUIs from MRREL: {len(valid_auis_mrrel):,}")

    print(f"📘 Extracting AUIs with attributes from {MRSAT_PATH.name}…")
    valid_auis_mrsat = get_auis_with_attributes(MRSAT_PATH)
    print(f"✔️  AUIs in MRSAT: {len(valid_auis_mrsat):,}")

    # intersect to only keep AUIs both in MRREL hierarchy and having MRSAT attributes
    valid_auis = valid_auis_mrrel & valid_auis_mrsat
    print(f"✔️  AUIs in both MRREL & MRSAT: {len(valid_auis):,}")

    print(f"📘 Extracting valid atoms from {MRCONSO_PATH.name} (excluding HL7V3.0)...")
    atoms = extract_valid_atoms(MRCONSO_PATH, valid_auis, cuis)
    print(f"✔️  Valid atoms extracted: {len(atoms):,}")

    print(f"💾 Saving results to {OUTPUT_FILE}...")
    # Store a separate list of candidate atoms for each endpoint. Currently
    # the same atom list works for all endpoints, but separating them makes it
    # easy to further customize in the future.
    data = {name: atoms for name in ENDPOINT_NAMES}
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"\n⏱️ Completed in {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
