# -*- coding: utf-8 -*-
"""Project on snake gun water game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1auKtrKFHPxlFLz56jfrHpFaS5YegDT91
"""

import random

def game(comp, you):
  if(comp == you):
     return None
  elif(comp == 's'):
    if(you == 'w'):
      return False
    elif(you == 'g'):
      return True
  elif(comp == 'w'):
    if(you == 's'):
      return True
    elif(you == 'g'):
      return False
  elif(comp == 'g'):
    if(you == 's'):
      return False
    elif(you == 'w'):
      return True


print("Choice by the Computer");
randm = random.randint(1, 3);
if(randm==1):
    comp = 's'
elif(randm==2):
    comp = 'w'
else:
    comp = 'g'

you = input("Choose Your Value: Snake(s), Water(w), Gun(g) ")

a = game(comp, you);

print(f"Computer Choose: {comp}")
print(f"You Choose: {you}")

if(a==None):
  print("Tie!!!")
elif(a):
  print("You Win!!!")
else:
  print("You Loose!!!")