import random

choices = ["rock", "paper", "scissors"]

while True:

    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter only Rock, Paper, or Scissors! ❌")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Match Draw! Both chose the same!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break  # Exit the loop