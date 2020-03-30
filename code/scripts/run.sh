#!/bin/bash
echo "Starting"

cd ../../../TeaStore 

mvn clean install -DskipTests -Dcheckstyle.skip

cd examples

sh docker_build.sh

cd docker

cd ../../../exjobb/code/scripts

docker logout gcr.io

docker-credential-gcloud get <<< "https://gcr.io"

docker login gcr.io

sh tagAndPushJaeger.sh

sh deployTeaStore.sh

echo "Done"