SHELL := bash -eou pipefail

# Change it to have a slow and fast

.PHONY: all
all:| format ci

.PHONY: ci
ci:| lint check test cluster-up cluster-test cluster-down

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
	# poetry poly check
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
	ctlptl apply -f dev-cluster.yaml
	
.PHONY: cluster-test
cluster-test:
	tilt ci

.PHONY: cluster-down
cluster-down:
	ctlptl delete -f dev-cluster.yaml

.PHONY: clean
clean:
	git clean -dfX
