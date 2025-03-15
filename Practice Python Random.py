
import random

print(random.randint(1, 20))
print(random.random())

answer = random.randint(1, 3)

if answer == 1:
    print("yes")
elif answer == 2:
    print("no")
elif answer == 3:
    print("maybe")
else:
    print("I don't know")