all: clean test run

run:
	gunicorn --bind 0.0.0.0:8000 --workers 4 app.wsgi

docker-run:
	sudo docker build -t dev/aporter .
	sudo docker run -it -p 8000:8000 dev/aporter

test:
	pytest -rav tests

clean:
	rm -rf *.pyc
	rm -rf *__pycache__
