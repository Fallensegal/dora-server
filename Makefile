SHELL := bash -eou pipefail

.PHONY: all
all:| format ci

.PHONY: ci
ci:| lint check test cluster-test

.PHONY: install
install: .venv

.venv: poetry.lock
	poetry install --sync
	@touch $@

.PHONY: format
format: install
	poetry poly sync
	poetry run ruff check --fix-only .
	poetry run ruff format --check .

.PHONY: lint
lint: install
	poetry poly check 
	poetry run ruff check --no-fix-only .
	poetry run ruff format --check .
	

.PHONY: check
check: install
	poetry run mypy .

.PHONY: test
test: install
	poetry run pytest

.PHONY: cluster-up
cluster-up:
	minikube start \
		--driver=docker \
		--cpus="2" \
		--memory="4g" \
		--kubernetes-version="v1.27.4" \
		--addons="ingress" \
		--addons="ingress-dns" \
		--wait=all

.PHONY: cluster-down
cluster-down:
	minikube stop

.PHONY: clean
clean:
	git clean -dfX
