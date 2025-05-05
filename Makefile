start-with-py:
	python ./task1/script.py

start-with-docker:
	docker build -t statuses_checker -f ./task2/Dockerfile .
	docker run statuses_checker
