# Balanced Group System
A system for creating balanced groups from a list of members, aiming to maximize new interactions and minimize repeat meetings

Useful for organizations or events where networking and meeting new people is a priority. See [Social Golfer Problem](https://en.wikipedia.org/wiki/Social_golfer_problem)

![Tests](https://github.com/joshSi/balanced_group_system/actions/workflows/tests.yaml/badge.svg)

## Installation
```bash
pip install balanced_group_system
```

## Usage

To create 3 groups as close in size as possible from a list of members:

```python
from balanced_group_system import BalancedGroupSystem

members = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Harry"]

# Create a new BalancedGroupSystem object with a list of members.
bgs = BalancedGroupSystem(members)

# Generate groups. # Since there are 8 members, this will create 3 groups of sizes [3, 3, 2].
groups = bgs.create_balanced_groups(3)
print(groups)

# Add a new member to the group system, who will not have any familiarity with anyone.
bgs.add_member("Ivy")

for i in range(5):
  # Now, this will create 3 groups of sizes [3, 3, 3] each time.
  groups = bgs.create_balanced_groups(3)
  print(groups)

# Print the history of all previously generated groups to see how the system has balanced familiarity.
bgs.print_history()
```

The output is non-deterministic and may generate different groups each time it is run.

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
