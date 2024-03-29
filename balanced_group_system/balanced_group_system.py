import random
from . import group_system

"""
BalancedGroupSystem.py

This module contains a subclass of GroupSystem that creates balanced groups based on the familiarity matrix.
It creates groups in such a way that members meet as many new members as possible and minimize repeat meetings.

Author: Joshua Si
"""

class BalancedGroupSystem(group_system.GroupSystem):
  def __init__(self, members: list[str] = []):
    super().__init__(members)
    self.familiarity_matrix: list[list[int]] = [[0 for _ in range(len(members))] for _ in range(len(members))]

  def __repr__(self) -> str:
    return f"BalancedGroupSystem({self.members})"
  
  def add_member(self, member: str) -> None:
    super().add_member(member)
    for row in self.familiarity_matrix:
      row.append(0)
    self.familiarity_matrix.append([0 for _ in range(len(self.members))])
  
  def remove_member(self, member: str) -> None:
    index = self.members.index(member)
    super().remove_member(member)
    for row in self.familiarity_matrix:
      row.pop(index)
    self.familiarity_matrix.pop(index)
    
  def create_groups(self, groups: list[list[str]]) -> list[list[str]]:
    super().create_groups(groups)
    for group in groups:
      self.update_familiarity(group)
    return groups

  def print_familiarity(self) -> None:
    print('  ',', '.join(self.members))
    for i, row in enumerate(self.familiarity_matrix):
      print(self.members[i], row)

  def evaluate_group(self, group: list[str]) -> int:
    score = 0
    for i, j in enumerate(group):
      for k in group[i+1:]:
        score += self.familiarity_matrix[self.members.index(j)][self.members.index(k)]
    return score
  
  def update_familiarity(self, group: list[str]) -> None:
    for i in range(len(group)):
      member_i = self.members.index(group[i])    
      for j in group[i+1:]:
        member_j = self.members.index(j)
        self.familiarity_matrix[member_j][member_i] += 1
        self.familiarity_matrix[member_i][member_j] += 1

  def calculate_balanced_groups(self, group_count: int, members: list[str] = [], verbose: bool = False) -> list[list[str]]:
    random.shuffle(members)
    groups = [[] for _ in range(group_count)]
    scores = {(): 0}
    # Memoized version of evaluate_group for evaluating score when adding one member
    def evaluate_member(group, member):
      group_key = tuple(sorted(group))
      new_key = tuple(sorted(group+[member]))
      if new_key in scores:
        return scores[new_key]
      score = scores[group_key]
      for i in group:
        score += self.familiarity_matrix[self.members.index(i)][self.members.index(member)]
      scores[new_key] = score + 1
      return score + 1

    # Balance and distribute members
    for member in members:
      min_group_index = min(range(group_count), key=lambda i: evaluate_member(groups[i], member))
      groups[min_group_index].append(member)
      if verbose:
        print(groups)
    return groups


  def create_balanced_groups(self, group_count: int) -> list[list[str]]:
    groups = self.calculate_balanced_groups(group_count, self.members.copy())
    return self.create_groups(groups)
