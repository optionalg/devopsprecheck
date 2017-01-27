build:
	python setup.py sdist
release:
	twine upload dist/*
tests:
	python -m unittest discover
