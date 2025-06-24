#!/usr/bin/env python3
import sys
import requests


if len(sys.argv) < 2:
    print("❌ Usage: python search_variants.py <apiKey>")
    sys.exit(1)

api_key = sys.argv[1]

environments = {
    "PROD": "https://uts-ws.nlm.nih.gov/rest/search/current",
    "QA": "https://uts-ws.awsqa.nlm.nih.gov/rest/search/current"
}

variant_sets = {
    "Alzheimer's disease": [
        'alzheimer', 'alzheimers', "alzheimer's", 'alzheimer disease',
        "alzheimer's disease", 'alzheimers disease', "alzheimers' disease",
        'alzheimer-disease', 'alzheimer s disease'
    ],
    "Parkinson's disease": [
        'parkinson', 'parkinsons', "parkinson's", 'parkinson disease',
        "parkinson's disease", 'parkinsons disease', 'parkinson-disease', 'parkinson s disease'
    ],
    "Crohn's disease": [
        'crohn', 'crohns', "crohn's", 'crohn disease', "crohn's disease",
        'crohns disease', 'crohn-disease', 'crohn s disease'
    ],
    "Lou Gehrig's disease / ALS": [
        'als', 'a.l.s.', 'amyotrophic lateral sclerosis',
        'lou gehrigs disease', "lou gehrig's disease", 'lou gehrig disease'
    ],
    "Multiple sclerosis": [
        'multiple sclerosis', 'm.s.', 'ms'
    ],
    "Diabetes": [
        'diabetes', 'diabetes mellitus', 'diabetes type 1', 'diabetes type 2',
        'type 1 diabetes', 'type i diabetes', 'type 2 diabetes', 'type ii diabetes',
        't1d', 't2d'
    ],
    "Heart attack / MI": [
        'heart attack', 'myocardial infarction', 'm.i.', 'mi', 'cardiac infarction'
    ],
    "Acetaminophen / Paracetamol": [
        'acetaminophen', 'paracetamol', 'tylenol', 'apap'
    ],
    "Ibuprofen": [
        'ibuprofen', 'advil', 'motrin', 'nurofen'
    ],
    "Beta blockers": [
        'beta blocker', 'beta-blocker', 'beta blockers', 'beta-blockers', 'b-blockers'
    ],
    "Statins": [
        'statin', 'statins', 'reductase inhibitor', 'cholesterol medication'
    ],
    "COVID-19": [
        'covid', 'covid19', 'covid-19', 'coronavirus', 'sars cov 2',
        'sars-cov-2', 'sarscov2'
    ],
    "HIV/AIDS": [
        'hiv', 'h.i.v.', 'aids', 'hiv aids', 'hiv/aids',
        'human immunodeficiency virus', 'acquired immune deficiency syndrome'
    ]
}

def query_umls(term, base_url):
    url = f"{base_url}?string={term}&pageSize=1000&apiKey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return len(json_data.get('result', {}).get('results', []))
    except Exception as e:
        return f"⚠️ {str(e)}"

def main():
    for label, terms in variant_sets.items():
        print(f"\n🧠 {label}")
        for term in terms:
            counts = {}
            for env, base_url in environments.items():
                count = query_umls(term, base_url)
                counts[env] = count
            print(f'  🔎 "{term}" → PROD: {counts["PROD"]} | QA: {counts["QA"]}')

if __name__ == "__main__":
    main()