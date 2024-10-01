# pytest-example

This projects demonstrates how to use `pytest`and `pytest-mock` (unittest.mock wrapper) to assert validity in layered API architecture.


## Init

``` bash
# create a virtual env
python -m venv .venv

# activate the venv
source .venv/bin/activate

# install dependencies into .venv
pip install -r requirements.txt
```


## Run API

```
uvicorn app.main:app --reload
```


## Inovke api

```
curl -X GET http://localhost:8000/items
```


## Tests

Run the `pytest` command to run all available tests
