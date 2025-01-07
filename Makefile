service-build:
	docker-compose build

service-up:
	docker-compose up -d

service-down:
	docker-compose down

service-clean:
	docker-compose down -v

api-up:
	docker start app

api-down:
	docker stop app

api-restart:
	docker restart app

api-log:
	docker-compose logs -f app
