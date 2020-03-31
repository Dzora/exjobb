#!/bin/bash
docker tag descartesresearch/teastore-recommender gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender
docker tag descartesresearch/teastore-auth gcr.io/causal-bongo-266013/descartesresearch/teastore-auth
docker tag descartesresearch/teastore-webui gcr.io/causal-bongo-266013/descartesresearch/teastore-webui
docker tag descartesresearch/teastore-image gcr.io/causal-bongo-266013/descartesresearch/teastore-image
docker tag descartesresearch/teastore-persistence gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence
docker tag descartesresearch/teastore-registry gcr.io/causal-bongo-266013/descartesresearch/teastore-registry
docker tag descartesresearch/teastore-db gcr.io/causal-bongo-266013/descartesresearch/teastore-db
docker tag descartesresearch/teastore-base gcr.io/causal-bongo-266013/descartesresearch/teastore-base

echo "Done Tagging"

docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-auth
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-webui
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-image
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-registry
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-db
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-base

echo "Done pushing"
