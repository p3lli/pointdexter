#!/bin/bash
IMAGE_NAME=pointdexter
TAG_DATE=`date +%Y%m%d%H%M%S`
docker build . -t ${IMAGE_NAME}:${TAG_DATE}
