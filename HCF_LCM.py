###HCF
num1=int(input("Please input the first value. :- "))
num2=int(input("Please input the secend value. :- "))
HCF=1
for i in range(2,num1+1):
    if num1%i==0 and num2%i==0:
        HCF=i
print("The numbers HCF is",HCF)

###LCM
LCM=(num1*num2)//HCF
print("The numbers LCM is",LCM)















