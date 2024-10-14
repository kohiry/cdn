up:
	docker-compose up
upb:
	docker-compose up --build
upd:
	docker-compose down
test:
	pytest --cov=app tests/

