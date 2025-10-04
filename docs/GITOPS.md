# GitOps (ArgoCD)  Quick Guide

## Install
kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## Login (optional)
kubectl -n argocd port-forward svc/argocd-server 8080:443
# browser: https://localhost:8080
# admin password:
# kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

## App
kubectl apply -f argocd/quakewatch-app.yaml
kubectl -n argocd get applications quakewatch-argocd
# expect: Synced, Healthy

## Update flow
# push to Git -> chart index (Pages) -> ArgoCD auto-sync -> rollout
