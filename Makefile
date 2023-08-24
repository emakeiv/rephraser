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
	docker build -t phraser-api .
	# $(eval DOCKER_IMAGE_ID := $(shell docker images -q phraser-api))

run:
	docker run -p 127.0.0.1:8000:8000 phraser-api:latest 

deploy:
	# deploy

all: install format lint test build deploy
