import time
import os 
import os.path
import sys
import keyboard
import random
import pickle
"""""
results = list() 
results = pickle.load(open("results.lc", "rb"))
while True:
   n1 = "mom" 

   print(results.index(n1))
   pickle.dump(results, open("results.lc", "wb"))
    
   print(results)
   input("")
   """
n1 = "hi"
n2 = "you"
test = list()
test.append("hiyou")
check = n1+n2
print(check)
input("")
if check in test:
    print("gi")