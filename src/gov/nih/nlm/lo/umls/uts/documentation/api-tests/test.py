import csv
import sys
import random
import requests
import argparse
import time
from html import escape
from pathlib import Path
import json
from collections import defaultdict
import urllib.parse

csv.field_size_limit(sys.maxsize)

# ---- CLI ----
parser = argparse.ArgumentParser(description="Benchmark UMLS REST API against a selected environment.")
parser.add_argument("--apiKey", required=True, help="UMLS API key")
parser.add_argument("--env", choices=["prod", "qa"], required=True, help="Target environment: 'prod' or 'qa'")
parser.add_argument("--count", type=int, required=True, help="Number of requests to run per endpoint")
args = parser.parse_args()

NUM_TRIALS = args.count
BASE_URL = {
    "qa": "https://uts-ws.awsqa.nlm.nih.gov",
    "prod": "https://uts-ws.nlm.nih.gov"
}[args.env]

VALID_CODES_PATH = Path("subset/valid_codes.json")
if not VALID_CODES_PATH.exists():
    print(f"❌ {VALID_CODES_PATH} not found. Run the preprocessing script first.")
    sys.exit(1)

with open(VALID_CODES_PATH, "r", encoding="utf-8") as f:
    atoms = json.load(f)
if not atoms:
    print("❌ No usable atoms found in valid_codes.json.")
    sys.exit(1)
print(f"🧠 Loaded {len(atoms):,} prefiltered atoms from {VALID_CODES_PATH.name}")

VERSION = "current"
ENDPOINTS = {
    "Search - basic": lambda a: f"/rest/search/{VERSION}?string={a['STR']}",
    "Search - basic - high page size": lambda a: f"/rest/search/{VERSION}?string={a['STR']}&pageSize=1000",
    "Search - exact": lambda a: f"/rest/search/{VERSION}?string={a['STR']}&searchType=exact",
    "Search - return a CODE": lambda a: f"/rest/search/{VERSION}?string={a['STR']}&sabs={a['SAB']}&returnIdType=code",
    "Search - input CODE, return CUIs": lambda a: f"/rest/search/{VERSION}?string={urllib.parse.quote(a['CODE'])}&sabs={a['SAB']}&inputType=sourceUi",
    "Search - input CUI, return CODE": lambda a: f"/rest/search/{VERSION}?string={a['CUI']}&sabs={a['SAB']}&returnIdType=code",
    "Search - left truncation": lambda a: f"/rest/search/{VERSION}?string={a['last4']}&searchType=leftTruncation",
    "Search - right truncation": lambda a: f"/rest/search/{VERSION}?string={a['first4']}&searchType=rightTruncation",
    "Search - normalized string": lambda a: f"/rest/search/{VERSION}?string={a['STR']}&searchType=normalizedString",
    "Search - normalized words": lambda a: f"/rest/search/{VERSION}?string={a['STR']}&searchType=normalizedWords",
    "Concept": lambda a: f"/rest/content/{VERSION}/CUI/{a['CUI']}",
    "Concept Atoms": lambda a: f"/rest/content/{VERSION}/CUI/{a['CUI']}/atoms",
    "Concept Definitions": lambda a: f"/rest/content/{VERSION}/CUI/{a['CUI']}/definitions",
    "Concept Relations": lambda a: f"/rest/content/{VERSION}/CUI/{a['CUI']}/relations",
    "Code": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}",
    "Code Attributes": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/attributes",
    "Code Children": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/children",
    "Code Parents": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/parents",
    "Code Ancestors": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/ancestors",
    "Code Descendants": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/descendants",
    "Code Relations": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/relations",
    "Code Atoms": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/atoms",
    "Code Default Preferred Atom": lambda a: f"/rest/content/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}/atoms/preferred",
    "Code Crosswalk": lambda a: f"/crosswalk/{VERSION}/source/{a['SAB']}/{urllib.parse.quote(a['CODE'])}",
}
# Some of these take several seconds, but you can run if you like. 
SINGLE_RUN_ENDPOINTS = {
    #"Code Ancestors - SNOMEDCT_US extreme example": lambda _: "/rest/content/current/source/SNOMEDCT_US/64680003/ancestors?pageSize=1000",
    #"Code Ancestors - NCBI extreme example": lambda _: "/rest/content/current/source/NCBI/504329/ancestors?pageSize=1000"
    #"Code Descendants - SNOMEDCT_US extreme example": lambda _: "/rest/content/current/source/SNOMEDCT_US/123037004/descendants?pageSize=1000",
    #"Code Descendants - NCBI extreme example": lambda _: "/rest/content/current/source/NCBI/131567/descendants?pageSize=1000",
    #"Code Crosswalk - extreme example": lambda a: f"/crosswalk/{VERSION}/source/RXNORM/581662",
}

request_logs = []
endpoint_throughput = {}
metrics = defaultdict(lambda: {"times": [], "failures": 0})

# ---- Regular Requests ----
for name, path_fn in ENDPOINTS.items():
    print(f"\n📊 Benchmarking: {name}")
    start_time = time.time()
    for _ in range(NUM_TRIALS):
        atom = random.choice(atoms)
        path = path_fn(atom)
        full_url = f"{BASE_URL}{path}&apiKey={args.apiKey}" if "?" in path else f"{BASE_URL}{path}?apiKey={args.apiKey}"
        try:
            req_start = time.time()
            res = requests.get(full_url, timeout=90)
            elapsed = time.time() - req_start
            res.raise_for_status()
            metrics[name]["times"].append(elapsed)
            status = f"✅ {res.status_code} OK ({elapsed:.2f}s)"
            response_content = res.json()
        except Exception as e:
            status = f"❌ {type(e).__name__}"
            response_content = {"error": str(e)}
            metrics[name]["failures"] += 1
        request_logs.append({
            "endpoint": name,
            "url": full_url,
            "status": status,
            "response": response_content
        })
    endpoint_throughput[name] = {"start": start_time, "end": time.time()}

