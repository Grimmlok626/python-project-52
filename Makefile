install:
	hatch env create
	hatch env run pip install -e .

collectstatic:
	hatch env run python manage.py collectstatic --noinput

migrate:
	hatch env run python manage.py migrate

build:
	./build.sh

render-start:
	hatch run gunicorn task_manager.wsgi