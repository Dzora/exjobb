#!/bin/bash

cd ../../../../JMeter/apache-jmeter-5.2.1/bin

kubectl cp teastore_browse_nogui.jmx default/$(kubectl get pod -l "app=jmeter" -o jsonpath='{.items[0].metadata.name}'):/src/apache-jmeter-5.2.1/