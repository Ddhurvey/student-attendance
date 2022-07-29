######### DAY ==???
# day=input("enter the day ")
# time=input("enter the time ")
# if day=="monday":
#     print("panir")
# elif day == "tuesday":
#     print("rajma")
# elif day == "wednesday":
#     print("fish")
# elif day=="thursday":
#     print("aalu bri")
# elif day=="friday":
#     print("egg")
# elif day=="saturday":
#     print("kheer")
# else:
#     print("chikan biryani")






























# dk_list=['a','b','c','d','e','f','g']
# ####join
# print("**".join(dk_list))
# ###append
# dk_list.append('h')
# print(dk_list)
# ###list ko idex mein add karna
# dk_list[0:2]=("devendradhur85@gmail.com")
# print(dk_list)






# ###########avrage in string??
# a="15+20+2.5+3+3.4+4+65+97+9+6"+"9"
# d=a.split("+")
# print(d)
# dd=0
# for var in d :
#     dd=dd+float(var)
# print(dd)
# print(len(d))
# avg=(dd/len(d))
# print(avg)
# print(avg,"is your avrage")
# print(type(avg))





























# ### IN AND NOT IN OPRATORS             IT IS BOOLEAN TYPE
# print('d' in 'devendra')
# print("d" not in "ground")



# #####IN AND NOT IN OPRATORS 2
# dlist=['a','b','c','d']
# print('d','a','g' in (dlist))


# ##int
# a=1,2,3,4,5
# print(1,3,4,2,1 in a)

































# ## if else:


# per_rain=[94.3,45,100,78,16,5.3,79,86]
# resp=[]
# for v in per_rain:
#    if v >90:
#        resp.append("bring an umbrella")
#    elif v > 80:
#        resp.append("good for the flowers")
#    elif v > 50:
#        resp.append("whatch out for clouds")
#    else:
#         resp.append("nice day")
# print(resp)


































# #### num mein list
# num=(list(range(0,68)))
# print(num)



























# fruit="Apple Banana Mango Orange"
# v=0
# for chr in fruit:
#     if chr != " " :
#        v=v+1
# print(v)























# fruit="apple banana mango orange"
# v=0
# for chr in fruit:
#     if chr == "a":
#        v=v+1
#     elif chr == "e":
#        v=v+1
#     elif chr == "i":
#        v=v+1
#     elif chr == "o":
#        v=v+1
#     elif chr == "u":
#        v=v+1
# print(v,"  itne vovel hain fruit mein .")



























# fruit="apple banana mango orange"
# x=0
# for chr in fruit:
#     if chr in ['a','e','i','o','u']:
#         x=x+1
# print(x)
































# str1="today you are you! that is truer than true there is no one "
# if "true" in str1:
#     print("True! you are you!")
# elif "false" in str1:
#     print("False. you aren't you?")
# else:
#     print("Neither true nor False!")



































# num=[5,11,9,22,2,25,3,30]
# large_num=0
# for big in num:
#     if big>=large_num:
#         large_num=big
# print(large_num)















































# words=["adopt","bake","beam","confide","grill","plant","time","wish"]
# past_tense=[]
# for var in words:
#     if "e" in var[-1] :
#         past_tense.append(var+'d')      
#     else:
#         past_tense.append(var+'ed')
# print(past_tense)




































# ### MUTABLE AND IMUTABLE
# alist=['a','b','c','d']
# alist[1]='d'
# print(alist)
# alist[1:2]='f','e','k','m'
# print(alist)
# alist[1:4]=[]
# print(alist)


# ## MUTABLE AND IMUTABLE in string(type error)

# alist="a,b,c,d"
# alist[1]='d'
# print(alist)












# ## MUTABLE AND IMUTABLE in string

# str1="hello world"
# str1='j'+ str1[1:]
# print(str1)

# str2=str1[0]+"jk"+str1[3:]
# print(str2)




















# ####DEL()
# a=[1,2,3,4,5,6,7,8,9,0]
# del a[3]
# print(a)
# del a[0:3]
# print(a)














######### ID
# a="banana"
# b="apple"
# print(a is b)
# print(id(a))
# print(id(b))












# #########2222222222222
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# print(id(a))
# print(id(b))








# #########33
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# a=b
# print(a is b)
# print(id(a))
# print(id(b))























# ########44444444
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# a=b
# b[0]=4
# print(a)

















# # var_time=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
# time=int(input("How much time is it now?"))
# alarm=int(input("After how many hours do you want the alarm to sound?"))
# # if time<12 :
# #   sum  =  time+alarm
# #   print(sum)
# # else:
# #     time>12
# #     Su_m=time+alarm
# #     sum1 = Su_m % 12
# #     print(sum1)
# total =(time+alarm)%24
# print("time on clock", total)
    

























    
# from turtle import *
# import turtle
# color('red', 'yellow')
# turtle.speed(0)
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# turtle.exitonclick()



























############ WHAT DAY I AM GO ??
# go=int(input("What day am I going to visit?"))
# come=int(input("After how many days will I come back?"))
# total=(go+come)%7
# print("I will come", total)































# a="71,72,73.5,45.9, 45,48"
# b=a.split(",")
# print(b)
# g=0
# for num in b:
#       g=g+float(num)
# print(g)
# print(len(b))
# print(g/len(b))




























