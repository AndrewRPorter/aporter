all: clean test run

run:
	gunicorn --bind 0.0.0.0:8000 --workers 4 app.wsgi

test:
	pytest --disable-pytest-warnings tests

clean:
	rm -rf *.pyc
	rm -rf *__pycache__
