# Input for What day i am going to visit? 
go=int(input("What day am I going to visit? If day-1 is sunday and day-2 is monday so, please write the day on number "))
# I will go on--
if go==1:
    print("I will go to the visit on sunday")
elif go==2:
    print("I will go to the visit on monday")
elif go==3:
    print("I will go to the visit on tuesday")
elif go==4:
    print("I will go to the visit on wednesday")
elif go==5:
    print("I will go to the visit on thursday")
elif go ==6:
    print("I will go to the visit on friday")
elif go==7:
    print("I will go to the visit on saturday")
# Input for After how many days will I come back?
come=int(input("After how many days will I come back? "))
# Calculate
total=int(go+come)%7
if go==0:
  (total+1)
# I will come on--
if total==1:
    print("I will come sunday")
elif total==2:
    print("I will come monday")
elif total==3:
    print("I will come tuesday")
elif total==4:
    print("I will come wednesday")
elif total==5:
    print("I will come thursday")
elif total ==6:
    print("I will come friday")
elif total==7:
    print("I will come saturday")
else:
    print("Error")