# from inspect import stack
# from opcode import stack_effect
# from operator import index
# from stringprep import in_table_a1, in_table_d1
# from xml.dom import INDEX_SIZE_ERR


# d= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# st="Riverside Natural School"
# #list
# print(d)
# #len
# print(len(d))
# #(::::::)
# print(d[0:4])
# #split
# j=st.split("e")
# print(j)
# #join
# print(("d").join(st))
# #count
# print((st.count)("e"))

# #count2
# g=0
# for va in d:
#     g=g+va
# print(g) 

# #index
# #for loop in string
# for ch in st[0:7]:
#     print(ch)
# ##_________
# for de in st:
#     print(de)





























































# for de in a:
#     print(de)
# avg=(a)
# print(avg)

# avg=0

# for va in int(a):
#     avg=int(avg)+int(va)
# print(avg) 





# avg=int(a)
# print(a)




# for de in [a]:
#     print(de)
# print(a)


# g=0
# for va in int (a):
#     print(g)
#     A=int(g)+int(va)
# print(g)



















































import turtle
# wn=turtle.Screen()
# wn.bgcolor("white")
# a=turtle.Turtle()
# a.color("green","gold")
# a.shape("circle")
# a.speed(10000)
# a.begin_fill()
# turtle.speed(0)
# for _ in range(60):
#     a.begin_fill()
#     a.fd(98)
#     a.lt(601)
#     a.fd(221)
#     a.bk(131)
#     a.rt(9)
#     a.end_fill()
# a.end_fill()
# a.hideturtle()
# turtle.exitonclick()























# # Example to find avearge of list
# from numpy import mean
# number_list = [45, 34, 10, 36, 12, 6, 80]
# avg = mean(number_list)
# print("The average is ", round(avg,2))









# # Example to find the average of the list
# from statistics import mean
 
# number_list = [45, 34, 10, 36, 12, 6, 80]
# avg = mean(number_list)
# print("The average is ", round(avg,2))









# # Example to find average of list
# number_list = [45, 34, 10, 36, 12, 6, 80]
# avg = sum(number_list)/len(number_list)
# print("The average is ", round(avg,2))













# def cal_average(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t           

#     avg = sum_num / len(num)
#     return avg

# print("The average is", cal_average([18,25,3,41,5]))


















































# #वृत्त की त्रिज्या, r = √(क्षेत्रफल / π)
# area=int(input("area"))
# radios=( (area/ (22/7))**(1/2))
# print(radios)

# #वृत्त का त्रिज्या ज्ञात करें जब परिधि दी गयी हो |
# #C = 2 π r
# #r=C/2π
# circumference=int(input("circumference"))
# radios2=(circumference/(2*22/7))
# print(radios2)


# #वृत्त का व्यास ज्ञात करें जब परिधि दी गयी हो |





































# day=input("din enter karo")
# time=input("time btao")
# if day == "monday":
#     if time == "breakfast":
#       print ("daliya")
#     elif time == "lunch":
#       print("pulao") 
#     else:
#       print ("dal chawal")
# if day == "tuesday":
#     if time == "breakfast":
#       print("pej")
#     elif time == "lunch": 
#       print("dal chawal") 
#     else:
#       print ("dal chawal egg")
# if day == "wednesday":
#     if time == "breakfast":
#       print("chila roti")
#     elif time == "lunch":
#       print("dam biryani")
#     else:
#       print ("fish")
# if day == "thursday":
#     if time == "breakfast":
#       print("paratha ke sath chatni")
#     elif time == "lunch":
#       print("chole bhature")
#     else:
#       print ("palak paneer")
# if day == "friday":
#     if time == "breakfast":
#       print("banana,apple") 
#     elif time == "lunch":
#       print("methi sabji chawal") 
#     else:
#       print ("dal chawal")
# if day == "saturday":
#     if time == "breakfast":
#       print("paratha")
#     elif time == "lunch": 
#       print("paneer") 
#     else:
#       print ("egg")
# else:
#     if time == "breakfast":
#       print("aalu ka paratha")
#     elif time == "lunch":
#       print("anda kari") 
#     else:
#       print ("chicken biryani")




































# #LIST OF STRINGS
# friends_list=["Amit","Sumit","Arvind","yogesh","Sameer"]
# print(friends_list)
# print(type(friends_list))

# #LIST OF INTEGERS
# no_list=[12,34,56,68,35,56]
# print(no_list)
# print(type(no_list))

# #LIST OF FLOATS
# float_list=[12.3,33.4,43.4,35.7,67.4]
# print(float_list)
# print(type(float_list))




























# dic= {
#  'Name': 'Devendra', 
#  'Age': 15,
#  }
# dic['ORGANIZATION'] = "Marida"
# dic['mobile no.'] = 1234567890
# dic['place'] = 'Mohgaon'
# dic['state'] = 'Madhya Pradesh'
# dic['city'] = 'Mandla'
# print(dic)

# #copy dict
# friends ={
#  "arvind":  "6th",
#  "amit":  "7th",
#  "suraj":  "8th",
#  "devendra":"9th",
#  "pradeep":"10th"
#   }
# myfriends=friends.copy()
# print(myfriends)


