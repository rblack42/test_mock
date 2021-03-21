.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow
	pip install --upgrade pip

.PHONY: reqs
reqs:
	pip install -r requirements.txt

.PHONY: test
test:
	python -m pytest -vvv

.PHONY: run
run:
	python -m mmdesigner

.PHONY: nb
nb:
	jupyter notebook
