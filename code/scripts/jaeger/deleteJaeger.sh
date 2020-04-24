#!/bin/bash

echo "Starting"
kubectl delete svc/jaeger
kubectl delete deployment jaeger

echo "Done"