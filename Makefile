NEW_PYTHONPATH="`pwd`/src:$(PYTHONPATH)"

install:
	@pip install -r requirements.txt

clean:
	@find . -name "*.pyc" -delete

run_mediator:
	PYTHONPATH="$(NEW_PYTHONPATH)" python -m olap2datacube.mediator

run_catalogue:
	PYTHONPATH="$(NEW_PYTHONPATH)" python -m olap2datacube.catalogue

test:
	@nosetests -s --tests=tests
