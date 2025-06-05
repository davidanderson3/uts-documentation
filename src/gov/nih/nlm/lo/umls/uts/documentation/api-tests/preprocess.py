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
OUTPUT_FILE = OUTPUT_DIR / "valid_codes.json"

# ---- Step 1: Extract CUIs with Definitions ----
def extract_cuis_with_definitions(def_path):
    cuis = set()
    with open(def_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="|")
        for row in reader:
            if len(row) >= 7 and row[6] == "N":
                cuis.add(row[0])
    return cuis

# ---- Step 2: Identify Valid AUIs from MRREL ----
def get_valid_aui2(mrrel_path, cuis):
    parents = set()
    children = set()
    with open(mrrel_path, "r", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="|"):
            if len(row) < 17 or row[14] != "N":
                continue
            sab, stype2, rela, rel = row[10], row[6], row[7], row[3]
            if rela in {"mapped_from"} or sab in {
                "RXNORM", "RCD", "SNMI", "MEDCIN", "SNOMEDCT_VET", "MTHMST", "AOD", "HPO", "SNM", "MSH", "ULT", "WHO"
            } or (sab == "GO" and row[2] == "SDUI") or (sab == "SNOMEDCT_US" and rela == "referred_to_by"):
                continue
            if row[0] in cuis or row[4] in cuis:
                if rel in {"CHD", "RN"}:
                    parents.add(row[5])
                elif rel in {"PAR", "RB"}:
                    children.add(row[5])
    return parents & children

# ---- Step 3: Extract Valid Atoms from MRCONSO ----
def extract_valid_atoms(mrconso_path, valid_auis, cuis):
    valid_codes = []
    with open(mrconso_path, "r", encoding="utf-8") as infile:
        reader = csv.reader(infile, delimiter="|")
        for row in reader:
            if (
                len(row) >= 18 and
                row[1] == "ENG" and
                row[16] == "N" and
                row[7] in valid_auis and
                row[0] in cuis and
                row[13] != "NOCODE"
            ):
                valid_codes.append({
                    "CUI": row[0],
                    "STR": row[14],
                    "SAB": row[11],
                    "CODE": row[13],
                    "AUI": row[7],
                    "first4": row[14][:4],
                    "last4": row[14][-4:]
                })
    return valid_codes

# ---- Main Execution ----
def main():
    start = time.time()

    print(f"📘 Reading {MRDEF_PATH.name} to extract CUIs with definitions...")
    cuis = extract_cuis_with_definitions(MRDEF_PATH)
    print(f"✔️  CUIs with definitions: {len(cuis):,}")

    print(f"📘 Analyzing MRREL to find valid AUIs...")
    valid_auis = get_valid_aui2(MRREL_PATH, cuis)
    print(f"✔️  Valid AUIs with both parent and child: {len(valid_auis):,}")

    print(f"📘 Extracting valid atoms from MRCONSO...")
    atoms = extract_valid_atoms(MRCONSO_PATH, valid_auis, cuis)
    print(f"✔️  Valid atoms extracted: {len(atoms):,}")

    print(f"💾 Saving results to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(atoms, f, indent=2)

    print(f"\n⏱️ Completed in {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
