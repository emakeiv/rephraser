#DOCKER_IMAGE_ID :=

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black app tests

lint:
	pylint --disable=R,C app

test:
	pytest -vv --cov=app tests/*

build:
	docker build -t rephraser-api-image .
	# $(eval DOCKER_IMAGE_ID := $(shell docker images -q rephraser-api-image))

run:
	docker run -p 127.0.0.1:8000:8000 rephraser-api-image:latest 

deploy:
	# deploy

all: install format lint test build deploy
