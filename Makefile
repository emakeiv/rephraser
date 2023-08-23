install:
	pipenv install
format:
	black app tests
lint:
	pylint --disable=R,C app 
test:
	pytest -vv --cov=app tests/*	
build:
	#build container
deploy:
	#deploy

all: install format lint test build deploy