import random
import os
import time
num = 0
rand = random.randint(1,101)

while(num != 1):
 answer = int(input("Guess The Number Beetween 1 to 100: "))
 if(answer == rand):
  print("You Won!")
  time.sleep(1)
  num = 1
 elif(answer > rand):
  print("Too High!")
 elif(answer < rand):
  print("Too Low!")
 else:
  print("Invalid Input!")
  num = 1
os.system('cls')
print("\033[32mCongrats You Won The Game!\033[0m")