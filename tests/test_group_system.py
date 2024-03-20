import pytest
from balanced_group_system import GroupSystem

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
    grouplist1 = [['Alice', 'Bob'], ['Charlie', 'David', 'Eve']]
    grouplist2 = [['Alice', 'Bob'], ['Charlie'], ['David', 'Eve']]
    group_system.createGroups(grouplist1)
    group_system.createGroups(grouplist2)
    assert group_system.groupHistory == [grouplist1, grouplist2]

def test_create_validate_groups(group_system):
    # Test case: Member not in groupSystem.members
    with pytest.raises(KeyError) as exc_info:
        group_system.createAndValidateGroups([['Alice', 'Bob'], ['Charlie', 'David', 'Frank']])
        assert str(exc_info.value) == "Element 'Frank' was not in members list"
    
    # Test case: Duplicate member within a group
    with pytest.raises(ValueError) as exc_info:
        group_system.createAndValidateGroups([['Alice', 'Bob'], ['Charlie', 'Charlie']])
        assert str(exc_info.value) == "Duplicate members found in grouplist"
