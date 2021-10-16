#!/usr/bin/python3

def choose_operation(op, balance):
  if op==1:
    balance = make_deposit(balance)
  elif op==2:
    balance = make_withdraw(balance)
  elif op==3:
    print_balance(balance)
  return balance

def make_deposit(balance):
  try:
    dep = float(input("Deposit money: "))
    if dep>0:
      balance += dep
    else:
      print("incorrect value")
  except:
    print("incorrect value")
  return balance

def make_withdraw(balance):
  try:
    draw = float(input("Withdraw money: "))
    if draw>0:
      balance -= draw
    else:
      print("incorrect value")
  except:
    print("incorrect value")
  return balance

def print_balance(balance):
  print(f"account balance is: {balance}")

balance = 0

while True:
  print("Your bank account")
  print("Choose operation:")
  print("1) deposit money")
  print("2) withdraw money")
  print("3) check balance")
  print("4) exit")
  op = 0
  try:
    op = int(input("> "))
  except:
    print("incorrect value")
  if op>0 and op <4:
    balance = choose_operation(op, balance)
  elif op==4:
    break
