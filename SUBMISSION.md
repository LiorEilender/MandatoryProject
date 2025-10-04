## Quick Links
- ArgoCD App: argocd/quakewatch-app.yaml
- PrometheusRule: monitoring/prometheus-rule.yaml
- Grafana Dashboard: monitoring/grafana-dashboard-cm.yaml
- ServiceMonitor: monitoring-servicemonitor.yaml
- Helm Chart: quakewatch/  (repo via gh-pages)
- Image: liore1/quakewatch:latest

## How to Verify
1) ArgoCD: Synced/Healthy
2) App: 200 on `/` and `/metrics`
3) Prometheus: Targets → quakewatch-argocd = UP
4) Grafana: QuakeWatch Overview shows RPS
