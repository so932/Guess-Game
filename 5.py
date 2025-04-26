import random

num = random.randint(1, 10)
guess = ""
count = 0
limit = 3
out = False
try:
      while guess != num and not out:
       if count < limit:
        guess = int(input("enter your guess: "))

        count += 1
        if guess < num:
           print("the number is bigger")
        elif guess > num:
           print("the number is smaller")   
       else:
        out = True

except ValueError:
   print("please enter numbers only")


if out:
    print("you lose")
else:
    print("you win")               
