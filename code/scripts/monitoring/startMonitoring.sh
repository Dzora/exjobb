#!/bin/bash

cd ../../monitoring

kubectl apply -f namespace.yaml

kubectl apply -f clusterRole.yaml

kubectl apply -f config-map.yaml

kubectl apply -f prometheus-deployment.yaml

kubectl apply -f node-exporter.yaml

kubectl apply -f grafana-datasource-config.yaml

kubectl apply -f grafana-deployment.yaml