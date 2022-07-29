
# ##Quiz For 15th August


var=0
#Q1.
a=input("who is your 14th prime minister?  ")
if a == "NARENDRA MODI" or a== "narendra modi" or a== "Narendra Modi":
    var+=10
    print("your score is", var)
elif a != "NARENDRA MODI" or a!= "narendra modi" or a!= "Narendra Modi":
    var-=10
    print("your score is",var)
#Q2.
a =input("which month indipendence india? ")
if a == "August" or a== "august" or a== "AUGUST":
    var+=10
    print("Your score is", var)   
elif a != "August" or a!= "august" or a!= "AUGUST":
    var-=10
    print("your score is",var)
#Q3.
a =input("which year india indipendece? ")
if a == "1947" or a== "1947" or a== "1947":
    var+=10
    print("Your score is", var)   
elif a!= "1947" or a!= "1947" or a!= "1947":
    var-=10
    print("your score is",var)
print(a)
#Q4.
a =input("what is national anthem in india ? ")
if a == "Jana Gana Mana" or a== "jana gana mana" or a== "JANA GANA MANA":
    var+=10
    print("Your score is", var)   
elif a!= "Jana Gana Mana" or a!= "jana gana mana" or a!= "JANA GANA MANA":
    var-=10
    print("your score is",var)
#Q5.
a =input("Who is father of nation in India? ")
if a == "MAHATAMA GANDHI" or a== "mahatma gandhi" or a== "Mahatma Gandhi":
    var+=10
    print("Your score is", var)   
elif a!= "MAHATAMA GANDHI" or a!= "mahatma gandhi" or a!= "Mahatma Gandhi":
    var-=10
    print("your score is",var)
#Q6.
a =input("Who is make the national flage in India? ")
if a == "Pingali Venkayya" or a== "pingali venkayya" or a== "PINGALI VENKAYYA":
    var+=10
    print("Your score is", var)   
elif a!= "Pingali Venkayya" or a!= "pingali venkayya" or a!= "PINGALI VENKAYYA":
    var-=10
    print("your score is",var)
#Q7.
a =input("What is the national flower of India? ")
if a == "lotus" or a== "Lotus" or a== "LOTUS":
    var+=10
    print("Your score is", var)   
elif a!= "lotus" or a!= "Lotus" or a!= "LOTUS":
    var-=10
    print("your score is",var)
#Q8.
a =input("What is national currency of India? ")
if a == "rupees" or a== "Rupees" or a== "RUPEES":
    var+=10
    print("Your score is", var)   
elif a!= "rupees" or a!= "Rupees" or a!= "Rupees":
    var-=10
    print("your score is",var)
#Q9.
a =input("What is national calendar of India? ")
if a == "Saka" or a== "SAKA" or a== "saka":
    var+=10
    print("Your score is", var)   
elif a!= "saka" or a!= "SAKA" or a!= "Saka":
    var-=10
    print("your score is",var)
#Q10.
a =input("What is national tree of India? ")
if a == "banyan" or a== "BANYAN" or a== "Banyan":
    var+=10
    print("Your score is", var)   
elif a!= "banyan" or a!= "BANYAN" or a!= "Banyan":
    var-=10
    print("your score is",var)
##output
if var<=10:
    print("Your are weak in genral knowledge.")
elif var<=50:
    print("Your genral knowledge is normal.")
elif var<=70:
    print("Your are good in genral knowledge.")
elif var<=90:
    print("Your are very good in genral knowledge.")
elif var<=100:
    print("Your are owsem in genral knowledge.")
else:
    print("Your are weak in genral knowledge.")


