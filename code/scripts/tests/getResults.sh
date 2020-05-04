#!/bin/bash

 kubectl cp default/$(kubectl get pod -l "app=jmeter" -o jsonpath='{.items[0].metadata.name}'):/src/apache-jmeter-5.2.1/results $PWD../../../results