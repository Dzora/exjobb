#!/bin/bash

kubectl exec  -it $(kubectl get pod -l "app=jmeter" -o jsonpath='{.items[0].metadata.name}') -- bash