#!/bin/bash
echo "Deleting"
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-auth:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-webui:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-image:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence:jaeger --force-delete-tags
"Y" | gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-base:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-registry:jaeger --force-delete-tags
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-db:jaeger --force-delete-tags
echo "Done"