from flask import Flask, Response
import os, time, requests
from datetime import datetime
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQ = Counter("http_requests_total", "HTTP requests total", ["path"])
LAT = Summary("request_latency_seconds", "Request latency")

FEED = os.getenv("API_URL", "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
TITLE = os.getenv("APP_TITLE", "QuakeWatch")

@app.before_request
def _before():
    from flask import request
    REQ.labels(request.path).inc()

@app.route("/")
def index():
    start = time.time()
    try:
        data = requests.get(FEED, timeout=5).json()
        rows = []
        for f in data.get("features", [])[:10]:
            p = f.get("properties", {})
            t = datetime.utcfromtimestamp(p.get("time", 0)/1000).strftime("%Y-%m-%d %H:%M:%S")
            rows.append((t, p.get("mag"), p.get("place")))
        body = "\n".join([f"<tr><td>{t}</td><td>{mag}</td><td>{place}</td></tr>" for t,mag,place in rows])
        html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title>
<style>body{{font-family:Arial;margin:20px}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ddd;padding:8px}}th{{background:#f4f4f4;text-align:left}}</style>
</head><body><h1>{TITLE}</h1><p>Source: {FEED}</p>
<table><thead><tr><th>Time (UTC)</th><th>Mag</th><th>Place</th></tr></thead><tbody>
{body}
</tbody></table></body></html>"""
        return html
    finally:
        LAT.observe(time.time() - start)

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
