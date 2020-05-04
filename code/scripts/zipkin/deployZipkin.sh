#!/bin/bash

echo "Starting"
kubectl delete job jaeger-cassandra-schema-job
kubectl apply -f ../../zipkin/production/zipkinDeployment.yaml
kubectl apply -f ../../zipkin/production/zipkin-service.yaml

kubectl get nodes --output wide
kubectl get svc

echo "Done"