import pytest
import timeit
from balanced_group_system import BalancedGroupSystem

@pytest.fixture
def balanced_group_system_large():
  members = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
             '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
             '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
  return BalancedGroupSystem(members)

def test_calculate_balanced_groups_performance(balanced_group_system_large):
  def time_code():
    for _ in range(10):
      balanced_group_system_large.calculate_balanced_groups(4, balanced_group_system_large.members.copy())
  timing = timeit.timeit(time_code, number=1000)
  print('Time for calculate_balanced_groups: {} seconds'.format(timing))
  assert timing < 100

def test_create_balanced_groups_performance(balanced_group_system_large):
  def time_code():
    for _ in range(10):
      balanced_group_system_large.calculate_balanced_groups(4, balanced_group_system_large.members.copy())
  timing = timeit.timeit(time_code, number=1000)
  print('Time for calculate_balanced_groups: {} seconds'.format(timing))
  assert timing < 100
