export PYSTRAY_BACKEND=gtk

run:
	@pipenv run python src/app.py

lint:
	@pipenv run black .
	@pipenv run isort .
