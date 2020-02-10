#!/bin/bash

echo "Starting"
kubectl apply -f ../TeaStore/TeaStore.yaml

gcloud compute firewall-rules create nodeport --allow tcp:30000-32767

kubectl get nodes --output wide
kubectl get svc

echo "Done"