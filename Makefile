APP_DIR := $(patsubst %/,%,$(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
VENV ?= .venv

.PHONY: all check clean venv update-venv clean-venv clean-pyc

all: check
build: all
test: check

venv: $(VENV)/installed

$(VENV)/installed:
	type -p virtualenv || sudo pip install virtualenv
	test -d $(VENV) || virtualenv $(VENV)
	$(VENV)/bin/python $(VENV)/bin/pip install -r requirements.txt
	touch $(VENV)/installed

update-venv:
	$(VENV)/bin/python $(VENV)/bin/pip install -Ur requirements.txt

clean-venv:
	@ [ ! -w "$(VENV)" ] || rm -rf $(VENV)

clean-pyc:
	find $(APP_DIR) -name "*.pyc" -delete

clean-emacs:
	find $(APP_DIR) -name "*~" -delete

clean-data:
	$(RM) -rf $(APP_DIR)/data/*.trie
	$(RM) -f $(APP_DIR)/data/data.py*

build-data: venv
	$(VENV)/bin/python $(APP_DIR)/trinine/build.py $(APP_DIR)/data/words $(APP_DIR)/data/20k.txt

clean: clean-venv clean-pyc clean-emacs

flake-check:
	$(VENV)/bin/flake8 $(APP_DIR)/tests $(APP_DIR)/trinine

check-unit: venv flake-check
	$(VENV)/bin/nosetests $(APP_DIR)/tests

check: venv flake-check check-unit