# # name
# mrida = { 1: 'ram',
# 	        2 : 'sanjay',
# 	        3: 'ganesh',
# 	        4: 'amit',
# 	        5: 'devendra',
# 	        6 : 'suraj',}
	 
# for name  in mrida :
# 	 print(name)
# mrida = { 1: 'ram',
# 	        2 : 'sanjay',
# 	        3: 'ganesh',
# 	        4: 'amit',
# 	        5: 'devendra',
# 	        6 : 'suraj',}
	 
# for name  in mrida :
# 	 print(mrida[name])











































# student=dict(name="amit",classes =9,city="mandla")
# print(student)

# #update
# person= {'1': 'RAM', '2': 17,}
# person['2'] =89 
# print(person)
# #1
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x=thisdict.keys()

# print(x)






















#dict 1
# from unicodedata import name


# dict={
#     "amit":25,
#     "arvind":20,
#     "sumit":8
# }
# print(dict)
# print(type(dict))
# print(dict["amit"])
# print(dict["arvind"])
# print(dict["sumit"])

# #dict2
# student=dict(name="amit",classes =9,city="mandla")
# print(student)



















































# #2nd function
# def food(* flavours):
#  for flavour in  flavours:
#   print("i like" , flavour)
# food("orange", "banana","apple",)


# def calculate(a,b,c):
#  print(a*8)
#  print(b*6)
#  print(c*4)
# calculate(8,2,5)

# # language
# def say_hello_language(name, language):
#  if language == "hindi":
#   print("Namaste ", name)
#   print("Aap kaise ho?")
#  elif language == "punjabi":
#   print("Sat sri akaal ", name)
#   print("Tuhada ki haal hai?")
#  else:
#    print("Hello ", name)
#    print("How are you?")
# say_hello_language("Rishi", "punjabi")
# say_hello_language("maan", "english")
# say_hello_language("Abhi", "french")
# say_hello_language("kavay", "hindi")


























#multipuly
# def  calculate(d):
#  print(d*5)
# calculate(5)
# #plus
# def calculate(e):
#  print(e+5)
# calculate(5)
# #minus
# def calculate(v): 
#  print(v-6)
# calculate(10)
# #division
# def calculate(n):
#  print(18%n)
# calculate(5)















































# var_time=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
# time=int(input("How much time is it now?"))
# alarm=int(input("After how many hours do you want the alarm to sound?"))
# if time<12 :
#   sum  =  time+alarm
#   print(sum)
# else:
#     time>12
#     Su_m=time+alarm
#     sum1 = Su_m % 12
#     print(sum1)
    


























# # isme sirf ### wale anko ko 10 -10 plus karna hai or 10-10 minus karna hai.


# import turtle
# s=turtle.Turtle()
# windo= turtle.Screen()
# s.speed(0)
# s.color("white","white")
# s.shape("turtle")
# s.pensize(5)
# colors=['skyblue','gold','pink','orange','yellow','green','red','blue','white','black']
# s.goto(0,0)
# for _ in range(100000):

#     s.pencolor(colors[_%9])
#     s.fd(_)
#     s.lt(90)
#     s.bk(90)
#     s.lt(32)
#     s.fd(79)
#     s.rt(62)
# windo.exitonclick() 



































































# d= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# st="Riverside Natural School"
# ###list
# print(d)
# ###len
# print(len(d))
# ###(::::::)
# print(d[0:4])
# ###split
# j=st.split("a")
# print(j)
# ###join
# print((",").join(st))
# ##count
# print((st.count)("e"))
# ### INDEX 
# print(d.index(5))
# ###split2
# print(st.split("e"))




























# print(type("True"))
# print(type(True))






# if 100 % 2==0:
#     print("is even")
# else: print("is odd")

















# if 100== 2==0:
#     print("is even")
# else: print("is odd")












# if 100 >= 2==0:
#     print("is even")
# else: print("is odd")











# if 100 <= 2==0:
#     print("is even")
# else: print("is odd")












# if 100 != 2==0:
#     print("is even")
# else: print("is odd")


















# if 100 <= 2==0:
#     print("is even")
# else: print("is odd")




















































###### LIST


# d=["amit",12,13.4,["a,b"],"ar,br,cr","45"]
# print(len(d))
# print(d[3])
# print(d[-4])
# print(d[1:5])
# b=(len(d)//2)
# print(d[b])







# a="Riverside Natural School"
# print(a.count("a"))
# print(a.index)
# print([ "hello"]+["world"])















# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# b=0
# for var in a:
#     print(var)
#     b=b+var
#     b=b+1
# print(b)


















# t= (list(range(0,41)))
# print(t)
# g=0
# for vari in t:
   
#     g=g+vari

# print(g)


























# ### It is most IMP 

# d= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# st="Riverside Natural School"
# # #list
# print(d)
# # #len
# print(len(d))
# # #(::::::)
# print(d[0:4])
# # #split
# j=st.split("a")
# print(j)
# # #join
# print((",").join(st))
# # #count
# print((st.count)("o"))
# ## INDEX 
# print(d.index(1))
# ##BOOLEN
# print(0==0)
# print(0==1)












# #count2
# g=0
# for va in d:
#     print(g)
#     g=g+va
# print(g) 

