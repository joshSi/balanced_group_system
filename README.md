# Balanced Group System
A system for creating balanced groups from a list of members, aiming to maximize new interactions and minimize repeat meetings

Useful for organizations or events where networking and meeting new people is a priority. See [Social Golfer Problem](https://en.wikipedia.org/wiki/Social_golfer_problem)

![Tests](https://github.com/joshSi/balanced_group_system/actions/workflows/tests.yaml/badge.svg)
## Testing
Make sure to have [Python](https://www.python.org/downloads/) (>=3.9) installed,
as well as the [poetry](https://pypi.org/project/poetry/) package.
```bash
pip install poetry
```

Once you have everything installed, navigate to the project directory and run the following command to install the project dependencies:

```bash
poetry install
```

Once the dependencies are installed, you can run the tests using the following command:

```bash
poetry run pytest
```

This command will automatically discover and run all tests in the project, which are located in the `tests` folder. Any failures or errors will be reported in the terminal output.

## License
This project is licensed under the MIT License - see LICENSE for details.
