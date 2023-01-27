
run:
	python manage.py runserver

migrate:
	python manage.py makemigrations  
	python manage.py migrate 

enable_rabbit:
	sudo systemctl enable rabbitmq-server

start_rabbit:
	sudo systemctl start rabbitmq-server

stop_rabbit:
	sudo systemctl stop

status_rabbit:
	systemctl status rabbitmq-server

start_celery_worker:
	celery -A mail_delivery worker -l info