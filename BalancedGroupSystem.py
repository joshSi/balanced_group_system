import random
import GroupSystem

"""
BalancedGroupSystem.py

This module contains a subclass of GroupSystem that creates balanced groups based on the familiarity matrix.
It creates groups in such a way that members meet as many new members as possible and minimize repeat meetings.

Author: Joshua Si
"""

class BalancedGroupSystem(GroupSystem.GroupSystem):
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
		
	def createGroups(self, groups: list[list[str]]) -> None:
		super().createGroups(groups)
		for group in groups:
			for i in group:
				for j in group:
					if i != j:
						self.familiarityMatrix[self.members.index(j)][self.members.index(i)] += 1

	def printMatrix(self) -> None:
		for row in self.familiarityMatrix:
			print(row)

	def evaluateGroup(self, group: list[str]) -> int:
		score = 0
		for i in group:
			for j in group:
				if i != j:
					self.familiarityMatrix[self.members.index(j)][self.members.index(i)] += 1
					score += self.familiarityMatrix[self.members.index(j)][self.members.index(i)]
		return score

	def calculateBalancedGroups(self, groupCount: int, verbose: bool = False) -> list[list[str]]:
		members = self.members.copy()
		random.shuffle(members)
		groups = [[] for _ in range(groupCount)]
		while members:
			i = members.pop(0)
			groups[min(enumerate(groups), key=lambda x: self.evaluateGroup(x[1]+[i]))[0]].append(i)
			if verbose: print(groups)
		return groups

	def makeBalancedGroups(self, groupCount: int) -> None:
		groups = self.calculateBalancedGroups(groupCount)
		self.createGroups(groups)
