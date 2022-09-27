##first code
value=str (input("Input the value "))
a=[]
a2=0
for i in value:
    a.append(i)

for j in a:
    a2=a2+int(j)
print(a2)














#secend code

value=int(input("Please input your value. :- "))
total=0
while value!=0:
    count=value%10
    total=total+count
    value=value//10
print(total)



















# ##third code
first_digit=0
secend_digit=1
while first_digit<=63245986:
    total=first_digit+secend_digit
    first_digit=secend_digit
    secend_digit=total
    print(total)
