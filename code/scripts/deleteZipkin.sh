#!/bin/bash

echo "Starting"
kubectl delete svc/zipkin
kubectl delete deployment zipkin

echo "Done"