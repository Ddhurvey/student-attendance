

##  Guess the number
import numbers
import random 
import math
def try_again():

    lover_value=int(input("input the Small value "))
    upper_value=int(input("input the Big value "))
    a=random.randint(lover_value,upper_value)

    d=math.log(upper_value-lover_value+1,2)
    print(int(d),"chanse you have collected")
    s=1

    while s<d:
        print("lover value is",lover_value)
        print("upper value is",upper_value)
        f=int(input("guess and Enter the number "))
        s=s+1
        if f>a:
            print("the number is biger than guess number")
        if f<a:
            print("the number is smaller than guess number")
        if f==a:
            print("Congratulation You Win!")
        else:
            print("Try Again")
            
    print("the correct number is ",a)

    que= input("You continue the Game yes/no " )
    if que =="yes" or que =="Yes" or que =="YES":
        try_again()
    elif que=="no" or que=="No" or que=="NO":
        print("ok Bye. Thankyou for play this game.")
try_again()

