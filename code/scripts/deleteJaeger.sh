#!/bin/bash

echo "Starting"
kubectl delete svc/jaeger
kubectl delete deployment jaeger

gcloud compute firewall-rules delete nodeport
echo "Done"