# #index


















# a="71,72,73.5,45.9"
# b=a.split(",")
# print(b)
# g=0
# for num in b:
#       g=g+float(num)
# print(g)
# print(len(b))
# print(g/len(b))









# alist=[3,67,"cat",[56,57,"dog"],[],3.14,false]
# print(alist[4:])






# s="python rocks"
# print(s[3])



# alist=[1,3,5]
# print(alist*3)















# alist=[3,67,"cat",[56,57,"dog"],[],3.14,False]
# print(alist[4:])











# a=16-2*5//3+1
# print(a)













# from re import X


# X=15
# y=X
# X=22
# print(X)
# print(y)














# alist=[1,3,5]
# blist=[2,4,6]
# print(alist+blist)



# print(int[53.785])

















# x=12
# x=x-3
# x=x+5
# x=x+1
# print(x)













# qu="wow,welcome week! were you wanting to go"
# ty=qu.count("we")
# print(ty)



































# ###list me kisi cheej ko add karna
# d=["a","b","c"]
# a=d.append("v")
# print(a)
# print(d)
# ###list mein maan badlna 
# d[1:2]="a","g","devendra"
# print(d)





















# s="python rocks"
# for ch in s:
#     print("hello")


























# ###list me anupaat

# d=['devendra','kumar', 'dhurvey','dungariya','fvdungariya','mandla','mp']
# print(d[0:4])
# print(d[0:6])
# print(d[0:5])
# print(d[0:3])





























# s="python"
# for idx in range(len(s)):
#     print(s[idx%2])






































# i=1
# while i <=20:
#     if i % 2 ==  0:
#       print(i)
#     i = i + 1

# i=1
# while i<=20:
#   if i%2==0:
#     (str(i) + "is even")
#   else:
#     print(str(i)+ " is odd")
#   i = i+1


























# i=0
# while True:
#     print(i)
#     i=i+1
#     if i>=750:
#         print("breaking")
#         break
#         if i == 749 :
#             print(i)
#             continue








































# # Python program to draw a tree using turtle
# # Importing required modules
# import turtle
# import math


# # Function to draw rectangle
# def drawRectangle(t, width, height, color):
# 	t.fillcolor(color)
# 	t.begin_fill()
# 	t.forward(width)
# 	t.left(90)
# 	t.forward(height)
# 	t.left(90)
# 	t.forward(width)
# 	t.left(90)
# 	t.forward(height)
# 	t.left(90)
# 	t.end_fill()

	
# # Function to draw triangle	
# def drawTriangle(t, length, color):
# 	t.fillcolor(color)
# 	t.begin_fill()
# 	t.forward(length)
# 	t.left(135)
# 	t.forward(length / math.sqrt(2))
# 	t.left(90)
# 	t.forward(length / math.sqrt(2))
# 	t.left(135)
# 	t.end_fill()

	
# # Set the background color
# screen = turtle.Screen ( )
# screen.bgcolor("skyblue")


# # Creating turtle object
# tip = turtle.Turtle()
# tip.color ("black")
# tip.shape ("turtle")
# tip.speed (2)


# # Tree base
# tip.penup()
# tip.goto(100, -130)
# tip.pendown()
# drawRectangle(tip, 20, 40, "brown")


# # Tree top
# tip.penup()
# tip.goto(65, -90)
# tip.pendown()
# drawTriangle(tip, 90, "lightgreen")
# tip.penup()
# tip.goto(70, -45)
# tip.pendown()
# drawTriangle(tip, 80, "lightgreen")
# tip.penup()
# tip.goto(75, -5)
# tip.pendown()
# drawTriangle(tip, 70, "lightgreen")
# tip.hideturtle()
# screen.exitonclick()












# # Python program to draw
# # Spiral Square Outside In and Inside Out
# # using Turtle Programming
# import turtle #Outside_In
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size-5

# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)






# import turtle #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")

# def sqrfunc(size):
# 	for i in range(4):
# 		skk.fd(size)
# 		skk.left(90)
# 		size = size + 5

# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)







# # Python program to draw
# # Rainbow Benzene
# # using Turtle Programming
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
# 	t.pencolor(colors[x%6])
# 	t.width(x//100 + 1)
# 	t.forward(x)
# 	t.left(59)






# # Python program to draw star
# # using Turtle Programming
# import turtle
# star = turtle.Turtle()

# star.right(75)
# star.forward(100)

# for i in range(4):
# 	star.right(144)
# 	star.forward(100)
	
# turtle.done()













#Python program to draw car in turtle programming

# Import required library
import turtle


# car = turtle.Turtle()


# # Below code for drawing rectangular upper body
# car.color('#008000')
# car.fillcolor('#008000')
# car.penup()
# car.goto(0,0)
# car.pendown()
# car.begin_fill()
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.left(90)
# car.forward(370)
# car.left(90)
# car.forward(50)
# car.end_fill()


# # Below code for drawing window and roof
# car.penup()
# car.goto(100, 50)
# car.pendown()
# car.setheading(45)
# car.forward(70)
# car.setheading(0)
# car.forward(100)
# car.setheading(-45)
# car.forward(70)
# car.setheading(90)
# car.penup()
# car.goto(200, 50)
# car.pendown()
# car.forward(49.50)


