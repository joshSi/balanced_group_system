'''
GroupSystem.py

This module contains a class that represents a group system that creates groups and stores group history.
'''

class GroupSystem:
	members: list[str] = []
	groupHistory: list[list[list[str]]] = []
	
	def __init__(self, members: list[str] = []):
		self.members = members
	
	def __repr__(self) -> str:
		return f"GroupSystem({self.members})"

	def printHistory(self) -> None:
		for i, groups in enumerate(self.groupHistory):
			print(i, ':', groups)
	
	def addMember(self, member: str) -> None:
		self.members.append(member)

	def removeMember(self, member: str) -> None:
		index = self.members.index(member)
		self.members.pop(index)

	def createGroups(self, groups: list[list[str]]) -> None:
		self.groupHistory.append(groups)
