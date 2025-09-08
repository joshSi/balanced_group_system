import random
from . import group_system

"""
AvailableGroupScheduler.py

This module contains a subclass of GroupScheduler that creates groups based on the
familiarity matrix and takes into account member availability. It creates groups
in such a way that members meet as many new members as possible and minimize
repeat meetings.

Author: Joshua Si
"""

class AvailableGroupScheduler(group_system.GroupSystem):
  def __init__(self, members: list[str] = [], availability_schedules: list[list[bool]] = []):
    super().__init__(members)
    self.familiarity_matrix: dict[frozenset[tuple[str, str]], int] = {frozenset((self.members[i], self.members[j])) : 0 for i in range(len(self.members)) for j in range(i+1, len(self.members))}
    self.participation_count: dict[int] = {member: 0 for member in self.members}
    if len(availability_schedules) == 0:
      self.availability_schedules: list[list[bool]] = [[True for _ in range(len(members))]]
    else:
      self.availability_schedules: list[list[bool]] = availability_schedules

  def add_schedule(self, availability: list[bool]) -> None:
    self.availability_schedules.append(availability)

  def update_participation(self, group: set[str]) -> None:
    for member in group:
      self.participation_count[member] += 1
      for m in group:
        if member != m:
          self.familiarity_matrix[frozenset((member, m))] += 1

  def create_balanced_schedules(self, group_size: int) -> list[set[str]]:
    self.familiarity_matrix: dict[frozenset[tuple[str, str]], int] = {frozenset((self.members[i], self.members[j])) : 0 for i in range(len(self.members)) for j in range(i+1, len(self.members))}
    self.participation_count: dict[int] = {member: 0 for member in self.members}
    schedules = []
    for availability in range(len(self.availability_schedules)):
      candidates = set(member for member, avail in zip(self.members, self.availability_schedules[availability]) if avail)
      # if less candidates than desired group_size, put all possible candidates in the group
      if len(candidates) < group_size:
        schedules.append(candidates)
        continue
      # otherwise filter for those who have participated the least to maximize new members
      min_threshold = min(self.participation_count[member] for member in candidates)
      min_participation_candidates = set(member for member in candidates if self.participation_count[member] == min_threshold)
      if len(min_participation_candidates) > group_size:
        # now select based on familiarity matrix
        group = self.get_balanced_group(min_participation_candidates, set(), group_size)
        schedules.append(group)
        self.update_participation(group)
      else:
        candidates = set(member for member in candidates if member not in min_participation_candidates)
        min_threshold += 1
        new_candidates = set(member for member in candidates if self.participation_count[member] == min_threshold)
        while len(min_participation_candidates) + len(new_candidates) < group_size:
          new_candidates = set(member for member in candidates if self.participation_count[member] == min_threshold)
          min_threshold += 1
          min_participation_candidates = min_participation_candidates | set(member for member in candidates if self.participation_count[member] == min_threshold)
        group = self.get_balanced_group(new_candidates, min_participation_candidates, group_size)
        schedules.append(group)
        self.update_participation(group)
    return schedules

  # returns group of size group_size, consisting of existing members and adding from candidates based on familiarity
  def get_balanced_group(self, candidates: set[str], existing: set[str], group_size: int) -> set[str]:
    group = existing
    scores = {frozenset(group): 0}
    # Memoized version of evaluate_group for evaluating score when adding one member
    def evaluate_member(group: set[str], member: str) -> int:
      group_key = frozenset(group)
      new_key = frozenset(group | {member})
      if new_key in scores:
        return scores[new_key]
      score = scores[group_key]
      for m in group:
        score += self.familiarity_matrix[frozenset((m, member))]
      scores[new_key] = score + 1
      return score + 1

    # Balance and distribute members
    while len(group) < group_size and len(candidates) > 0:
      min_candidate = min(candidates, key=lambda c: evaluate_member(group, c))
      group.add(min_candidate)
      candidates.remove(min_candidate)

    return group
