# JSONPlaceholder Client Application

## Description
A Python application that interacts with the JSONPlaceholder API, demonstrating OOP, type hinting, testing, and CI/CD practices.

## Prerequisites
- Python 3.10 or higher
- Virtualenv (optional, but recommended)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vic-bot-boss/BangOlufsen_task.git
   cd BangOlufsen_task
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```   

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the application:
```bash
python src/main.py
```

This fetches and prints data from the /posts and /users endpoints of the JSONPlaceholder API.

## Running tests

To run the tests:
```bash
pytest
```

### Checking for type errors with MyPy

To check for type errors using Mypy:
```bash
mypy src/ tests/
```

### Coverage report results

To generate a test coverage report, run:
```bash
pytest --cov=src tests/
```

The current test coverage of the project is as follows:

```bash
---------- coverage: platform win32, python 3.10.6-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
src\__init__.py       0      0   100%
src\main.py          25      3    88%
-------------------------------------
TOTAL                25      3    88%
```

## Continuous Integration

This project uses GitHub Actions to automate the testing process. The workflow can be triggered manually via the GitHub Actions tab in the repository.

The workflow runs the following checks:
- **Mypy** for static type checking.
- **Pytest** for running the test suite.
- **Test coverage report** is generated using `pytest-cov`.

## Conclusion

Thank you for reviewing this project. I have learned a lot about testing through it.
