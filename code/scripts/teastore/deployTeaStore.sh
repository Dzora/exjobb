#!/bin/bash

echo "Starting"
kubectl apply -f ../../TeaStore/tracing-config.yaml
kubectl apply -f ../../TeaStore/localTeaStoreWithTolerations.yaml



kubectl get nodes --output wide
kubectl get svc

echo "Done"