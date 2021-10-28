#!/usr/bin/python3

import rooms

def main():
  print("")
  room_list = []
  room_list.append(rooms.Kitchen(30, 2010))
  room_list.append(rooms.Bedroom(20, 3))
  room_list.append(rooms.LivingRoom(30, "south"))
  for r in room_list:
    print(r.get_info())
  print("\nupdate sizes\n")
  room_list[0].size=25
  room_list[1].size=-15
  room_list[2].size=200
  for r in room_list:
    print(r.get_info())
  print("")

if __name__ == "__main__":
  main()

