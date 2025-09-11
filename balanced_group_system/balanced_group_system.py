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
    self.familiarity_matrix: dict[frozenset[tuple[str, str]], int] = {
        frozenset((self.members[i], self.members[j])) : 0
        for i in range(len(self.members))
        for j in range(i+1, len(self.members))
    }

  def __repr__(self) -> str:
    return f"BalancedGroupSystem({self.members})"
  
  def add_member(self, member: str) -> None:
    super().add_member(member)
    for i in range(len(self.members)-1):
      self.familiarity_matrix[frozenset((self.members[i], member))] = 0
  
  def remove_member(self, member: str) -> None:
    try:
      super().remove_member(member)
      for m in self.members:
        self.familiarity_matrix.pop(frozenset((m, member)))
    except ValueError:
      raise ValueError("Member '{}' was not in members".format(member))
    
  def create_groups(self, groups: list[set[str]]) -> list[set[str]]:
    super().create_groups(groups)
    for group in groups:
      self._update_familiarity(group)
    return groups

  def print_familiarity(self) -> None:
    for i in self.members:
      print(i, end=' ')
    print()
    for i in self.members:
      print(i, end=' ')
      for j in self.members:
        if i == j:
          print('-', end=' ')
        else:
          print(self.familiarity_matrix[frozenset((i, j))], end=' ')
      print()

  def evaluate_group(self, group: set[str]) -> int:
    score = 0
    pairs = ((i, j) for i in group for j in group if i != j)
    score = sum(self.familiarity_matrix[frozenset(pair)] for pair in pairs)
    return score
  
  '''
  Update familiarity matrix with given group. Used internally when creating groups.
  '''
  def _update_familiarity(self, group: set[str]) -> None:
    pairs = ((i, j) for i in group for j in group if i != j)
    for pair in pairs:
      self.familiarity_matrix[frozenset(pair)] += 1

  '''
  Calculate a possible set of balanced groups by trying to minimize score when choosing which group to add each member to.
  Dry run equivalent to create_balanced_groups that does not update group history or familiarity matrix.
  '''
  def _calculate_balanced_groups(self, group_count: int, members: list[str] = [], verbose: bool = False) -> list[set[str]]:
    random.shuffle(members)
    groups = [set() for _ in range(group_count)]
    scores = {(): 0}
    # Memoized version of evaluate_group for evaluating score when adding one member
    def evaluate_member(group: set[str], member: str) -> int:
      new_group: set[str] = group | {member}
      if frozenset(new_group) in scores:
        return scores[frozenset(new_group)]
      score = scores[frozenset(group)] if frozenset(group) in scores else 0
      for i in group:
        score += self.familiarity_matrix[frozenset((i, member))]
      scores[frozenset(new_group)] = score + 2
      return score + 2

    # Balance and distribute members
    for member in members:
      min_group_index = min(range(group_count), key=lambda i: evaluate_member(groups[i], member))
      groups[min_group_index].add(member)
      if verbose:
        print(groups)
    return groups


  def create_balanced_groups(self, group_count: int, verbose: bool = False) -> list[set[str]]:
    groups = self._calculate_balanced_groups(group_count, self.members.copy(), verbose)
    return self.create_groups(groups)
