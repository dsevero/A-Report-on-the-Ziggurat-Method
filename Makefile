.DELETE_ON_ERROR:
.PHONY: clean clear-cache install README.md report slides

clean:
	rm -rf \
		build dist dask-worker-space ziggurat.egg-info \
		.eggs .mypy_cache .pytest_cache venv .coverage* \
		build/

clear-cache:
	rm -rf ~/.cache/pypoetry/virtualenvs/ziggurat-py3.* poetry.lock

config:
	git config core.hooksPath .githooks

install:
	poetry run pip install pip==19.1.1
	poetry update -vv
	poetry install -vv

bin/gh-md-toc:
	mkdir -p bin
	wget https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc
	chmod a+x gh-md-toc
	mv gh-md-toc bin/

README.md:
	./bin/gh-md-toc --insert README.md
	rm -f README.md.orig.* README.md.toc.*

report slides:
	mkdir -p build/$@
	latexmk -lualatex -jobname=build/$@/$@ tex/$@.tex
