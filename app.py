# easy-4-idor-report/app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

REPORTS = {
    "1001": {"owner":"alice","content":"public"},
    "9999": {"owner":"admin","content":"CTF{easy_idor_report}"}
}

@app.route("/")
def index():
    return """
<h2>Report Viewer</h2>
<p>View generated user and system reports.</p>
<ul>
<li>GET /api/report/&lt;id&gt;</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/api/report/<rid>")
def get_report(rid):
    # BUG: no ownership check
    return jsonify(REPORTS.get(rid, {"error":"not found"}))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
