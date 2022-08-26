go=int(input("Please your visiting time? "))
come=int(input("After how many hour will you come back? "))
total=(go+come)%12
print("I will come on", total," clock")
