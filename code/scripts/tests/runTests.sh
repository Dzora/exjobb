#!/bin/bash

#Warmup 5 min
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 20 -JrampUp 2 -Jthroughput 300 -Jduration 300 -n
sleep 60s

# 20 users, 5req/s
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 20 -JrampUp 2 -Jthroughput 300 -Jduration 660 -n
sleep 60s

# 40 users, 5req/s
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 40 -JrampUp 2 -Jthroughput 300 -Jduration 660 -n
sleep 60s

# 60 users, 5req/s
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 60 -JrampUp 2 -Jthroughput 300 -Jduration 660 -n
sleep 60s

# 80 users, 5req/s
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 80 -JrampUp 2 -Jthroughput 300 -Jduration 660 -n
sleep 60s

# 100 users, 5req/s
java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 100 -JrampUp 2 -Jthroughput 300 -Jduration 660 -n

echo "Done Testing"