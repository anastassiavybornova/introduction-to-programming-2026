# import libraries
import random
from datetime import date

# list of random predictions about studies
prediction_studies = [
    "there will be a slide show",
    "there will be a fire alarm",
    "..."
]

# list of random predictions about private life
prediction_private = [
    "you will remember your best friend's birthday last minute",
    "you will get a call from a family member who likes to talk",
    "..."
]

# list of random predictions about the day
prediction_day = [
    "a random stranger will smile at you",
    "a squirrel will sit on your shoulder",
    "..."
]

bday = input("What is your birthday? ")

print(f"Your birthday is {bday}; and today is {date.today()}; that means {random.choice(prediction_studies)} during class today, and later, {random.choice(prediction_private)}...")