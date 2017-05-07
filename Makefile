init:
	pip install -r requirements.txt

test:
	nosetests -v --with-coverage --cover-branches --cover-package=quanteodstocks --cover-tests