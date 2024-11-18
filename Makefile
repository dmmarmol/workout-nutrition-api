IMAGE_NAME=nutrition-api
IMAGE_VERSION=0.0.3
HOST_PORT=6001
CONTAINER_PORT=8000
HOST_SOURCE_DIR=$(shell pwd)/src
CONTAINER_SOURCE_DIR=/nutrition-api/src
ENV_FILE_PATH=$(shell pwd)/../.env

build:
	docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .

run:
	echo "Container: ${IMAGE_NAME}"
	echo "Image used: ${IMAGE_NAME}:${IMAGE_VERSION}"
	echo "Host Source Dir: ${HOST_SOURCE_DIR}"
	echo "Env used: ${ENV_FILE_PATH}"
	docker run -d \
		--name ${IMAGE_NAME} \
		--env-file ${ENV_FILE_PATH} \
		-p ${HOST_PORT}:${CONTAINER_PORT} \
		-v ${HOST_SOURCE_DIR}:${CONTAINER_SOURCE_DIR} \
		${IMAGE_NAME}:${IMAGE_VERSION}

logs:
	docker logs -f ${IMAGE_NAME}

exec:
	docker exec -it ${IMAGE_NAME} /bin/bash

remove:
	docker rm ${IMAGE_NAME}

stop:
	docker stop ${IMAGE_NAME}

delete:
	make stop
	make remove

restart:
	docker restart ${IMAGE_NAME}

# Be careful: this removes unused images, networks, and containers
prune:
	docker system prune -f

req:
	pip freeze > requirements.txt
