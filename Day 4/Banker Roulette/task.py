import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# without the method
choice = random.randint(0, 4)
print(f"The One who is going to die is: {friends[choice]}")
# The choice() method allows you to choose a element from the list.
choice2 = random.choice(friends)
print(f"The One who is going to die is: {choice2}")