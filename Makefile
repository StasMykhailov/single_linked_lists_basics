build_core:
	docker-compose build core

start_core:
	docker-compose up -d core

stop_core:
	docker-compose stop core

run_tests:
	docker-compose up --build tests
