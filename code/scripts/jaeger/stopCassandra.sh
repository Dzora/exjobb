#!/bin/bash

kubectl delete configmap jaeger-configuration
kubectl delete service cassandra
kubectl delete statefulset cassandra