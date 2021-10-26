#!/usr/bin/python3

import re

class Complex:

  def __init__(self, a=0, b=0):
    self.a = a
    self.b = b

  def set_a(self, a):
    self.a = a

  def set_b(self, b):
    self.b = b

  def set_ab(self, a, b):
    self.a = a
    self.b = b

  def set_abi(self, abi):
    multi_a = 1
    if abi[0]=="-":
      multi_a = -1
      abi = abi[1:]
    multi_b = 1
    if "-" in abi:
      multi_b = -1
    abi = re.split("\+|-", abi)
    if len(abi)==2:
      try:
        self.a = float(abi[0]) * multi_a
      except:
        self.a = 0
      try:
        self.b = float(abi[1][:-1]) * multi_b
      except:
        self.b = 1

  def get_a(self):
    return "{}".format(self.a)

  def get_bi(self):
    return "{}i".format(self.b)

  def get_ab(self):
    sign = "+"
    if self.b<0:
      sign = "-"
    b = abs(self.b)
    if b==1:
      b = ""
    abi = "{}{}{}i".format(self.a, sign, b)
    if b==0 and type(b)==float:
      abi = abi[:-5]
    elif b==0:
      abi = abi[:-3]
    return abi

c = Complex()
print(c.get_ab())
c.set_abi("-4-2.3i")
print(c.get_ab())
c.set_abi("4.9-2i")
print(c.get_ab())
c.set_abi("-1+i")
print(c.get_ab())
c.set_abi("3+0i")
print(c.get_ab())
