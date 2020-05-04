#!/bin/bash


kubectl apply -f ../../jaeger/production/cassandraConfigmap.yaml
cd ../../zipkin/production
kubectl apply -f cassandra-zipkin.yaml

echo "Wait for job... Use this to check status - kubectl get job jaeger-cassandra-schema-job"