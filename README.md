# Cloud Assignments

A small Flask application packaged with Docker and deployed to Kubernetes.

## Requirements

- Python 3.11 or later
- Docker
- Kubernetes cluster and `kubectl`

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open [http://localhost:5000](http://localhost:5000). The health endpoint is
available at [http://localhost:5000/health](http://localhost:5000/health).

## Run with Docker

```bash
docker build -t cloud-assignments:1.0 .
docker run --rm -p 5000:5000 cloud-assignments:1.0
```

## Deploy to Kubernetes

Build the image in the environment used by your cluster, then apply the
Deployment and Service:

```bash
docker build -t cloud-assignments:1.0 .
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get deployments,pods,services
```

The Service exposes port `30007` on the Kubernetes node. For a local
development cluster, open `http://localhost:30007` when the cluster supports
NodePort access on localhost.
