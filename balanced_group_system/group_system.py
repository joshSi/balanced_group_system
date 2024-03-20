'''
GroupSystem.py

This module contains a class that represents a group system that creates grouplist and stores group history.
'''

class GroupSystem:
	members: list[str] = []
	groupHistory: list[list[list[str]]] = []
	
	def __init__(self, members: list[str] = []):
		self.members = members
	
	def __repr__(self) -> str:
		return f"GroupSystem({self.members})"

	def printHistory(self) -> None:
		for i, grouplist in enumerate(self.groupHistory):
			print(i, ':', grouplist)
	
	def addMember(self, member: str) -> None:
		self.members.append(member)

	def removeMember(self, member: str) -> None:
		index = self.members.index(member)
		self.members.pop(index)

	def createGroups(self, grouplist: list[list[str]]) -> None:
		self.groupHistory.append(grouplist)

	def createAndValidateGroups(self, grouplist: list[list[str]]) -> None:
		memberSet = set(self.members)
		for group in grouplist:
			for member in group:
				try:
					memberSet.remove(member)
				except KeyError:
					if member in self.members:
						raise ValueError("Duplicate members found in grouplist")
					else:
						raise KeyError("Element '{}' was not in members".format(member))
		self.groupHistory.append(grouplist)
