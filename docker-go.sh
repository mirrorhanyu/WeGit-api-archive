#!/usr/bin/env bash

set -e

IMAGE_NAME=callmehan/gitter-server

docker build -t $IMAGE_NAME:3 .