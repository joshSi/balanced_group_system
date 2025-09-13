from balanced_group_system import BalancedGroupSystem
import csv

if __name__ == '__main__':
  with open('participants.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip header
    members = [row[0] for row in reader]

  N = 20

  for i in range(1, N):
    group_system = BalancedGroupSystem(members)
    groups = group_system.create_balanced_groups(N)
    print(f"N = {i}:")
    for j, g in enumerate(groups):
      print(f" Group {j+1}: {g}")
    for g in groups:
      assert abs(len(g) - len(members)//N) <= 1
