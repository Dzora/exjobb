#!/bin/bash
echo "Starting"
kubectl delete pods,deployments,services -l app=teastore
gcloud compute firewall-rules delete nodeport
echo "Done"