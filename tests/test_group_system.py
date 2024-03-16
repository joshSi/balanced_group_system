import pytest
from balanced_group_system.group_system import GroupSystem

@pytest.fixture
def group_system():
    # Initialize GroupSystem instance with some initial members
    return GroupSystem(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

def test_init(group_system):
    assert group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    assert group_system.groupHistory == []

def test_add_member(group_system):
    group_system.addMember('Frank')
    assert group_system.members == ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

def test_remove_member(group_system):
    group_system.removeMember('Bob')
    assert group_system.members == ['Alice', 'Charlie', 'David', 'Eve']

def test_create_groups(group_system):
    groups = [['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]
    group_system.createGroups(groups)
    assert group_system.groupHistory == [[['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]]

