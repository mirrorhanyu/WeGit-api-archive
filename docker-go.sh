#!/usr/bin/env bash

set -e

IMAGE_NAME=gitter-server

docker build -t $IMAGE_NAME .

docker run --rm -d -p 5000:5000 $IMAGE_NAME