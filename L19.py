import random

users_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors" ]

while True:
    user_input = input("Type rock/paper/sissors or type Q to quit: ").lower()

    if user_input =="q":
        break

    if user_input not in options:
        continue


    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print("computer picked", computer_pick + ".")

    if user_input =="rock" and computer_pick == "scissors":
        print("You win! 🤪")
        users_wins += 1

    elif user_input =="scissors" and computer_pick == "paper":
        print("You win! 🤪")
        users_wins += 1 
    
    elif user_input =="paper" and computer_pick == "rock":
        print("You win! 🤪")
        users_wins += 1 
    
    elif user_input == "scissors" and computer_pick =="scissors":
        print("Same option")
        users_wins +=1
        computer_wins += 1

    elif user_input == "paper" and computer_pick =="paper":
        print("Same option")
        users_wins +=1
        computer_wins += 1

    elif user_input == "rock" and computer_pick =="rock":
        print("Same option")
        users_wins +=1
        computer_wins += 1

    else:
        print("You lost 🥴")
        computer_wins += 1
    
print("You win", users_wins , "times. ")
print("Computer win", computer_wins, "times. " )

input ("Press Enter to exit")
