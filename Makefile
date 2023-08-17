install:
    #installing dependencies
	pipenv install
format:
	#format code
lint:
	#pylint
test:
	#test
deploy:
	#deploy

all: install format lint test deploy