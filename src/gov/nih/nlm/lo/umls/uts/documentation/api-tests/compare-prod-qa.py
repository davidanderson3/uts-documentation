#!/usr/bin/env python3
import os
import sys
import requests
import html
import urllib.parse

# ─── Configuration: output directory ───────────────────────────────────────────
# All HTML files will be written into a "reports" subfolder next to this script.
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "reports")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# ─────────────────────────────────────────────────────────────────────────────

def fetch_results(term, base_url, api_key):
    url = f"{base_url}?string={urllib.parse.quote_plus(term)}&pageSize=1000&apiKey={api_key}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        return data.get('result', {}).get('results', [])
    except Exception as e:
        return f"⚠️ {e}"


def generate_html_report(counts, output_filename="report.html"):
    head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>UMLS Variant Search Report</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    th { background: #f4f4f4; }
    .mismatch { background-color: #ffecec; }
    a { text-decoration: none; color: #06c; }
  </style>
</head>
<body>
  <h1>UMLS Search Prod-QA Comparison Report</h1>
  <table>
    <thead>
      <tr><th>Variant</th><th>PROD</th><th>QA</th><th>Compare</th></tr>
    </thead>
    <tbody>
"""
    rows = ""
    for term, env_counts in counts.items():
        safe_term = html.escape(term)
        prod_cnt = html.escape(str(env_counts["PROD"]))
        qa_cnt   = html.escape(str(env_counts["QA"]))
        highlight = ' class="mismatch"' if prod_cnt != qa_cnt else ""
        comp_file = f"compare_{urllib.parse.quote_plus(term)}.html"
        rows += (
            f"      <tr{highlight}>"
            f"<td>{safe_term}</td>"
            f"<td>{prod_cnt}</td>"
            f"<td>{qa_cnt}</td>"
            f"<td><a href=\"{comp_file}\">View</a></td>"
            "</tr>\n"
        )
    tail = """    </tbody>
  </table>
</body>
</html>"""

    output_path = os.path.join(OUTPUT_DIR, output_filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(head + rows + tail)
    print(f"✅ Wrote HTML report to {output_path}")


def generate_comparison_pages(results_data):
    for term, env_data in results_data.items():
        safe_term = html.escape(term)
        filename = f"compare_{urllib.parse.quote_plus(term)}.html"
        full_path = os.path.join(OUTPUT_DIR, filename)

        prod_list = env_data.get("PROD", [])
        qa_list   = env_data.get("QA",   [])

        prod_idx = {item.get("ui",""): i for i, item in enumerate(prod_list)} if isinstance(prod_list, list) else {}
        qa_idx   = {item.get("ui",""): i for i, item in enumerate(qa_list)}   if isinstance(qa_list, list) else {}

        shifts = [abs(qa_idx[ui] - prod_idx[ui]) for ui in set(prod_idx) & set(qa_idx)]
        max_shift = max(shifts) if shifts else 0
        if max_shift == 0:
            max_shift = 1

        head = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Compare \"{safe_term}\"</title>
  <style>
    body {{ font-family: sans-serif; margin: 0; padding: 20px; }}
    .columns {{ display: flex; gap: 20px; }}
    .column {{ flex: 1; }}
    ol {{ padding-left: 20px; }}
    li {{ margin-bottom: 4px; padding: 2px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>Compare results for \"{safe_term}\"</h1>
  <div class="columns">
    <div class="column">
      <h2>PROD</h2>
      <ol>
"""
        prod_items_html = ""
        if isinstance(prod_list, list):
            for item in prod_list:
                ui = item.get("ui", "")
                name = html.escape(item.get("name", ""))
                if ui in qa_idx:
                    diff = qa_idx[ui] - prod_idx[ui]
                    norm = diff / max_shift
                    hue = (1 - norm) * 60
                    style = f' style="background-color:hsl({hue:.1f},100%,90%)"'
                else:
                    style = ' style="background-color:hsl(0,0%,90%)"'
                prod_items_html += f"        <li{style}>{name} [{ui}]</li>\n"
        else:
            prod_items_html = f"        <li>{html.escape(str(prod_list))}</li>\n"

        mid = """      </ol>
    </div>
    <div class="column">
      <h2>QA</h2>
      <ol>
"""
        qa_items_html = ""
        if isinstance(qa_list, list):
            for item in qa_list:
                ui = item.get("ui", "")
                name = html.escape(item.get("name", ""))
                if ui in prod_idx:
                    diff = qa_idx[ui] - prod_idx[ui]
                    norm = diff / max_shift
                    hue = (1 - norm) * 60
                    style = f' style="background-color:hsl({hue:.1f},100%,90%)"'
                else:
                    style = ' style="background-color:hsl(240,100%,90%)"'
                qa_items_html += f"        <li{style}>{name} [{ui}]</li>\n"
        else:
            qa_items_html = f"        <li>{html.escape(str(qa_list))}</li>\n"

        tail = """      </ol>
    </div>
  </div>
</body>
</html>"""

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(head + prod_items_html + mid + qa_items_html + tail)

    print(f"✅ Wrote comparison pages into {OUTPUT_DIR}")


def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python compare-prod-qa.py <apiKey>")
        sys.exit(1)
    api_key = sys.argv[1]

    environments = {
        "PROD": "https://uts-ws.nlm.nih.gov/rest/search/current",
        "QA":   "https://uts-ws.awsqa.nlm.nih.gov/rest/search/current"
    }

    variant_list = [
        'alzheimer', 'alzheimers', "alzheimer's", 'alzheimer disease', 'alzheimer-disease', 'alzheimer s disease',
        'parkinson', 'parkinsons', "parkinson's", 'parkinson disease', "parkinson's disease", 'parkinsons disease',
        'parkinson-disease', 'parkinson s disease', 'crohn', 'crohns', "crohn's", 'crohn disease', "crohn's disease", 
        'crohns disease', 'crohn-disease', 'crohn s disease', 'als', 'amyotrophic lateral sclerosis',
        'lou gehrigs disease', "lou gehrig's disease", 'lou gehrig disease', 'multiple sclerosis', 'ms',
        'diabetes', 'diabetes mellitus', 'diabetes type 1', 'diabetes type 2', 'type 1 diabetes', 'type i diabetes',
        'type 2 diabetes', 'type ii diabetes', 't1d', 't2d', 'heart attack', 'myocardial infarction', 'mi',
        'cardiac infarction', 'acetaminophen', 'paracetamol', 'tylenol', 'apap', 'ibuprofen', 'advil', 'motrin',
        'nurofen', 'beta blocker', 'beta-blocker', 'beta blockers', 'beta-blockers', 'statin', 'statins',
        'reductase inhibitor', 'cholesterol medication', 'covid', 'covid19', 'covid-19', 'coronavirus',
        'sars-cov-2', 'sarscov2', 'hiv', 'aids', 'hiv aids', 'human immunodeficiency virus', 
        'acquired immune deficiency syndrome', 'C0022646', 'C4554465', '42399005', 'D053579', '7623', 'M0023172'
    ]

    results_data = {}
    counts = {}
    for term in variant_list:
        term_data = {}
        term_counts = {}
        for env_name, base_url in environments.items():
            data = fetch_results(term, base_url, api_key)
            term_data[env_name] = data
            term_counts[env_name] = len(data) if isinstance(data, list) else data
        results_data[term] = term_data
        counts[term] = term_counts

    generate_html_report(counts)
    generate_comparison_pages(results_data)

if __name__ == "__main__":
    main()
