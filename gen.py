import random
import string
import random
import pyperclip
N= 8
K = 4
E = 12
number = int(input("How many Synapse X keys would you like to generate?: "))
for x in range(number):
  res = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N))
  res2 = ''.join(random.choices(string.digits, k = K))
  res3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k = K))
  res4 = ''.join(random.choices(string.ascii_lowercase + string.digits, k = K))
  res5 = ''.join(random.choices(string.ascii_lowercase + string.digits, k = E))

  all = res + "-" + res2 + "-" + res3 + "-" + res4 + "-" + res5
  print(all)

