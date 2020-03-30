#!/bin/bash
echo "Starting"
kubectl apply -f ../jaeger/jaeger-deployment.yaml
kubectl apply -f ../jaeger/jaeger-service.yaml

gcloud compute firewall-rules create nodeport --allow tcp:30000-32767,udp:30000-32767 --source-ranges 194.132.164.168

kubectl get nodes --output wide
kubectl get svc

echo "Done"