#!/bin/bash

echo "Starting"

kubectl delete deployment jaeger-collector
kubectl delete svc/jaeger-collector
kubectl delete deployment jaeger-query
kubectl delete svc/jaeger-query
kubectl delete ds jaeger-agent

echo "Done"