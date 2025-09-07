import pytest
from balanced_group_system import AvailableGroupScheduler

@pytest.fixture
def available_group_system():
  return AvailableGroupScheduler(
    ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    [[True, True, True, True, False],
     [True, True, True, False, True],
     [True, True, False, True, True],
     [True, False, True, True, True],
     [False, True, True, True, True]]
  )

def test_init(available_group_system):
  assert available_group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
  assert available_group_system.group_history == []
  assert available_group_system.familiarity_matrix == {
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

def test_create_balanced_schedules(available_group_system):
  assert available_group_system.create_balanced_schedules(4) == [
    {'Alice', 'Bob', 'Charlie', 'David'},
    {'Alice', 'Bob', 'Charlie', 'Eve'},
    {'Alice', 'Bob', 'David', 'Eve'},
    {'Alice', 'Charlie', 'David', 'Eve'},
    {'Bob', 'Charlie', 'David', 'Eve'}
  ]

def test_get_balanced_group(available_group_system):
  assert available_group_system.get_balanced_group({'Alice', 'Bob', 'Charlie', 'David'}, set(), 4) == {'Alice', 'Bob', 'Charlie', 'David'}
  assert available_group_system.get_balanced_group({'Alice', 'Bob', 'Charlie'}, {'David'}, 4) == {'Alice', 'Bob', 'Charlie', 'David'}