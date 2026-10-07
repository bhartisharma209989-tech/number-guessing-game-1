import random

secret = random.randint(1, 50)
lives = 5

print("Guess the number between 1 and 50")

while lives > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("You guessed it!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    lives -= 1
    print("Lives left:", lives)

if lives == 0:
    print("Game over!")
    print("The number was:", secret)