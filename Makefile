install:
	hatch run pip install -r requirements.txt

collectstatic:
	hatch run python manage.py collectstatic --noinput

migrate:
	hatch run python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi