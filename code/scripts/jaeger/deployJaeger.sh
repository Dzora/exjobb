#!/bin/bash
echo "Starting"
kubectl delete job jaeger-cassandra-schema-job
kubectl apply -f ../../jaeger/production/jaegerDeployment.yaml

kubectl get nodes --output wide
kubectl get svc

echo "Done"