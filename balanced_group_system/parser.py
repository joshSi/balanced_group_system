import csv

def parse_csv(file_name):
  with open(file_name, 'r') as f:
      reader = csv.reader(f)
      members = [row[0] for row in reader]
  print(members)
  return members
