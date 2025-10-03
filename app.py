import os, requests
from datetime import datetime, timezone
from flask import Flask, render_template_string

APP_TITLE = os.getenv("APP_TITLE", "QuakeWatch")
API_URL = os.getenv("API_URL", "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")

app = Flask(__name__)

TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{{title}}</title>
<style>body{font-family:Arial;margin:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ddd;padding:8px}th{background:#f4f4f4;text-align:left}</style>
</head><body>
<h1>{{title}}</h1>
<p>Source: {{api_url}}</p>
{% if items %}
<table><thead><tr><th>Time (UTC)</th><th>Mag</th><th>Place</th></tr></thead><tbody>
{% for it in items %}
<tr><td>{{it.time}}</td><td>{{it.mag}}</td><td>{{it.place}}</td></tr>
{% endfor %}
</tbody></table>
{% else %}
<p>No recent data (or API unavailable).</p>
{% endif %}
</body></html>"""

def fetch_quakes():
    try:
        r = requests.get(API_URL, timeout=2)
        r.raise_for_status()
        data = r.json()
        feats = data.get("features", [])[:20]
        items = []
        for f in feats:
            props = f.get("properties", {})
            ts = props.get("time")
            tstr = ""
            if isinstance(ts, (int, float)):
                dt = datetime.fromtimestamp(ts/1000, tz=timezone.utc)
                tstr = dt.strftime("%Y-%m-%d %H:%M:%S")
            items.append({
                "mag": props.get("mag"),
                "place": props.get("place", ""),
                "time": tstr
            })
        return items
    except Exception:
        return []

@app.route("/")
def index():
    items = fetch_quakes()
    return render_template_string(TEMPLATE, title=APP_TITLE, api_url=API_URL, items=items), 200

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
