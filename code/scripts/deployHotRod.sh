#!/bin/bash

echo "Starting"
kubectl apply -f ../jaeger/jaeger-deployment.yaml
kubectl apply -f ../jaeger/jaeger-service.yaml
kubectl apply -f ../hotrod/hotrod-deployment.yaml
kubectl apply -f ../hotrod/hotrod-service.yaml

gcloud compute firewall-rules create hotrod-rule --allow tcp:30000-32767

kubectl get nodes --output wide
kubectl get svc

echo "Done"