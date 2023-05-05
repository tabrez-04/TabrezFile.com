print("Welcome to this game ! 😀")

play = input("Do you want to play this game? : ")

if play.lower() !="yes":
    quit()

print("let's play 🙃")
score = 0

answer = input("what is the capital of Tajikistan? ")
if answer.lower() == "dushanbe":
    print("Answer is correct")
else:
    print("Wrong answer 😒")
    score += 1

answer = input("What is the population of Tajikistan? ")
if answer == "11M":
    print("Answer is correct")
else:
    print("Wrong answer 😒")
    score += 1

answer = input("Is tajikistan a beautiful country? ")
if answer.lower() == "yes":
    print("Answer is correct")
else:
    print("Wrong answer 😒")
    score += 1

answer = input("How many regions there are in Tajikistan? ")
if answer == "4":
    print("Good job !😉")
    score+= 1
else:
    print("Oops, something went wrong!")

answer = input("When we celebrate Independence day in Tajikistan? ")
if answer.lower() == "9th september":
    print("Well done !")
    score+= 1
else:
    print("Maybe next time 🤔")

answer = input("Area of Tajikistan? ")
if answer == "142,1":
    print("Excelent 👏")
    score+= 1
else:
    print(" Incorrect 🤔")

answer = input("What is the translate of Dushanbe in English ? ")
if answer.lower() == "monday":
    print("Excelent 👏")
    score+= 1
else:
    print(" Try later 🤔")

answer = input("... % of Tajikistan are mountinous? ")
if answer == "93":
    print("Great 👏")
    score+= 1
else:
    print(" Wrong answer 🤔")

answer = input("The most popular holiday in Tajikistan? ")
if answer.lower() == "navruz":
    print("Great 👏")
    score+= 1
else:
    print(" Oops, wrong answer 🥴")

answer = input("Tajikistan located in... ? ")
if answer.lower() == "central asia":
    print("Great 👏")
    score+= 1
else:
    print(" Wrong answer 🤔")

print("Your score is " + str(score) + " correct answers. ")
print("Your percentage is " + str((score /10)*100))

input("Press Enter to exit")