# # Below code for drawing two tyres
# car.penup()
# car.goto(100, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
# car.penup()
# car.goto(300, -10)
# car.pendown()
# car.color('#000000')
# car.fillcolor('#000000')
# car.begin_fill()
# car.circle(20)
# car.end_fill()
# car.hideturtle()
# turtle.exitonclick()


















# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


























# import turtle
# import colorsys

# def draw_stick(x,y,length,pensize,color,angle):
#     turtle.up()
#     turtle.goto(x,y)
#     turtle.seth(angle)
#     turtle.pensize(pensize)
#     turtle.down()
#     turtle.color(color)
#     turtle.fd(length)

# def draw_tree(x,y,length,pensize,hue,angle,fat_angle,n):
#     if n == 0:
#         return
#     (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
#     draw_stick(x,y,length,pensize,(r,g,b),angle)
#     tx = turtle.xcor()
#     ty = turtle.ycor()
        
#     draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle+fat_angle,fat_angle,n-1)
#     draw_tree(tx,ty,length*0.7,pensize*0.7,hue-1/13,angle-fat_angle,fat_angle,n-1)
    
# turtle.setup(800,800)
# turtle.title("Rainbow Colored Tree - PythonTurtle.Academy")
# turtle.speed(5)
# turtle.hideturtle()
# turtle.tracer(5)
# turtle.bgcolor('black')

# draw_tree(0,-300,200,10,12/13,90,25,12)
# turtle.exitonclick()


























# import turtle
# Cppsecrets = turtle.Screen()
# Cppsecrets.bgcolor('black')
# s = turtle.Turtle()
# s.speed('fastest')
# s.color('white')
# rotate=int(180)
# def Circles(t,size):
#     for i in range(10):
#         t.circle(size)
#         size=size-4
# def Cppsecrets1(t,size,repeat):
#   for i in range (repeat):
#     Circles(t,size)
#     t.right(360/repeat)
# Cppsecrets1(s,200,10)
# t1 = turtle.Turtle()
# t1.speed(0)
# t1.color('yellow')
# rotate=int(90)
# def Circles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-10
# def Cppsecrets1(t,size,repeat):
#     for i in range (repeat):
#         Circles(t,size)
#         t.right(360/repeat)
# Cppsecrets1(t1,160,10)
# t2= turtle.Turtle()
# t2.speed(0)
# t2.color('blue')
# rotate=int(80)
# def Circles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-5
# def Cppsecrets1(t,size,repeat):
#     for i in range (repeat):
#         Circles(t,size)
#         t.right(360/repeat)
# Cppsecrets1(t2,120,10)
# t3 = turtle.Turtle()
# t3.speed(0)
# t3.color('red')
# rotate=int(90)
# def Circles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-19
# def Cppsecrets1(t,size,repeat):
#     for i in range (repeat):
#         Circles(t,size)
#         t.right(360/repeat)
# Cppsecrets1(t3,80,10)
# t4= turtle.Turtle()
# t4.speed(0)
# t4.color('green')

# rotate=int(90)
# def Circles(t,size):
#     for i in range(4):
#         t.circle(size)
#         size=size-20
# def Cppsecrets1(t,size,repeat):
#     for i in range (repeat):
#         Circles(t,size)
#         t.right(360/repeat)
# Cppsecrets1(t4,40,10)
# Cppsecrets.exitonclick()





































# from turtle import * 
# import  random

# speed(speed ='fastest')

# def draw(n, x, angle):
# 	# loop for number of stars
# 	for i in range(n):
		
# 		colormode(255)
		
# 		# choosing random integers
# 		# between 0 and 255
# 		# to generate random rgb values
# 		a = random.randint(0, 255)
# 		b = random.randint(0, 255)
# 		c = random.randint(0, 255)
		
# 		# setting the outline
# 		# and fill colour
# 		pencolor(a, b, c)
# 		fillcolor(a, b, c)
		
# 		# begins filling the star
# 		begin_fill()
		
# 		# loop for drawing each star
# 		for j in range(5):
			
# 			forward(5 * n-5 * i)
# 			right(x)
# 			forward(5 * n-5 * i)
# 			right(72 - x)
			
# 		# colour filling complete
# 		end_fill()
		
# 		# rotating for
# 		# the next star
# 		rt(angle)
		

# # setting the parameters
# n = 30 # number of stars
# x = 144 # exterior angle of each star
# angle = 18 # angle of rotation for the spiral

# draw(n, x, angle)































# from random import randrange
# from turtle import Turtle, Screen

# MAX_ANGLE = 30
# MAX_DISTANCE = 250

# def jaggedLine(turtle, pieceLength):
#     randomColor(turtle)

#     while turtle.distance(0, 0) < MAX_DISTANCE:
#         angle = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
#         turtle.right(angle)
#         turtle.forward(pieceLength)

# def jumpToCenter(turtle):
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()

# def randomColor(turtle):
#     r = randrange(255)  # red component of color
#     g = randrange(255)  # green component
#     b = randrange(255)  # blue component

#     turtle.pencolor(r, g, b)

# def main():
#     s = Screen()
#     s.colormode(255)
#     t = Turtle()
#     t.pensize(2)
#     t.speed('fastest')  # because I have no patience

