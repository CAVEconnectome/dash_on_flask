export DOCKER_DEFAULT_PLATFORM=linux/amd64
docker run -v ${PWD}:/app python:3.10 /bin/bash -c "cd /app && pip install pip-tools && pip-compile -v -r requirements.in"