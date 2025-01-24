import random

for i in range(1, 11):
    rand_num = random.randint(1, 10)
    rand_float = random.random()
    percentage_float = rand_float * 100
    print(f"{round(percentage_float, 2):.2f}%")

# COIN FLIP
coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Heads")
else:
    print("Tails")