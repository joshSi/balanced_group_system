import pytest
from balanced_group_system import BalancedGroupSystem

@pytest.fixture
def balanced_group_system():
  return BalancedGroupSystem(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

def test_init(balanced_group_system):
  assert balanced_group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
  assert balanced_group_system.familiarity_matrix == [[0, 0, 0, 0, 0] for _ in range(5)]

def test_add_member(balanced_group_system):
  balanced_group_system.add_member('Frank')
  assert balanced_group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
  assert balanced_group_system.familiarity_matrix == [[0, 0, 0, 0, 0, 0] for _ in range(6)]

def test_remove_member(balanced_group_system):
  balanced_group_system.remove_member('Bob')
  assert balanced_group_system.members == ['Alice', 'Charlie', 'David', 'Eve']
  assert balanced_group_system.familiarity_matrix == [[0, 0, 0, 0] for _ in range(4)]

def test_create_groups(balanced_group_system):
  groups = [['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]
  balanced_group_system.create_groups(groups)
  assert balanced_group_system.familiarity_matrix[0][1] == 1
  assert balanced_group_system.familiarity_matrix[2][3] == 1
  assert balanced_group_system.familiarity_matrix[2][4] == 1
  assert balanced_group_system.familiarity_matrix[3][4] == 1

def test_update_familiarity(balanced_group_system):
  group = ['Alice', 'Bob', 'Charlie']
  balanced_group_system.update_familiarity(group)
  assert balanced_group_system.familiarity_matrix[0][1] == 1
  assert balanced_group_system.familiarity_matrix[0][2] == 1
  assert balanced_group_system.familiarity_matrix[1][2] == 1

def test_calculate_balanced_groups(balanced_group_system):
  groups = balanced_group_system.calculate_balanced_groups(2, balanced_group_system.members)
  assert len(groups) == 2
  assert all(len(group) >= 2 for group in groups)

def test_create_balanced_groups(balanced_group_system):
  groups = balanced_group_system.create_balanced_groups(2)
  assert len(groups) == 2
  assert all(len(group) >= 2 for group in groups)