# ---- Single-Run Requests ----
print("\n📊 Running Single-Run Tests:")
for name, path_fn in SINGLE_RUN_ENDPOINTS.items():
    print(f"\n🔹 Running: {name}")
    path = path_fn(None)
    full_url = f"{BASE_URL}{path}&apiKey={args.apiKey}" if "?" in path else f"{BASE_URL}{path}?apiKey={args.apiKey}"
    try:
        req_start = time.time()
        res = requests.get(full_url)
        elapsed = time.time() - req_start
        res.raise_for_status()
        metrics[name]["times"].append(elapsed)
        status = f"✅ {res.status_code} OK ({elapsed:.2f}s)"
        response_content = res.json()
    except Exception as e:
        elapsed = 0
        status = f"❌ {type(e).__name__}"
        response_content = {"error": str(e)}
        metrics[name]["failures"] += 1
    print(f"   - Status: {status}")
    request_logs.append({
        "endpoint": name,
        "url": full_url,
        "status": status,
        "response": response_content
    })
    endpoint_throughput[name] = {"start": req_start, "end": req_start + elapsed}

# ---- HTML Summary ----
html_path = Path("results.html")
endpoint_pages_dir = Path("results_pages")
endpoint_pages_dir.mkdir(exist_ok=True)

html = f"""<!DOCTYPE html>
<html><head>
  <meta charset="utf-8">
  <title>UMLS API Test Results</title>
  <style>
    body {{ font-family: monospace; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 6px; text-align: left; vertical-align: top; }}
    th {{ background-color: #f2f2f2; }}
    td.ok {{ background-color: #e6ffed; }}
    td.err {{ background-color: #ffe6e6; }}
    code {{ white-space: pre-wrap; word-break: break-word; }}
    td:first-child {{ min-width: 300px; }}
  </style>
</head><body>
<h1>UMLS API Test Results</h1>
<p><strong>Total Requests:</strong> {len(request_logs)}</p>
<h2>Metrics Summary</h2>
<table>
<thead><tr><th>Endpoint</th><th>Average Time (s)</th><th>Time Range (s)</th><th>Failed</th><th>Requests/sec</th></tr></thead><tbody>
"""

for endpoint, data in metrics.items():
    times = data["times"]
    failures = data["failures"]
    total_requests = len(times) + failures
    total_time = endpoint_throughput[endpoint]["end"] - endpoint_throughput[endpoint]["start"]
    rps = total_requests / total_time if total_time > 0 else 0
    link = f"<a href='results_pages/{endpoint.replace(' ', '_').replace('/', '_')}.html'>{escape(endpoint)}</a>"

    if times:
        avg = sum(times) / len(times)
        html += f"<tr><td>{link}</td><td>{avg:.2f}</td><td>{min(times):.2f} - {max(times):.2f}</td><td>{failures}</td><td>{rps:.2f}</td></tr>"
    else:
        html += f"<tr><td>{link}</td><td colspan='2'>No successes</td><td>{failures}</td><td>0.00</td></tr>"

html += "</tbody></table><h2>Request Log</h2><table><thead><tr><th>Endpoint</th><th>URL</th><th>Status</th></tr></thead><tbody>"
for log in request_logs:
    cls = "ok" if log["status"].startswith("✅") else "err"
    html += f"<tr><td>{escape(log['endpoint'])}</td><td><code>{escape(log['url'])}</code></td><td class='{cls}'>{escape(log['status'])}</td></tr>"
html += "</tbody></table></body></html>"
html_path.write_text(html, encoding="utf-8")
print(f"📄 Results saved to {html_path}")

# ---- Endpoint Detail Pages ----
for endpoint in metrics:
    file = endpoint_pages_dir / f"{endpoint.replace(' ', '_').replace('/', '_')}.html"
    body = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{escape(endpoint)}</title>
<style>
  body {{ font-family: monospace; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ border: 1px solid #ccc; padding: 6px; text-align: left; vertical-align: top; }}
  th {{ background-color: #f2f2f2; }}
  td.ok {{ background-color: #e6ffed; }}
  td.err {{ background-color: #ffe6e6; }}
  pre {{ background-color: #f8f8f8; padding: 10px; border: 1px solid #ccc; overflow-x: auto; }}
</style></head><body>
<h1>{escape(endpoint)} - Detail</h1><table>
<thead><tr><th>URL</th><th>Status</th><th>Response</th></tr></thead><tbody>
"""
    for log in request_logs:
        if log["endpoint"] != endpoint:
            continue
        cls = "ok" if log["status"].startswith("✅") else "err"
        resp = json.dumps(log["response"], indent=2)
        body += f"<tr><td><code>{escape(log['url'])}</code></td><td class='{cls}'>{escape(log['status'])}</td><td><pre>{escape(resp)}</pre></td></tr>"
    body += "</tbody></table></body></html>"
    file.write_text(body, encoding="utf-8")

print(f"📄 Individual endpoint pages saved to {endpoint_pages_dir}")
