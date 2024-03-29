import pytest
from balanced_group_system import GroupSystem

@pytest.fixture
def group_system():
  return GroupSystem(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

def test_init(group_system):
  assert group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
  assert group_system.group_history == []

def test_add_member(group_system):
  group_system.add_member('Frank')
  assert group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

def test_remove_member(group_system):
  group_system.remove_member('Bob')
  assert group_system.members == ['Alice', 'Charlie', 'David', 'Eve']

def test_create_groups(group_system):
  group_list1 = [['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]
  group_list2 = [['Alice', 'Bob'], ['Charlie'], ['David', 'Eve']]
  group_system.create_groups(group_list1)
  group_system.create_groups(group_list2)
  assert group_system.group_history == [group_list1, group_list2]

def test_create_validate_groups(group_system):
  # Test case: Member not in groupSystem.members
  with pytest.raises(KeyError) as exc_info:
    group_system.create_and_validate_groups([['Alice', 'Bob'], ['Charlie', 'David', 'Frank']])
    assert str(exc_info.value) == "Element 'Frank' was not in members list"
  
  # Test case: Duplicate member within a group
  with pytest.raises(ValueError) as exc_info:
    group_system.create_and_validate_groups([['Alice', 'Bob'], ['Charlie', 'Charlie']])
    assert str(exc_info.value) == "Duplicate members found in group_list"
