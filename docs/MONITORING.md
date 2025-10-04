# Monitoring (Prometheus & Grafana)

**Targets:** ServiceMonitor אוסף את `http://:5000/metrics` → הtargets במצב **UP**.  
**Alerts:**
- `QuakeWatchHighTraffic`  `sum(rate(http_requests_total{service="quakewatch-argocd"}[1m])) > 2` למשך 2 דקות (warning)
- `QuakeWatchDown`  `absent(up{service="quakewatch-argocd"} == 1)` למשך דקה (critical)

## Screenshots
- ArgoCD: ![ArgoCD](img/argocd-synced-healthy.png)
- Prometheus Targets: ![Prometheus Targets](img/prometheus-targets-up.png)
- Grafana RPS: ![Grafana RPS](img/grafana-rps.png)
- (Optional) Alerts: ![Alerts](img/alerts-firing.png)
