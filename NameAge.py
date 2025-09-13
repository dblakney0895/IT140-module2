# NameAge.py
# Prompts the user for their name and age, then calculates their birth year.

from datetime import date

# Ask for user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# Calculate birth year
current_year = date.today().year
birth_year = current_year - age

# Display output
print(f"Hello {name}! You were born in {birth_year}.")
