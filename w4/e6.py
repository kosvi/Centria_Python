#!/usr/bin/python3

def solve_root(eq):
  eq = eq.split("=")
  # t = re.split('\+|-', eq[0])
  t = eq[0].split(" ")
  mon = []
  for n in t:
    f = splitter(n)
    mon.append(f)
  print(mon)
  return tester(mon)

def tester(mon_list):
  a = mon_list[0][0]
  b = mon_list[1][0]
  c = mon_list[2][0]
  d = mon_list[3][0]
  best_y = 10000000
  best_x = -20
  x = -10
  while x < 10:
    current_y = abs(calculate_value(a, b, c, d, x))
    if current_y < best_y:
      best_y = current_y
      best_x = x
    x += 0.0001
  return best_x, best_y

def calculate_value(a, b, c, d, x):
  return a*x**3+b*x**2+c*x+d

def splitter(t):
  t = t.split('x')
  if len(t)==1:
    return int(t[0]), 0
  else:
    if len(t[1])>0 and t[1][0]=='^':
      t[1]=t[1][1:]
    else:
      t[1] = '1'
    return int(t[0]), int(t[1])

# function is obsolete
def cubic_formula(mon_list):
  a = mon_list[0][0]
  b = mon_list[1][0]
  c = mon_list[2][0]
  d = mon_list[3][0]

  # p = -1*b/(3*a)
  # q = p**3 + (b*c-3*a*d)/(6*a**2)
  # r = c/(3*a)

  # x = (q + (q**2 + (r-p**2)**3)**(1/2))**(1/3) + (q - (q**2 + (r-p**2)**3)**(1/2))**(1/3) + p
  # x = -1*b/(3*a) + ((-1*b**3/(27*a**3+b*c/(6*a**2)-d/(2*a))) + ((-1*b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a))**2+(c/(3*a)-b**2/(9*a**2)))**(1/2))**(1/3) + ((-1*b**3/(27*a**3+b*c/(6*a**2)-d/(2*a))) - ((-1*b**3/(27*a**3)+b*c/(6*a**2)-d/(2*a))**2+(c/(3*a)-b**2/(9*a**2)))**(1/2))**(1/3)
  # x = -1*b/(3*a)
  # f = ((3*c/a)-(abs(b)**2/a**2))/3
  # print(f)
  # g = (-1*(2*abs(b)**3/a**2)-(9*b*c/a**2)+(27*a/1))/27
  # print(g)
  # h = (g**2/4)+(f**3/27)
  # print(h) 
  # R = -1*(g/2)+h**(1/2)
  # print(R)
  # S = R**(1/3)
  # print(S)
  # T = -1*(g/2)-h**(1/2)
  # print(T)
  # U = (-1*T)**(1/3)
  # print(U)
  # x = (S+U)-(b/(3*a))

  return 0

eq = "3x^3 -4x^2 +9x +5=0"
best_x, best_y = solve_root(eq)
print(f"closest we got was with x = {best_x} - ",end="")
print(f"3x^3-4x^2+9x+5={format(best_y, '.6f')}")
