# Playwright End-to-end Tests

## About

The purpose of this repo is to create a structured project for automating end-to-end tests.

## Project structure

Project implements Page Object Pattern architecture.

- **tests:** definition of test suites and scenarios

- **conftest.py:** allows you to define fixtures, plugins, and hooks that can be shared across multiple test files in a
  subdirectories.
- **pages:** main project library combines pages construction and behaviour in `page_objects`, pages locator
  definition and generation in `locators` and common elements like navbars or textinputs in `elements`.
- **pytest.ini** is a configuration file for Pytest that allows you to set options and modify the behavior of Pytest for
  a specific project.

## Installation

[Poetry](https://python-poetry.org/) is a dependency management and packaging tool for Python that helps you manage your
project's dependencies and
build your project. It's similar to pip, but provides additional features and benefits.

- **Dependency management:** Poetry provides version constraints, installation and updating of packages, and virtual
  environment management.

- **Lockfile:** Poetry generates a poetry.lock file that ensures that everyone working on the project uses the same set
  of dependencies with the same versions

- **Packaging:** Poetry generates a pyproject.toml file that
  describes your project and its dependencies, as well as a source distribution and wheel package that you can
  distribute to others.

- **Integration with other tools:** Poetry integrates with other tools, such as Pytest and Flake8, to help you manage
  your project's dependencies and testing.

### Installation using poetry

#### Installing Poetry

Poetry can be installed via python standard package manager PIP

    pip install poetry

#### Starting environment

To spawn poetry session inside your environment, write

    poetry shell

> This command starts a new shell and activates the virtual environment.
> As such, exit should be used to properly exit the shell and the virtual environment instead of deactivate.

#### Adding dependencies

To add a new dependency to your project, use the add command:

    poetry add <package>

This will add the requests package to your project and update the pyproject.toml file.

#### Installing dependencies

To install dependencies defined in `pyproject.toml`, simply run

    poetry install

### Pre-commit

Pre-commit is a framework used for pre-commits git hooks management. It allows to define actions that confirm that
written code is formatted and configured properly according to defined practices.

**TLDR** you cannot commit stuff unless it's green and your code fits the language guidelines
like [PEP8](https://peps.python.org/pep-0008/)

#### Running pre-commit automatically

To run validation automatically before each commit, please use:

    pre-commit install

This will add pre-commit to git hooks and perform all the checks defined in `.pre-commit-config.yaml`

#### Running pre-commit manually

To check stying in all files, please use:

    pre-commit run -a

#### pre-commit in CI

Every pull request should pass pre-commit stage to be merged

## Running tests

This project uses `pytest` with `pytest-playwright` as a test runner.

### Defining test choice

#### Running all

To run all the scripts with default setting simply type:

    pytest

#### Running specific test

    pytest tests/test_stx_blog.py::test_blog_page_and_filter_articles

#### Running tests matching given expression

    pytest -k stx

For more fancy ways of defining your suite check the official
markers [documentation](https://docs.pytest.org/en/latest/example/markers.html)

### Developer friendly run commands

This will run tests in a headed browser with a delay of 500 milliseconds between actions. It will make observing browser
behaviour easier.

    pytest --headed --slowmo 500
