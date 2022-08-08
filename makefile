gendiff -N:
	poetry run gendiff -h
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
make lint:
	poetry run flake8 package/
install:
	poetry install
