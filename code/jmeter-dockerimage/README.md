#Dockerimage for Jmeter and flask server
#Starts dummy flask server - printing hello world

# Create docker image from dockerfile:
# docker build -t your_image_name .

# run docker image:
# docker run -it --name your_image_name -p 80:80 -p 5000:5000 your_image_name

# create docker image on cloud --- correct project must be set with "set project"
# gcloud builds submit --tag gcr.io/[PROJECT-ID]/[IMAGE]

# Access jmeter
# kubectl exec -it pod_name -- bash

# Run jmeter from bash inside pod
# java -jar ./bin/ApacheJMeter.jar -t teastore_browse_nogui.jmx -Jhostname $TEASTORE_WEBUI_SERVICE_HOST -Jport 8080 -JnumUser 100 -JrampUp 0 -Jduration 60 -Jthroughput 3000 -JaggregateFile agg.csv  -n
