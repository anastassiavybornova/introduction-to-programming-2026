# this program is a mental math trainer for multiplication.
# it randomly picks two numbers (between 0 and 50, both included) 
# and asks the user to provide their product.
# if the answer was right, the user gets a new question.
# if the answer was wrong, the user gets the same question again.
# the program also displays the time it takes for the user to compute.

# import libraries
import random

# print first welcome message to user
print("Welcome to mental math multiplication training!")
print("To end the game, type END at any time. Let's go!")

# first "eternal" while loop - will end if user types END
while True:

    # select two random numbers between 0 and 50
    x = random.choice((0,51))
    y = random.choice((0,51))

    # check the clock when user starts guessing
    time_before = time.time()

    # second "eternal" whie loop - will end if user types "END"
    while True:

        # ask the user for a guess
        user_answer = input("What is {x} times {y}? ")

        # account for the option of the user typing "END" to end the game
        if user_answer = "END":
            print("Ok, ending the game!")

        # compute the correct answer
        correct_answer = x**y

        if user_answer == correct_answer:
            time_after = time.time()
            time_elapsed = int(time_before - time_after)
            print(f"Correct! It took you {time_after} seconds to answer.")
            break
        else:
            print("That's wrong, try again!")

    # breaking out of the first (outer) while loop: 
    # the lines of code below will only be executed we break out
    # of the second (inner) while loop
    if user_answer == "END":
        break