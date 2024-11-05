IMAGE_NAME=nutrition-api
IMAGE_VERSION=0.0.1
HOST_PORT=6001
CONTAINER_PORT=8000
HOST_SOURCE_DIR=./src
CONTAINER_SOURCE_DIR=/nutrition-api/src

build:
	docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .

run:
	docker run -d \
		--name ${IMAGE_NAME} \
		-p ${HOST_PORT}:${CONTAINER_PORT} \
		-v ${HOST_SOURCE_DIR}:${CONTAINER_SOURCE_DIR} \
		${IMAGE_NAME}:${IMAGE_VERSION}

req:
	pip freeze > requirements.txt
