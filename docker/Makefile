SHELL=/bin/bash

name = python
ports = 8000:8000
path = $(shell pwd)
network = $(name)-net


.PHONY: build
build:
	@if [[ "$(shell docker images -q $(name) 2> /dev/null)" == "" ]]; then \
		cd $(path); docker build -t $(name) .; \
	else \
		echo "image: $(name) is already setup"; \
	fi

.PHONY: network
network:
	@if [[ "$(shell docker network inspect $(network) 2> /dev/null)" == "[]" ]]; then \
		docker network create $(network); \
	else \
		echo "network: $(network) is already setup"; \
	fi

.PHONY: run
run: build network
	# docker run --name $(name) --network=$(network) -v $(path):/code/ -d -p $(ports) $(name)
	@echo run

.PHONY: shell
shell: build network
	docker run --network=$(network) -v $(path):/code/ -p $(ports) -it --rm $(name) /bin/bash

.PHONY: stop
stop:
	docker stop $(name) 

.PHONY: rm
rm:
	docker rm $(name)

.PHONY: rmi
rmi:
	docker rmi $(name)

.PHONY: lint
lint:
	pylint --rcfile=lint.rc src/*.py

.PHONY: clean
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
