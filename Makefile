install:
	hatch env create
	hatch env run pip install --upgrade pip
	hatch env run pip install .

collectstatic:
	hatch run python manage.py collectstatic --noinput

migrate:
	hatch run python manage.py migrate

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi