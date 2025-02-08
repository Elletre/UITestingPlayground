# UITestingPlayground Automation with Playwright

## Overview

This project automates UI tests for UITestingPlayground using Playwright and pytest. The tests cover various UI interactions such as button clicks, AJAX requests, dynamic elements, and input field validation.

## Features

Automated UI testing with Playwright (async)

Page Object Model (POM) for better test structure

Parallel test execution using pytest-xdist

Supports Chromium, Firefox, and WebKit

Headless and Headed browser execution

## Installation

1. Clone the Repository

2. Create a Virtual Environment (Optional but Recommended)

3. Install Dependencies
```commandline
pip install -r requirements.txt
```

## Running the Tests
### Run All Tests
```commandline
pytest
```


Run Tests in Parallel (4 processes)
```commandline
pytest -n 4
```

Run Tests in a Visible Browser (Headed Mode)
```commandline
pytest --headed
```


Run a Specific Test File
```commandline
pytest tests/test_dynamic_id.py
```

Run a Specific Test Case
```commandline
pytest -k "test_dynamic_id"
```

Running Tests on Different Browsers
By default, Playwright runs tests in Chromium. You can specify a different browser:

```commandline
pytest --browser=firefox
```

```commandline
pytest --browser=webkit
```


