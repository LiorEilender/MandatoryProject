# QuakeWatch

## Run locally (venv)
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
python app.py
# http://127.0.0.1:5000

## Docker
docker build -t liore007/quakewatch:latest .
docker run -p 5000:5000 liore007/quakewatch:latest

## Docker Compose
docker compose up --build
# browse: http://127.0.0.1:5000

## Kubernetes (Minikube)
kubectl apply -f k8s/
minikube service quakewatch-svc --url

## Image
- Docker Hub: docker.io/liore007/quakewatch (tags: latest, <commit-sha>)

## Service Health
GET /Service Healthz
