#!/bin/bash
echo "Starting"
kubectl apply -f ../../jaeger/jaeger-deployment.yaml
kubectl apply -f ../../jaeger/jaeger-service.yaml

kubectl get nodes --output wide
kubectl get svc

echo "Done"