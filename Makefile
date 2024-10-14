up:
	docker-compose up
upb:
	docker-compose up --build
upd:
	docker-compose down
test:
	pytest --cov=main.app tests/

