SHELL := bash -eou pipefail

.PHONY: all
all:| format ci

.PHONY: ci
ci:| lint check test

.PHONY: install
install: .venv

.venv: poetry.lock
	poetry install --sync
	@touch $@

.PHONY: format
format: install
	poetry poly sync
	poetry run ruff --quiet --fix-only .
	poetry run black --quiet .
	poetry run toml-sort --check pyproject.toml \
	|| poetry run toml-sort pyproject.toml

.PHONY: lint
lint: install
	poetry poly check --quiet
	poetry run ruff --quiet --no-fix-only .
	poetry run black --quiet --check .
	poetry run toml-sort --check pyproject.toml

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
