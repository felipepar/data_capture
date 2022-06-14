# Data Capture

A challenge program that must collect and display some basic statistics on a collection
of small positive integers.

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

This was a test for a position.

## Table of Contents

- [Technology](#technology)
- [Developing](#developing)
  - [Running the tests](#running-the-tests)

## Technology

- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/en/7.1.x/)

## Developing

1 - Clone the project

```
git clone https://github.com/felipepar/data-capture.git
```

2 - Change the directory

```
cd data_capture
```

3 - Install the requirements(optionally use a virtual environment):

```
pip3 install -r requirements.txt
```

4 - Run the example script:

```
python3 example.py
```

## Running the tests

```
pytest tests.py
```
