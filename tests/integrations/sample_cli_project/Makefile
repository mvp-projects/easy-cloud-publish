.DEFAULT_GOAL := help
SHELL:=/usr/bin/env bash
OS = $(shell uname | tr A-Z a-z)

.PHONY: build-image
build-image:  ## Build docker image
	docker build -t simple-cli:latest -f docker/Dockerfile .

.PHONY: run-ephemeral
run-ephemeral: ## Run command in an ephemeral container
	docker run --rm simple-cli:latest $(command)

.PHONY: remove-image
remove-image: ## Remove image
	docker rmi simple-cli:latest 

.PHONY: help
help:
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'