#     for angle in range(0, 360, 2):
#         jumpToCenter(t)
#         t.setheading(angle)
#         jaggedLine(t, 30)

#     t.hideturtle()

#     s.mainloop()

# if __name__ == "__main__":
#     main()
















































# import turtle
# colors=['red','purple','blue','green','yellow','orange']
# turtle.bgcolor('black')
# for x in range(360):
#     turtle.pencolor(colors[x%6])
#     turtle.width(x/100+1)
#     turtle.forward(x)
#     turtle.left(59)






































































# from turtle import *
# import turtle as tur

# tur = tur.Turtle()
 

# tur.penup ()
# tur.left (90)
# tur.fd (200)
# tur.pendown ()
# tur.right (90)
 

# tur.fillcolor ("red")
# tur.begin_fill ()
# tur.circle (10,180)
# tur.circle (25,110)
# tur.left (50)
# tur.circle (60,45)
# tur.circle (20,170)
# tur.right (24)
# tur.fd (30)
# tur.left (10)
# tur.circle (30,110)
# tur.fd (20)
# tur.left (40)
# tur.circle (90,70)
# tur.circle (30,150)
# tur.right (30)
# tur.fd (15)
# tur.circle (80,90)
# tur.left (15)
# tur.fd (45)
# tur.right (165)
# tur.fd (20)
# tur.left (155)
# tur.circle (150,80)
# tur.left (50)
# tur.circle (150,90)
# tur.end_fill ()
 

# tur.left (150)
# tur.circle (-90,70)
# tur.left (20)
# tur.circle (75,105)
# tur.setheading (60)
# tur.circle (80,98)
# tur.circle (-90,40)

# tur.left (180)
# tur.circle (90,40)
# tur.circle (-80,98)
# tur.setheading (-83)

# tur.fd (30)
# tur.left (90)
# tur.fd (25)
# tur.left (45)
# tur.fillcolor ("dark green")
# tur.begin_fill ()
# tur.circle (-80,90)
# tur.right (90)
# tur.circle (-80,90)
# tur.end_fill ()
# tur.right (135)
# tur.fd (60)
# tur.left (180)
# tur.fd (85)
# tur.left (90)
# tur.fd (80)
 
# tur.right (90)
# tur.right (45)
# tur.fillcolor ("dark green")
# tur.begin_fill ()
# tur.circle (80,90)
# tur.left (90)
# tur.circle (80,90)
# tur.end_fill ()
# tur.left (135)
# tur.fd (60)
# tur.left (180)
# tur.fd (60)
# tur.right (90)
# tur.circle (200,60)
# turtle.exitonclick()



















































# # importing turtle for graphics
# import turtle

# # Forming the window screen
# tut = turtle.Screen()

# # background color green
# tut.bgcolor("White")

# # object
# pen = turtle.Turtle()

# #speed of pen
# pen.speed(10)

# # object color
# pen.color("Green")

# # object width
# pen.width(10)
# tut = turtle.Screen()


# # Code for symbol
# # backward C
# for x in range(180):
#     pen.forward(1)
#     pen.right(1)

# # up
# pen.right(90)
# pen.forward(50)

# # right
# pen.right(90)
# pen.forward(130)

# # down
# pen.right(90)
# pen.forward(50)
# pen.left(90)

# # forward C
# for x in range(180):
#     pen.backward(1)
#     pen.right(1)

# turtle.done()



























































# # Python program to draw smile
# # face emoji using turtle
# import turtle

# # turtle object
# pen = turtle.Turtle()

# # function for creation of eye
# def eye(col, rad):
# 	pen.down()
# 	pen.fillcolor(col)
# 	pen.begin_fill()
# 	pen.circle(rad)
# 	pen.end_fill()
# 	pen.up()


# # draw face
# pen.fillcolor('yellow')
# pen.begin_fill()
# pen.circle(100)
# pen.end_fill()
# pen.up()

# # draw eyes
# pen.goto(-40, 120)
# eye('white', 15)
# pen.goto(-37, 125)
# eye('black', 5)
# pen.goto(40, 120)
# eye('white', 15)
# pen.goto(40, 125)
# eye('black', 5)

# # draw nose
# pen.goto(0, 75)
# eye('black', 8)

# # draw mouth
# pen.goto(-40, 85)
# pen.down()
# pen.right(90)
# pen.circle(40, 180)
# pen.up()

# # draw tongue
# pen.goto(-10, 45)
# pen.down()
# pen.right(180)
# pen.fillcolor('red')
# pen.begin_fill()
# pen.circle(10, 180)
# pen.end_fill()
# pen.hideturtle()
# turtle.exitonclick()
































































# #import module
# import turtle

# #define pen size
# turtle.pensize (5)

# #define pen color
# turtle.pencolor ("Blue")

# #for outer bigger circle
# turtle.fillcolor ("red")
# turtle.penup ()
# turtle.goto (0, -200)
# turtle.pendown ()
# turtle.circle (200)

# #for eyes
# turtle.penup ()
# turtle.goto (-100,50)
# turtle.pendown ()
# turtle.begin_fill ()
# turtle.circle (17.5)
# turtle.end_fill ()
# turtle.penup ()
# turtle.goto (100,50)
# turtle.pendown ()
# turtle.begin_fill ()
# turtle.circle (17.5)
# turtle.end_fill ()

