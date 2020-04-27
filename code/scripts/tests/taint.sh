#!/bin/bash

test=$(kubectl get nodes -o=name)

array=($test)

kubectl taint nodes "${array[0]}" node1:NoSchedule
kubectl taint nodes "${array[1]}" node2:NoSchedule
kubectl taint nodes "${array[2]}" node3:NoSchedule
kubectl taint nodes "${array[3]}" node4:NoSchedule

