#!/usr/bin/python3

dictionary = [
('auto', 'a car'), 
('lentokone', 'an airplane'), 
('polkypyörä', 'a bike'), 
('hevonen', 'a horse'), 
('jalka', 'a leg'), 
('kenkä', 's shoe'), 
('linja-auto', 'a bus'), 
('etäkokous', 'a remote meeting')
]

def find_word(s, d):
  results = []
  for p in d:
    if s in p[0] or s in p[1]:
      results.append(p)
  list_dict(results)



def list_dict(d): 
  for pair in d:
    if len(pair[0])<6:
      print(f"{pair[0]} \t\t-\t {pair[1]}")
    else:
      print(f"{pair[0]} \t-\t {pair[1]}")

while True:
  s = input("Find a word (\'list\' to list all words, \'exit\' to quit):\n> ")
  if s=='exit':
    break
  if s=='list':
    list_dict(dictionary)
  find_word(s, dictionary)

