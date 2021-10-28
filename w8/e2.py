#!/usr/bin/python3

class Group:

  def __init__(self, name = ""):
    self.name = name
    self.members = []

  def add_member(self, member):
    self.members.append(member)

class Member:

  def __init__(self, name="", role=""):
    self.name = name
    self.role = role

  def get_info(self):
    return f"{self.name} ({self.role})"

def main():
  g = Group()
  g.name = "My Group"
  g.add_member(Member("Anna", "Boss"))
  g.add_member(Member("Mike", "Secretary"))
  g.add_member(Member("Jane", "Worker"))
  print(f"Group name: {g.name}")
  print("It's members are: ")
  for m in g.members:
    print(m.get_info())

if __name__ == "__main__":
  main()
