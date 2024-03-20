import random
from . import group_system

"""
BalancedGroupSystem.py

This module contains a subclass of GroupSystem that creates balanced groups based on the familiarity matrix.
It creates groups in such a way that members meet as many new members as possible and minimize repeat meetings.

Author: Joshua Si
"""

class BalancedGroupSystem(group_system.GroupSystem):
	familiarityMatrix: list[list[int]] = []

	def __init__(self, members: list[str] = []):
		super().__init__(members)
		self.familiarityMatrix = [[0 for _ in range(len(members))] for _ in range(len(members))]

	def __repr__(self) -> str:
		return f"BalancedGroupSystem({self.members})"
	
	def addMember(self, member: str) -> None:
		super().addMember(member)
		for row in self.familiarityMatrix:
			row.append(0)
		self.familiarityMatrix.append([0 for _ in range(len(self.members))])
	
	def removeMember(self, member: str) -> None:
		index = self.members.index(member)
		super().removeMember(member)
		for row in self.familiarityMatrix:
			row.pop(index)
		self.familiarityMatrix.pop(index)
		
	def createGroups(self, groups: list[list[str]]) -> list[list[str]]:
		super().createGroups(groups)
		for group in groups:
			self.updateFamiliarity(group)
		return groups

	def printFamiliarity(self) -> None:
		print('  ',', '.join(self.members))
		for i, row in enumerate(self.familiarityMatrix):
			print(self.members[i], row)

	def evaluateGroup(self, group: list[str]) -> int:
		score = 0
		for i, j in enumerate(group):
			for k in group[i+1:]:
				score += self.familiarityMatrix[self.members.index(j)][self.members.index(k)]
		return score
	
	def updateFamiliarity(self, group: list[str]) -> None:
		for i in range(len(group)):
			member_i = self.members.index(group[i])	
			for j in group[i+1:]:
				member_j = self.members.index(j)
				self.familiarityMatrix[member_j][member_i] += 1
				self.familiarityMatrix[member_i][member_j] += 1

	def calculateBalancedGroups(self, groupCount: int, members: list[str] = [], verbose: bool = False) -> list[list[str]]:
		random.shuffle(members)
		groups = [[] for _ in range(groupCount)]
		scores = {(): 0}
		# Memoized version of evaluateGroup for evaluating score when adding one member
		def evaluateMember(group, member):
			group_key = tuple(sorted(group))
			new_key = tuple(sorted(group+[member]))
			if new_key in scores:
				return scores[new_key]
			score = scores[group_key]
			for i in group:
				score += self.familiarityMatrix[self.members.index(i)][self.members.index(member)]
			scores[new_key] = score + 1
			return score + 1

		# Balance and distribute members
		for member in members:
			min_group_index = min(range(groupCount), key=lambda i: evaluateMember(groups[i], member))
			groups[min_group_index].append(member)
			if verbose:
				print(groups)
		return groups


	def createBalancedGroups(self, groupCount: int) -> list[list[str]]:
		groups = self.calculateBalancedGroups(groupCount, self.members.copy())
		return self.createGroups(groups)
