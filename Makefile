#!make

# docker-compose up
# python manage.py runserver
# celery -A config worker --loglevel=debug --concurrency=4
# celery -A quick_publisher beat

.PHONY: run
run:
	python src/manage.py runserver

.DEFAULT_GOAL := run