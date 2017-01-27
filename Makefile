build:
	python setup.py sdist
release:
	twine upload dist/*
tests:
	python -m unittest discover

pylintcheck:
	@for f in `find . -iname "*.py"`; do\
		pylint -E $$f;\
	done
# python -m unittest tests.test_paramater_helper
