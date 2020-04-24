#!/bin/bash

kubectl delete svc prometheus-service -n monitoring

kubectl delete deployment prometheus-deployment -n monitoring

kubectl delete configmap prometheus-server-conf -n monitoring

kubectl delete clusterrole prometheus

kubectl delete clusterrolebinding prometheus

kubectl delete namespace monitoring