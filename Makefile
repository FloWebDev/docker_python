IDU := $(shell id -u)
IDG := $(shell id -g)

.PHONY: help build-up down

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Available commands:"
	@echo "  build-up  - Build, up and detach container."
	@echo "  build  - Remove container."
	@echo "  build  - Access to bash container."

build-up:
	docker-compose build --build-arg UID=$(IDU) --build-arg GID=$(IDG)
	docker-compose up -d
	echo "docker-compose up with USER: $(IDU)(uid) GROUP: $(IDG)(gid)"

down:
	docker-compose down --remove-orphans

bash:
	docker-compose exec -u www-data python bash

