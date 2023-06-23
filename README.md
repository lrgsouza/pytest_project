
# API Tests using Pytest

This project is focused on developing and executing tests using the Pytest framework to verify the functionality and reliability of an API that generates random data. The tests will include unit tests, integration tests, acceptance tests, and load tests, and will be created using Pytest and the requests library. The main goal of the project is to provide comprehensive test coverage and ensure the stability and accuracy of the API.

## Installation

1. Clone the project repository to your local environment:

   ```bash
   git clone https://github.com/lrgsouza/pytest_project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pytest_project
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

4. Install the project dependencies:

   ```bash
    pip install pytest pytest-html
   ```

## Usage

Run the command below in your terminal:
   ```bash
    pytest --html=report.html
   ```

This will run the tests and generate a HTML file, named report.html, where you can see more details about each test.

## Why Pytest is Great!

You will see below two great functions that makes Pytest the best!

1. Pytest has plugins that increase its power. One example is _pytest-html_, that we use in this software.

2. Pytest allows you to reply the same test for each item in a list, as you can see in this example:

```python
@pytest.mark.parametrize("resource", ["users", "addresses", "banks"])
def test_load(resource):
    result = get_random_data(resource, size=100)
    assert isinstance(result, list)
    assert len(result) == 100
```

The _resource_ variable is a list containing 3 items. It means that the test will be processed 1 time for each of them.


## Authors

- Lucas R. G. Souza [@lrgsouza](https://github.com/lrgsouza)
- Airton G. Carvalho [@airtong](https://github.com/airtong)