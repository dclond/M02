"""
David Clond
SDEV 220 M02
clond_m02_programming_assignment.py


This application solves the problems for the following 4.1, 4.2, 6.1, 6.2, and 6.3
"""

# 4.1
secret = 4
guess = 9

while secret != guess:
    if guess < secret:
        print("Too low")
        guess += 1
    elif guess > secret:
        print("Too high")
        guess -= 1
else:
    print("just right")

# 4.2
small = True
green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermellon")
    else:
        print("pumpkin")

# 6.1
for element in [3,2,1,0]:
    print(element)

# 6.2
guess_me = 7
number = 1


while True:
    if number < guess_me:
        print("Too low")
    elif number > guess_me:
        print("oops")
        break
    else:
        print("found it!")
        break
    number += 1
    
# 6.3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
