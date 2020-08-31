import random
randomNum = list()


for x in range(0, 10):
    rand = int(random.randint(0, 10))
    randomNum.append(rand)

for x in randomNum:
    print(x)

