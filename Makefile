PYTHON := $(shell which python)

ifeq ($(PYTHON),)
	PYTHON := $(shell which python3)
endif

VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
PIP := $(VENV_PYTHON) -m pip

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

install-dependencies: $(VENV_PYTHON)
	$(PIP) install -r requirements.txt

run-prj1: install-dependencies
	$(VENV_PYTHON) project_1/analyze_data.py

clean:
	rm -rf $(VENV)