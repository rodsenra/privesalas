NEW_PYTHONPATH="`pwd`/src:$(PYTHONPATH)"

install:
	@pip install -r requirements.txt

clean:
	@find . -name "*.pyc" -delete

run_mediator:
	PYTHONPATH="$(NEW_PYTHONPATH)" python -m olap2datacube.mediator

test:
	@nosetests -s --tests=tests
