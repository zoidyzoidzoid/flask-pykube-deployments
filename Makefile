.PHONY=dev run

dev:
	FLASK_DEBUG=1 FLASK_APP=app.py flask run
