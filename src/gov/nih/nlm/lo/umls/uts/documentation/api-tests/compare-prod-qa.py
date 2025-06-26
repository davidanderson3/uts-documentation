#!/usr/bin/env python3
import sys
import requests

if len(sys.argv) < 2:
    print("❌ Usage: python search_variants.py <apiKey>")
    sys.exit(1)

api_key = sys.argv[1]

environments = {
    "PROD": "https://uts-ws.nlm.nih.gov/rest/search/current",
    "QA":   "https://uts-ws.awsqa.nlm.nih.gov/rest/search/current"
}

variant_list = [
    # Alzheimer’s disease
    'alzheimer', 'alzheimers', "alzheimer's", 'alzheimer disease',
    'alzheimer-disease', 'alzheimer s disease',
    # Parkinson’s disease
    'parkinson', 'parkinsons', "parkinson's", 'parkinson disease',
    "parkinson's disease", 'parkinsons disease', 'parkinson-disease',
    'parkinson s disease',
    # Crohn’s disease
    'crohn', 'crohns', "crohn's", 'crohn disease', "crohn's disease",
    'crohns disease', 'crohn-disease', 'crohn s disease',
    # Lou Gehrig’s disease / ALS
    'als', 'amyotrophic lateral sclerosis',
    'lou gehrigs disease', "lou gehrig's disease", 'lou gehrig disease',
    # Multiple sclerosis
    'multiple sclerosis', 'ms',
    # Diabetes
    'diabetes', 'diabetes mellitus', 'diabetes type 1', 'diabetes type 2',
    'type 1 diabetes', 'type i diabetes', 'type 2 diabetes', 'type ii diabetes',
    't1d', 't2d',
    # Heart attack / MI
    'heart attack', 'myocardial infarction', 'mi', 'cardiac infarction',
    # Acetaminophen / Paracetamol
    'acetaminophen', 'paracetamol', 'tylenol', 'apap',
    # Ibuprofen
    'ibuprofen', 'advil', 'motrin', 'nurofen',
    # Beta blockers
    'beta blocker', 'beta-blocker', 'beta blockers', 'beta-blockers',
    # Statins
    'statin', 'statins', 'reductase inhibitor', 'cholesterol medication',
    # COVID-19
    'covid', 'covid19', 'covid-19', 'coronavirus'
    'sars-cov-2', 'sarscov2',
    # HIV/AIDS
    'hiv', 'aids', 'hiv aids',
    'human immunodeficiency virus', 'acquired immune deficiency syndrome',
    # CUIs
    'C0022646', 'C4554465',
    # Codes
    '42399005', 'D053579', '7623',
    #SCUI
    'M0023172'
    
]

def query_umls(term, base_url):
    url = f"{base_url}?string={term}&pageSize=1000&apiKey={api_key}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        return len(data.get('result', {}).get('results', []))
    except Exception as e:
        return f"⚠️ {e}"

def main():
    for term in variant_list:
        print(f'\n🔎 "{term}"')
        for env_name, base_url in environments.items():
            count = query_umls(term, base_url)
            print(f'    {env_name}: {count}')

if __name__ == "__main__":
    main()
