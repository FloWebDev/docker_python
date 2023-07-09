.PHONY: help build-up down

help:
	@echo "Usage: make [command]"
	@echo ""
	@echo "Available commands:"
	@echo "  build-up  - Build, up and detach container."
	@echo "  build  - Remove container."
	@echo "  build  - Access to bash container."

build-up:
	docker-compose up --build -d

down:
	docker-compose down --remove-orphans

bash:
	docker-compose exec python /bin/sh

