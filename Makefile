start-with-py:
	python ./task1/script.py

start-with-docker:
	docker build -t your_image_name -f ./task2/Dockerfile .
	docker run statuses_checker
