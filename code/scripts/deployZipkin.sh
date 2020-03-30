#!/bin/bash

echo "Starting"
kubectl apply -f ../zipkin/zipkin-deployment.yaml
kubectl apply -f ../zipkin/zipkin-service.yaml

kubectl get nodes --output wide
kubectl get svc

echo "Done"