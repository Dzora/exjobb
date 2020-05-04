#!/bin/bash
cd ../../jaeger/production

kubectl apply -f cassandraConfigmap.yaml
kubectl apply -f cassandra.yaml

echo "Wait for job... Use this to check status - kubectl get job jaeger-cassandra-schema-job"

