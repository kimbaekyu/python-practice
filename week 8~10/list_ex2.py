import random

numbers=[]
for num in range(0,10):
    numbers.append(random.randrange(0,10))

print("Created list",numbers)

for num in range(0,10):
    if num not in numbers:
                   print("%d is not in list"%num)
