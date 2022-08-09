gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
make lint:
	poetry run flake8 package/
	poetry run flake8 tests/
install:
	poetry install
test:
	poetry run pytest -vv --cov
