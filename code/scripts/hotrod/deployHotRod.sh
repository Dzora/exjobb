#!/bin/bash

echo "Starting"
kubectl apply -f ../../hotrod/hotrod-deployment.yaml
kubectl apply -f ../../hotrod/hotrod-service.yaml

gcloud compute firewall-rules create nodeport --allow tcp:30000-32767 --destination-ranges 194.132.164.168

kubectl get nodes --output wide
kubectl get svc

echo "Done"