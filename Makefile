


all:
	pip uninstall sus -y
	rm -rf dist build
	python setup.py install

clean:
	rm -rf dist build *.egg-info

push:
	twine upload dist/*