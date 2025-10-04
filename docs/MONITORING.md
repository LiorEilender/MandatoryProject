# Monitoring  Quick Guide

## Install
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install monitoring prometheus-community/kube-prometheus-stack `
  --namespace monitoring --create-namespace `
  --set grafana.adminPassword="Admin123!"

## Scrape
kubectl apply -f monitoring-servicemonitor.yaml
kubectl apply -f monitoring/prometheus-rule.yaml
kubectl apply -f monitoring/grafana-dashboard-cm.yaml

## Access
kubectl -n monitoring port-forward svc/monitoring-grafana 3000:80
kubectl -n monitoring port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090

## Screenshots to include
1) Prometheus /targets  quakewatch-argocd: UP
2) Grafana  QuakeWatch Overview dashboard
3) Alerts page  one of QuakewatchDown/NoTraffic/HighTraffic