# #for nose
# turtle.penup ()
# turtle.goto (0,50)
# turtle.pendown ()
# turtle.circle (-70, steps=3)

# # for smile
# turtle.penup ()
# turtle.goto (-100, -70)
# turtle.pendown ()
# turtle.right (90)
# turtle.circle (100,180)
# turtle.mainloop ()



































































# # Import turtle package
# import turtle

# # Creating a turtle screen object
# sc = turtle.Screen()

# # Creating a turtle object(pen)
# pen = turtle.Turtle()

# # Defining a method to form a semicircle
# # with a dynamic radius and color
# def semi_circle(col, rad, val):

# 	# Set the fill color of the semicircle
# 	pen.color(col)

# 	# Draw a circle
# 	pen.circle(rad, -180)

# 	# Move the turtle to air
# 	pen.up()

# 	# Move the turtle to a given position
# 	pen.setpos(val, 0)

# 	# Move the turtle to the ground
# 	pen.down()

# 	pen.right(180)


# # Set the colors for drawing
# col = ['violet', 'indigo', 'blue',
# 	'green', 'yellow', 'orange', 'red']

# # Setup the screen features
# sc.setup(600, 600)

# # Set the screen color to black
# sc.bgcolor('black')

# # Setup the turtle features
# pen.right(90)
# pen.width(10)
# pen.speed(7)

# # Loop to draw 7 semicircles
# for i in range(7):
# 	semi_circle(col[i], 10*(
# 	i + 8), -10*(i + 1))

# # Hide the turtle
# pen.hideturtle()






























































# import turtle
# import math

# # Set the background color
# screen = turtle.Screen()
# screen.bgcolor("lightpink")

# # Create our turtle
# t = turtle.Turtle()
# t.color("black")
# t.shape("turtle")
# t.speed(5)

# # Define a function to draw and
# # fill a rectangle with the given
# # dimensions and color
# def drawRectangle(t, width, height, color):

# 	t.fillcolor(color)
# 	t.begin_fill()
# 	t.forward(width)
# 	t.left(90)
# 	t.forward(height)
# 	t.left(90)
# 	t.forward(width)
# 	t.left(90)
# 	t.forward(height)
# 	t.left(90)
# 	t.end_fill()


# # Define a function to draw and fill an equalateral right
# # triangle with the given hypotenuse length and color. This
# # is used to create a roof shape.
# def drawTriangle(t, length, color):
# 	t.fillcolor(color)
# 	t.begin_fill()
# 	t.forward(length)
# 	t.left(135)
# 	t.forward(length / math.sqrt(2))
# 	t.left(90)
# 	t.forward(length / math.sqrt(2))
# 	t.left(135)
# 	t.end_fill()


# # Define a function to draw and fill a parallelogram, used to
# # draw the side of the house
# def drawParallelogram(t, width, height, color):
# 	t.fillcolor(color)
# 	t.begin_fill()
# 	t.left(30)
# 	t.forward(width)
# 	t.left(60)
# 	t.forward(height)
# 	t.left(120)
# 	t.forward(width)
# 	t.left(60)
# 	t.forward(height)
# 	t.left(90)
# 	t.end_fill()


# # Draw and fill the front of the house
# t.penup()
# t.goto(-150, -120)
# t.pendown()
# drawRectangle(t, 100, 110, "blue")

# # Draw and fill the front door
# t.penup()
# t.goto(-120, -120)
# t.pendown()
# drawRectangle(t, 40, 60, "lightgreen")

# # Front roof
# t.penup()
# t.goto(-150, -10)
# t.pendown()
# drawTriangle(t, 100, "magenta")

# # Side of the house
# t.penup()
# t.goto(-50, -120)
# t.pendown()
# drawParallelogram(t, 60, 110, "yellow")

# # Window
# t.penup()
# t.goto(-30, -60)
# t.pendown()
# drawParallelogram(t, 20, 30, "brown")

# # Side roof
# t.penup()
# t.goto(-50, -10)
# t.pendown()
# t.fillcolor("orange")
# t.begin_fill()
# t.left(30)
# t.forward(60)
# t.left(105)
# t.forward(100 / math.sqrt(2))
# t.left(75)
# t.forward(60)
# t.left(105)
# t.forward(100 / math.sqrt(2))
# t.left(45)
# t.end_fill()
# turtle.done()
















































































# import turtle
# animation = turtle.Turtle()
# animation.hideturtle()
# animation.getscreen().bgcolor("black")
# animation.speed(0)
# animation.color("white")
# animation.goto(0,0)
# turtle.speed(1)
# for d in range(111360):
# 	animation.circle(d)
# 	animation.lt(105)
# turtle.exitonclick()

































































# dk_list=['a','b','c','d','e','f','g']
# ####join
# print("**".join(dk_list))
# ###append
# dk_list.append('h')
# print(dk_list)
# ###list ko idex mein add karna
# dk_list[0:2]=("devendradhur85@gmail.com")
# print(dk_list)






