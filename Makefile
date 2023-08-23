install:
	pipenv install
format:
	black app tests
lint:
	pylint --disable=R,C app 
test:
	pytest -vv --cov=app tests/*	
build:
	docker build -t phraser-api .
run:
	docker run -p 127.0.0.1:8000:8000 4bce3ab7c8a0
deploy:
	#deploy

all: install format lint test build deploy