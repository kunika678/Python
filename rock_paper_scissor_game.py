import random
print("********************")
print("         Game       ")
print("********************")

while True:
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Choose rock, paper, or scissors: ")
    print(f"The computer chose {computer_choice}.")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
    else:
        print("The computer wins!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != 'y':
        print("Thanks for playing !")
        break
