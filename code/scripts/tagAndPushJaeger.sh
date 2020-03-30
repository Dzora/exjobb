#!/bin/bash
docker tag descartesresearch/teastore-recommender gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender:jaeger
docker tag descartesresearch/teastore-auth gcr.io/causal-bongo-266013/descartesresearch/teastore-auth:jaeger
docker tag descartesresearch/teastore-webui gcr.io/causal-bongo-266013/descartesresearch/teastore-webui:jaeger
docker tag descartesresearch/teastore-image gcr.io/causal-bongo-266013/descartesresearch/teastore-image:jaeger
docker tag descartesresearch/teastore-persistence gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence:jaeger
docker tag descartesresearch/teastore-registry gcr.io/causal-bongo-266013/descartesresearch/teastore-registry:jaeger
docker tag descartesresearch/teastore-db gcr.io/causal-bongo-266013/descartesresearch/teastore-db:jaeger
docker tag descartesresearch/teastore-base gcr.io/causal-bongo-266013/descartesresearch/teastore-base:jaeger

echo "Done Tagging"

docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-recommender:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-auth:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-webui:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-image:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-persistence:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-registry:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-db:jaeger
docker push gcr.io/causal-bongo-266013/descartesresearch/teastore-base:jaeger

echo "Done pushing"
