##input
name=input("what is your name ")
hindi=float(input("what is your marks in hindi "))
english=float(input("what is your marks in english "))
sst=float(input("what is your marks in SST "))
sanskrit=float(input("what is your marks in sanskrit "))
science=float(input("what is your marks in scince "))
maths=float(input("what is your marks in maths "))
## count the all subjects number
total=hindi+english+sst+sanskrit+science+maths
##print the marks
print("your hindi marks is",hindi)
print("your english marks is",english)
print("your sst marks is",sst)
print("your sanskrit marks is",sanskrit)
print("your science marks is",science)
print("your maths marks is",maths)
## convert to persent
persent=total/600*100
print("your total persent is",persent)
## calculation
if persent>=90.0:
    print(name,"your grade is (A+).")
elif persent>=75.0:
    print(name,"your grade is (A).")
elif persent >=60.0:
    print(name,"your grade is (B+).")
elif persent >=50.0:
    print(name,"your grade is (B).")
elif persent >=40.0:
    print(name,"your grade is (C+).")
elif persent >=33.0:
    print(name,"your grade is (C).")
else:
    print(name,"you are fail.")
#hindi
if hindi <=32.0:
    print(name,"you are fail in hindi subject because your marks is",hindi)
#maths
if maths <=32.0:
    print(name,"you are fail in maths subject because your marks is",maths)
#english
if english <=32.0:
    print(name,"you are fail in english subject because your marks is",english)
#sanskrit
if sanskrit <=32.0:
    print(name,"you are fail in sanskrit subject because your marks is",sanskrit)
#sst
if sst <=32.0:
    print(name,"you are fail in SST subject because your marks is",sst)
#scince
if science <=32.0:
    print(name,"you are fail in scince subject because your marks is",science)


