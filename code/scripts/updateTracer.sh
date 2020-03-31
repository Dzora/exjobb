#!/bin/bash

kubectl apply -f ../TeaStore/tracing-config.yaml

kubectl scale deployment/teastore-webui --replicas=0;
kubectl scale deployment/teastore-webui --replicas=1;

kubectl scale deployment/teastore-persistence --replicas=0;
kubectl scale deployment/teastore-persistence --replicas=1;

kubectl scale deployment/teastore-auth --replicas=0;
kubectl scale deployment/teastore-auth --replicas=1;

kubectl scale deployment/teastore-recommender --replicas=0;
kubectl scale deployment/teastore-recommender --replicas=1;

kubectl scale deployment/teastore-image --replicas=0;
kubectl scale deployment/teastore-image --replicas=1;

