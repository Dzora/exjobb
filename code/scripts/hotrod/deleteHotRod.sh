#!/bin/bash

echo "Starting"
kubectl delete svc/hotrod
kubectl delete svc/jaeger
kubectl delete deployment hotrod
kubectl delete deployment jaeger

gcloud compute firewall-rules delete nodeport
echo "Done"