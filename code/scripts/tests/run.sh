#!/bin/bash

if [ "$#" -ne 5 ]; then
	echo "You must enter exactly 4 command line arguments which should be [host,port,numUser,rampUp,loopCount "
	exit 1
fi
cd ../../../../JMeter/apache-jmeter-5.2.1/bin

java -jar ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname "$1" -Jport "$2" -JnumUser "$3" -JrampUp "$4" -JloopCount "$5" -n