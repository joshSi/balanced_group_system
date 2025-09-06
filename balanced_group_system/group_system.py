'''
group_system.py

This module contains a class that represents a group system that creates group_list and stores group history.
'''

class GroupSystem:  
  def __init__(self, members: list[str] = []):
    self.members: list[str] = members
    self.group_history: list[list[set[str]]] = []
  
  def __repr__(self) -> str:
    return f"GroupSystem({self.members})"

  def print_history(self) -> None:
    for i, group_set in enumerate(self.group_history):
      print(i, ':', group_set)
  
  def add_member(self, member: str) -> None:
    self.members.append(member)

  def remove_member(self, member: str) -> None:
    index = self.members.index(member)
    self.members.pop(index)

  def create_groups(self, group_list: list[set[str]]) -> None:
    self.group_history.append(group_list)

  # Slower version of create_groups that validates input
  def create_and_validate_groups(self, group_list: list[set[str]]) -> None:
    member_set = set(self.members)
    for group in group_list:
      for member in group:
        try:
          member_set.remove(member)
        except KeyError:
          raise KeyError("Element '{}' was not in members".format(member))
    self.group_history.append(group_list)