# ###########avrage in string??
# a="15+20+2.5+3+3.4+4+65+97+9+6"+"9"
# d=a.split("+")
# print(d)
# dd=0
# for var in d :
#     dd=dd+float(var)
# print(dd)
# print(len(d))
# avg=(dd/len(d))
# print(avg)
# print(avg,"is your avrage")
# print(type(avg))





























# ### IN AND NOT IN OPRATORS             IT IS BOOLEAN TYPE
# print('d' in 'devendra')
# print("d" not in "ground")



# #####IN AND NOT IN OPRATORS 2
# dlist=['a','b','c','d']
# print('d','a','g' in (dlist))


# ##int
# a=1,2,3,4,5
# print(1,3,4,2,1 in a)

































# ## if else:


# per_rain=[94.3,45,100,78,16,5.3,79,86]
# resp=[]
# for v in per_rain:
#    if v >90:
#        resp.append("bring an umbrella")
#    elif v > 80:
#        resp.append("good for the flowers")
#    elif v > 50:
#        resp.append("whatch out for clouds")
#    else:
#         resp.append("nice day")
# print(resp)


































# #### num mein list
# num=(list(range(0,68)))
# print(num)



























# fruit="Apple Banana Mango Orange"
# v=0
# for chr in fruit:
#     if chr != " " :
#        v=v+1
# print(v)























# fruit="apple banana mango orange"
# v=0
# for chr in fruit:
#     if chr == "a":
#        v=v+1
#     elif chr == "e":
#        v=v+1
#     elif chr == "i":
#        v=v+1
#     elif chr == "o":
#        v=v+1
#     elif chr == "u":
#        v=v+1
# print(v,"  itne vovel hain fruit mein .")



























# fruit="apple banana mango orange"
# x=0
# for chr in fruit:
#     if chr in ['a','e','i','o','u']:
#         x=x+1
# print(x)
































# str1="today you are you! that is truer than true there is no one "
# if "true" in str1:
#     print("True! you are you!")
# elif "false" in str1:
#     print("False. you aren't you?")
# else:
#     print("Neither true nor False!")



































# num=[5,11,9,22,2,25,3,30]
# large_num=0
# for big in num:
#     if big>=large_num:
#         large_num=big
# print(large_num)















































# words=["adopt","bake","beam","confide","grill","plant","time","wish"]
# past_tense=[]
# for var in words:
#     if "e" in var[-1] :
#         past_tense.append(var+'d')      
#     else:
#         past_tense.append(var+'ed')
# print(past_tense)




































# ### MUTABLE AND IMUTABLE
# alist=['a','b','c','d']
# alist[1]='d'
# print(alist)
# alist[1:2]='f','e','k','m'
# print(alist)
# alist[1:4]=[]
# print(alist)


# ## MUTABLE AND IMUTABLE in string(type error)

# alist="a,b,c,d"
# alist[1]='d'
# print(alist)












# ## MUTABLE AND IMUTABLE in string

# str1="hello world"
# str1='j'+ str1[1:]
# print(str1)

# str2=str1[0]+"jk"+str1[3:]
# print(str2)




















# ####DEL()
# a=[1,2,3,4,5,6,7,8,9,0]
# del a[3]
# print(a)
# del a[0:3]
# print(a)














######### ID
# a="banana"
# b="apple"
# print(a is b)
# print(id(a))
# print(id(b))












# #########2222222222222
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# print(id(a))
# print(id(b))








# #########33
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# a=b
# print(a is b)
# print(id(a))
# print(id(b))























# ########44444444
# a=[1,2,3]
# b=[1,2,3]
# print(a is b)
# a=b
# b[0]=4
# print(a)



















































# # Python code to demonstrate string length
# # using len

# str = "geeks"
# print(len(str))

















# # Python code to demonstrate string length
# # using for loop

# # Returns length of string
# def findLen(str):
# 	counter = 0	
# 	for i in str:
# 		counter += 1
# 	return counter


# str = "geeks"
# print(findLen(str))




























# # Python code to demonstrate string length
# # using while loop.

# # Returns length of string
# def findLen(str):
# 	counter = 0
# 	while str[counter:]:
# 		counter += 1
# 	return counter

# str = "geeks"
# print(findLen(str))





































# # Python code to demonstrate string length
# # using join and count

# # Returns length of string
# def findLen(str):
# 	if not str:
# 		return 0
# 	else:
# 		some_random_str = 'py'
# 		return ((some_random_str).join(str)).count(some_random_str) + 1

# str = "geeks"
# print(findLen(str))














































# user_name=input("name")
# user_password=input("password")
# print( "this is"" "+user_name)
# print("this is"" "+user_password)




























# a="banana"
# b="apple"
# print(a is b)
# print(id(a))
# print(id(b))


















# ########        CLONE

# a=list(range(0,11))
# b=a[:]
# print(a)
# print(b)
# print( a is b )
# print(id(a))
# print(id(b))
# b[5]="a"
# print(a)
# print(b)
































# a=[1,2,3]
# b=a*3
# b[3]=90
# print(a)





# a=[1,2,3]
# a.insert(1,10)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.remove(1)
# print(a)



# ##  list se item ko hatana or variable me badalna 
# a=[1,2,3,4,5,6,7,8,9,0]
# b=a.pop(5)
# print(b)
# print(a)









