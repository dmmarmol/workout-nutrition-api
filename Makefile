IMAGE_NAME=nutrition-api
IMAGE_VERSION=0.0.2
HOST_PORT=6001
CONTAINER_PORT=8000
HOST_SOURCE_DIR=./src
CONTAINER_SOURCE_DIR=/nutrition-api/src
ENV_FILE_PATH="../.env"

build:
	docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} .

run:
	docker run -d \
		--name ${IMAGE_NAME} \
		--env-file ${ENV_FILE_PATH} \
		-p ${HOST_PORT}:${CONTAINER_PORT} \
		-v ${HOST_SOURCE_DIR}:${CONTAINER_SOURCE_DIR} \
		${IMAGE_NAME}:${IMAGE_VERSION}

stop:
	docker stop ${IMAGE_NAME}

restart:
	docker restart ${IMAGE_NAME}

# Be careful: this removes unused images, networks, and containers
prune:
	docker system prune -f

req:
	pip freeze > requirements.txt
