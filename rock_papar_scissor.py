

#Game (rock, papar, scissors)
import random
from secrets import choice

def try_again():
    r=["rock","papar","scissors"]
    ran=random.choice(r)
    rps=(input("what you need rock, papar, scissors" ))
    print("it's your choice",rps) 
    print("it's computer choice",ran)
    ##papar
    if ran=="papar":
        if rps == "papar":
            print("Tie! Game")
        elif rps == "scissors":
            print("You Win! Game")
        elif rps == "rock":
            print("Computer Win!")
        else:
            print("Wrong Word")
    ##rock
    if ran=="rock":
        if rps == "papar":
            print("You Win! Game")
        elif rps == "scissors":
            print("Computer Win! Game")
        elif rps == "rock":
            print("Tie! Game")
        else:
            print("Wrong Word")
    ##scissors
    if ran=="scissors":
        if rps == "papar":
            print("Computer Win! Game")
        elif rps == "scissors":
            print("Tie! Game")
        elif rps == "rock":
            print("You Win! Game")
        else:
            print("Wrong Word")


    que= input("You continue the Game yes/no")
    if que =="yes" or que =="Yes" or que =="YES":
        try_again()
    elif que=="no" or que=="No" or que=="NO":
        print("ok Bye.")
try_again()
