import pytest
from balanced_group_system import BalancedGroupSystem

@pytest.fixture
def balanced_group_system():
  return BalancedGroupSystem(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

def test_init(balanced_group_system):
  assert balanced_group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
  assert balanced_group_system.familiarity_matrix == {
    frozenset(('Alice', 'Bob')) : 0,
    frozenset(('Alice', 'Charlie')) : 0,
    frozenset(('Alice', 'David')) : 0,
    frozenset(('Alice', 'Eve')) : 0,
    frozenset(('Bob', 'Charlie')) : 0,
    frozenset(('Bob', 'David')) : 0,
    frozenset(('Bob', 'Eve')) : 0,
    frozenset(('Charlie', 'David')) : 0,
    frozenset(('Charlie', 'Eve')) : 0,
    frozenset(('David', 'Eve')) : 0,
  }

def test_add_member(balanced_group_system):
  balanced_group_system.add_member('Frank')
  assert balanced_group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
  assert balanced_group_system.familiarity_matrix == {
    frozenset(('Alice', 'Bob')) : 0,
    frozenset(('Alice', 'Charlie')) : 0,
    frozenset(('Alice', 'David')) : 0,
    frozenset(('Alice', 'Eve')) : 0,
    frozenset(('Bob', 'Charlie')) : 0,
    frozenset(('Bob', 'David')) : 0,
    frozenset(('Bob', 'Eve')) : 0,
    frozenset(('Charlie', 'David')) : 0,
    frozenset(('Charlie', 'Eve')) : 0,
    frozenset(('David', 'Eve')) : 0,
    frozenset(('Frank', 'Alice')) : 0,
    frozenset(('Frank', 'Bob')) : 0,
    frozenset(('Frank', 'Charlie')) : 0,
    frozenset(('Frank', 'David')) : 0,
    frozenset(('Frank', 'Eve')) : 0,
  }

def test_remove_member(balanced_group_system):
  balanced_group_system.remove_member('Bob')
  assert balanced_group_system.members == ['Alice', 'Charlie', 'David', 'Eve']
  assert balanced_group_system.familiarity_matrix == {
    frozenset(('Alice', 'Charlie')) : 0,
    frozenset(('Alice', 'David')) : 0,
    frozenset(('Alice', 'Eve')) : 0,
    frozenset(('Charlie', 'David')) : 0,
    frozenset(('Charlie', 'Eve')) : 0,
    frozenset(('David', 'Eve')) : 0,
  }

def test_create_groups(balanced_group_system):
  groups = [['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]
  balanced_group_system.create_groups(groups)
  assert balanced_group_system.group_history[0] == groups
  assert balanced_group_system.familiarity_matrix[frozenset(('Alice', 'Bob'))] == 2
  assert balanced_group_system.familiarity_matrix[frozenset(('Charlie', 'David'))] == 2
  assert balanced_group_system.familiarity_matrix[frozenset(('Charlie', 'Eve'))] == 2
  assert balanced_group_system.familiarity_matrix[frozenset(('David', 'Eve'))] == 2

def test_update_familiarity(balanced_group_system):
  group = ['Alice', 'Bob', 'Charlie']
  balanced_group_system.update_familiarity(group)
  assert balanced_group_system.familiarity_matrix[frozenset(('Alice', 'Bob'))] == 2
  assert balanced_group_system.familiarity_matrix[frozenset(('Alice', 'Charlie'))] == 2
  assert balanced_group_system.familiarity_matrix[frozenset(('Bob', 'Charlie'))] == 2

def test_calculate_balanced_groups(balanced_group_system):
  groups = balanced_group_system.calculate_balanced_groups(2, balanced_group_system.members)
  assert len(groups) == 2
  assert all(len(group) >= 2 for group in groups)

def test_create_balanced_groups(balanced_group_system):
  groups = balanced_group_system.create_balanced_groups(2)
  assert len(groups) == 2
  assert all(len(group) >= 2 for group in groups)
