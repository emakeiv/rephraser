install:
	pipenv install
format:
	black app tests
lint:
	pylint --disable=R,C app
test:
	#test
build:
	#build container
deploy:
	#deploy

all: install format lint test deploy