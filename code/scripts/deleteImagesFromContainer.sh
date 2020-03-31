#!/bin/bash
echo "Deleting"
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-auth
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-webui
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-image
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-base
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-registry
"Y" |gcloud container images delete gcr.io/causal-bongo-266013/descartesresearch/teastore-db
echo "Done"