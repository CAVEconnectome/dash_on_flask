# /bin/bash
docker build --no-cache -t gcr.io/neuromancer-seung-import/dashonflask:v$1 .
docker push gcr.io/neuromancer-seung-import/dashonflask:v$1
docker tag gcr.io/neuromancer-seung-import/dashonflask:v$1 docker.io/caveconnectome/dashonflask:v$1
docker push docker.io/caveconnectome/dashonflask:v$1