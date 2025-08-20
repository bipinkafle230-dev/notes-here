import random

cpu_number = random.randint(1, 100)
user_number = int(input("Enter your guess (1-100): "))

print(f"CPU chose: {cpu_number}")
print(f"You chose: {user_number}")

if user_number == cpu_number:
    print("Congratulations! You guessed the exact number.")
elif user_number < cpu_number:
    print("Your guess is too low.")
elif user_number > cpu_number:
    print("You won .")
else:
    print("Invalid input. Please enter a number between 1 and 100.")

# # End of game/main.py

