import random

x = random.randint(9, 10)
y = random.random()

rockPaperScissors = ["Rock", "Paper", "Scissors"]
z = random.choice(rockPaperScissors)
newCode = "-------------------------------------------"
print(z)
print(newCode)

suite = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(suite)
print(suite)
print(newCode)