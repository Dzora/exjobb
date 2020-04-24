#!/bin/bash
echo "Starting"
kubectl delete pods,deployments,services -l app=teastore
kubectl delete configmap tracing-config
echo "Done"