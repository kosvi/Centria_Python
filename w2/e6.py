#!/usr/bin/python3

seconds = int(input("Give the amount of seconds: "))

hours = int(seconds/(60*60))
minutes = int(seconds/60 - hours*60)
seconds = seconds - hours*60*60 - minutes*60

print(f"it is {hours} h {minutes} min {seconds} s")
