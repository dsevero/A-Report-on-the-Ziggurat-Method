.PHONY: clean clear-cache tests docker-build docker-tests

clean:
	rm -rf \
		build dist dask-worker-space ziggurat.egg-info \
		.eggs .mypy_cache .pytest_cache venv .coverage*

clear-cache:
	rm -rf ~/.cache/pypoetry/virtualenvs/ziggurat-py3.* poetry.lock

install:
	poetry run pip install pip==19.1.1
	poetry update -vv
	poetry install -vv
