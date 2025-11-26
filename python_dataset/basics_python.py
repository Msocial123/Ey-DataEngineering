# this is a inline comment
#
# login page
# 1.read the inputs from the user
# 2.user name
# 3.password
# 4.login button
# 5.store it into database
# store the value for x it may b e contains the marks of the student
# x=10
# y=20    #y can store marks
#
# select all the lines ctl + A ctl+?/
import random
from ctypes import c_void_p
from math import floor, ceil, trunc
from operator import truediv
from threading import Condition
from tkinter.font import names
from tokenize import endpats

#print()
# a builtin function which is used to display the output message ,
# whcih is able to communicate with users as output screen

# print("this is python example")

# what is function  which can accept inputs and process something and then give output

# print(" hi python")
# print('hi python')
# #print("commented line")
# print("hi python")
# print("-----------------------------------")
# print("     THIS IS PYTHON FIRST SESSION  ")
# print("------------------------------------")
# print python " pyhton"
# print("hi \"python\" ")
# # print python ' pyhton'
# print('hi \'python\' ')
#
# print("path:C:\\user\\murali_mohan")

# print("message1 \n\n\n\n\n\n\n\n\nmessage2")

# print("message1 \tmessage2")

# print("""Course includes following Subjects:\n\t-Datawh
#       \t-Bigdata\t-Agile\n\t-SQl Advanced
#       \t-Python""")

# a=10
# b=20
# c=a+b
# print(a)
# print(b)
# print("sum",c)

                        # Variable
# variable is a name you create to store a value, so you can use it in your program /code
# make programs dynamic
#name to store value
#stored in memory
#reusable any time
#update variable at anytime

# a=10
# b=20
# name="murali mohan"
#
# name="sql"
#
# print(name,"script that contains the word ",name)
# print("Here is another line of ",name + "code that demonstrates Python syntax.")
#
# name="Python"
# print(name,"script that contains the word ",name)

            # input() function -> a builtin function that stops your program to get user input
            # print() displaying something to the user
            # input() get something from the user
#             using input() alone reads the user's response but immediately discards it.'
            # to keep this value, assign that to a variable
# input("enter the your name")
# name = input("enter your name:")
# print("your name is :",name)

# Hardcode vs dynami values
# a=10 #int
# b=3.5 #float
# c="heloo" # String
# d="21234565" # string
# e='123' #string
# f=True #boolean can either true or false , used to handle logic and decision making
# g=False # boolean
# h=None # none type
# i="" # sting blank
# j=" " # STING Empty space

            # functions + data types
            # do something(functions)  to data (value)

    # Functions:                                                Methods:
    # -> it is independent block of code            functions belongs to object/class
    # Syntax : Function_name(value)                 value.method_name() /value or variables
    # print('python')                               'hello'.upper()
    #type(50)                                        50.bit_length()


# text="hai"
# number=100
# print(text)
# print(number)
# type() -->  builtin function , return the data type of a value, so that you can know what type of object it is
# print(type(text))
# print(type(number))
#len() -->it will give total count of items inside your a value to help measuring the lentgh
# print(len(text))
# print(len(number)) --> not acceptable
# upper()--> convert sting to uppercases
# print(text.upper())
# print(number.upper()) -- not accepted
# bit.length()--> <method of class int> return the length of a number in binary
# print(number.bit_length())
# print(text.bit_length())

# -> each values has a dtatype
# -> automaticall detects the data types
# ->dynamic:datatypes can change any time
# ->      no vlaue : None
#        single value: int,str,bool,float
#         multiple values; set,tuple,dict,list

# name="murali"
# print(type(name))
#
# mobile=12345678
# print(type(mobile))
# print("mobile number is" + mobile )

# str() which is used to convert the  variable in to sting type

# print("mobile number is" + str(mobile) )
# print(type(mobile))
# number=mobile+3
# number=str(mobile)
# print(type(number))
# number=number+"one"
# print(number)

#math
# password="123ab22fg52f5f5"
# print(len(password))
# if len(password)<8:
#     print("your password is too short")

#count(substring)-> str method
# it returns how often a word reapeted/appeard in the sting
# text="This is a sample Text. This Text contains repeated words, like 'this' and 'text'."
# print(text.count("&"))

# replace()--> its is used to replace old text or value to the new value
# 2025/10/28 -> 2025-10-28 old(/)  new(-)
# price="1500,50"
# print(price.replace(",","."))
# mobile='-91 785554555451245'
# print(mobile.replace("-","+"))
# print(mobile.replace(" ",""))
# date_for='2025/10/28'
# print(date_for.replace("/","-"))
# total_sale="$1000000"
# print(total_sale.replace("$","₹"))
# +  concatination
# folder="C:/Users/python"
# file="report.csv"
# full_file_path=folder + file
# print(full_file_path)
# name="kiran"
# age=20
# location="india"
# std="12th"
# print("my name is "+name + "my age is " + str(age) + " and my location is " + location + " and my standard is  " + std)
#f{string} -> modern, supereasy way to format and build stings
# f stands for formatted ... lets you easily put variables and expressions directly inside single value
# print(f"my name is {name}, my age is {age}, my location is {location}, my standard is {std}")
# print(f" 2 + 3 ={2 + 3}")
#SPLIT() -> IT WILL BE USED TO SPLIT THE DATA BASED ON THE DELIMITER , by default it split by using space
# "NAME AGE LOCATION"
# "KIRAN,30,INDIAN"
# STAMP="2025-10 28"
# print(STAMP.split())
# dat_csv_file="KIRAN,30,INDIAN"
# print(dat_csv_file.split(","))

# sting multiplication *

# text='ha'
# print(text * 3)
# print("**" *30)
# print("\twelcome to python language")
# print("**" * 30)

#index and slicing
# text="python"
# # extract the first character
# print(text[0])
# print(text[-6])
# # extract the last character
# print(text[-1])
# print(text[5])
# t_date='2025-10-28'
# print(t_date[0:4])
# print(t_date[:4])
# print(t_date[5:7])
# print(t_date[8:])
# print(t_date[-2:])
# TEXT="    Process finished with exit code 0     ".lstrip()
# print(TEXT)
# TEXT="    Process finished with exit code 0     ".rstrip()
# print(TEXT)
#
# TEXT="    Process finished with exit code 0     ".strip()
# print(TEXT)

# text="####abc####".strip("#")
# print(text)
# text="*****abc####".strip("*#")
# print(text)
# text="abc####".strip("a")
# print(text)
#startswith-->startswith(substring) boolean
# to check the beiging values is available or matching eith given values
# phone="+91 12521385645"
# print(phone.startswith("+91"))
#endwith()- method used to check the given value is really ended the sting ->boolean
# email="murali@gmail..com"
# print(email.endswith("gmail.com"))

# file="sales.txt"
# print(file.endswith(".csv"))
#in -->substring in string its an operator -> return boolean
# check if a word or text exist in the string

# email="murali@gmail.com"
# print("@" in email)
#
# email="muraligmail.com"
# print("@" in email)
# url="https://api.company.com/v1/data"
# print("api" in url)

# find()-->is used to when combined with other methods to add dynamics
#it returns the index value where the word is found

# phone="+91 817988235242"
# phone2="91-817988235242"
# phone3="    817988235242"
# print(phone.find("+91"))
# # print(phone.find("+91"))
# print(phone[4:])
# print(phone2.find("-")+1)
# print(phone[phone.find(" ")+1:])
# print(phone2[phone2.find("-")+1:])
# print(phone3[phone3.find(" ")+1:])

#validation

#isalpha()-  it is a string method which returns the boolean
#it is used to check if the sting is contains only letters

# country="INDIA"
# print(country.isalpha())
#  #innumeric() it is used to check given string contains only numeric values or not -- boolean
# phone="78546r.5861629812"
# print(phone.isnumeric())

#Numerics
# x="5"
# y=5.5
# z=2+3j
# print(type(x))
# x=int(x)
# print(type(x))
# print(x * 5)

# a=3.5
# print(type(a))
# print(a * 5)

# a="3.5"
# print(type(a))
# print(a * 5)
# a=float(3.5)
# print(type(a))

# print(1 +2 )
# print(5-3)
# print(5*3)
# print(7/2)
# print(7//2) #floor division (it devides two numbers and rounds it down)
# print(7 % 2)  # reminder -. the leftover part after the division ... used to check if the number is even or odd
#
# print(10 % 2)
# print(2 ** 3) #exponentiation -> it raises a number to the power of another number
# 2*2*2

# x=2
# x=x+3   #=> (X=2+3) 5
# print(x)
# x+=3
# print(x)
#
# x=x-3
# x-=3
#ROunding
#measure the distance
# print(abs(2 - 10))

# price=35.542525
# print(round(price))
# print(floor(price))
# print(ceil(price))
#math.trunc(x) -> cutoff the decimal part and it keeps whole number (no rounding)
# print(trunc(price))
# print(int(price)) #if not imported the math module then , use int otherwise use trunc()
#random() it is a method which is used to generate some random numbers
# print(random.random())

#randint() ->(start,end ) -> gets a random whole number from start to end(both included)
# print(random.randint(18,30))
# is_integet() --> boolean
# checks if a float has no decimal part(is a whole number)
# x=7.00000
# print(x.is_integer())
#
# y=7.4252552
# print(y.is_integer())

#isinstance()(value,type)  -> boolean check if a value belongs to certain data type
# x=70.255
# print(isinstance(x, int))
# print(isinstance(x, float))

#boolean
# print(True)
# print(False)
#
# print(type(True))
# print(bool("heloo")) #-- true becase some data is available
# print(bool())
# print(bool(0))
# print(bool(""))
# print(bool(" "))
# print(bool(None))
# print(type((None)))
# email="murali@gmail.com"
# phone="9824256260316313"
# username='murali@123'
# #if any field is filled then allow
# # print(any([email,phone,username]))
# #all  field are required
# print(all([email,phone,username]))

# isinstance() (value,type)->checks if a value belongs to certain data type
# print(isinstance(123,int))
# print(isinstance('123',int))
# print(isinstance(True,str))
#
# print("heloo".endswith('o'))
# print("heloo".startswith('o'))

# x=5
# b=10
# variable x<10 -- true
# value 3>2- true
# expresiions 5+5!=10 false
# functions len("hai")==3 -- true

# print(10 == 10)
# print(10 != 10)
# print(7>3)
# print(7>=3)
# print(3<7)
# print(7<=7)
#
# string comparision
# print("a" == "A")
# print("a" = "A")

# chain of comparision
# print(1<4<6)
# 1<4 -true
# 4<6 -- true final result is true
# print(5<4<6)
# 5<4 false
# 4<6 true
#is age between 18 and 30?
age=35
# print(18<= age <=30)
# 18<=20 -->true
# 20<=30 --> treu
# 18<=35 -->true
# 35<=30 --> false

#logical operators --> used to combine one or more (multiple) boolean expressions
#and or not --> it returns either true or false

# print(3<5 and 5==5)
# print(3>1 and 5<1)

#check if the system is under pressure

# cpu_usage=70
# memoryusage=50
# print(cpu_usage>90 or memoryusage>90)
# print(cpu_usage>90 and memoryusage>90)
# logical NOT operator
# it reverse the truth it returns true into false and false into true
#         3>2-->True
#         5==8 -->False
#    Not 3>2--> flase
#    not 5==8 -->true

# print(not 3>2)
# print(not True)
# print(not False)
# name="murali"
# print(not name)
# print(not 0)
# control mixed conditions
#the right side condition or operator having heiger priority

 # x=5
 # y=8
 # z=6
 # x==5  or  y>5  and  z<4
 # 5==5 or 8>5 and 6<4
 # and is having more priority than or
# 1.8 > 5 and 6 < 4 --> Fasle
# 2. 5==5 or 8>5 --> true
# true or false  --> true
#
# x=5
# y=8
# z=6
# print(x==5 or y>5 and z<4) #true
#  # to controll tyhe execution use ()
# #
# # # (x==5 or y>5) and z<4
# # True and False  --> false
# print((x==5 or y>5) and z<4) # false

# Membership (In) operator
# check if a value inside another value
# like a string ,list,tuple or sequences
# 'a' in 'Data' --> True
# 'a' not in 'Data' --> False
# pax=['abhiram','alfin','amith','aswin','Bhavya','gopika','nandna','nicy james','sidharth','sowmyajith','swayammishra']
#
# print('abhiram' not in pax)
# print("Murali Mohan" in pax)
#
# print(3 not in [1,2,3,4])

# Identity (Is) operator
# Check if two variables refer to the same object in memory
# x=['a','b','c','d','e','f']
# Y=['a','b','c','d','e','f']
# print(x == Y)
# print(x is Y)
#
# x=10
# y=10
# print(x == y)
# print(x is y)


# CONDITIONAL STATEMENTS
# CHECKPOINT  THAT CHECKS A Condition
#        - TRUE? RUN THE CODE
#         - FALSE ? SKIP IT

# STANDALONE IF
# DEFINES THE CONDITION : IF THIS IS TRUE DO THIS  - OTHERWISE SKIP NOTHING TO DO
# if conditino :
#     do operation
# rules:
# 1. only one if
# 2.starts with if
# 3.requried condition
# 4.can standalone

# score =100
# if score>=90:
#     print("A grade")

    # else statement
    # it runs only if all previous conditions are false
    # if nothing was true, then do this block execution
# if condition:
#     do operation
# else:
#     do work with else block

# rules:
# 1. comes at the end
# 2.no other conditions shoud allow
# 3. optional
# 4.cannot standalone(without if , the else block invalid)
# 5.only one else statement allowed

# score =95
# if score<=90:
#     print("A grade")
# else:
#     print("F")
# elif(else if statement)
# asks a follow-up question only runs if previous condition were false
# if the first wasnt true , try this one

# if condition 1:
#     do execute the block
# elif condition 2:
#     do execute this block
# else:
#     do execute thsi block
# Rules
# 1. comes after if
# 2.multiple elif
# 3.needs a condition
# 4.optional
# 5.cannot be standalone
# score =95
# project_submition=True #python evaluate the boolean conditions directly  avoid explicit comparisions ==true or == false
# if score>= 90:
#     if project_submition:
#         print("A+")
#     else:
#         print("A grade")
# elif score>= 80:
#     print("B grade")
# elif score>= 70:
#     print("C grade")
# else:
#     print("F grade")

    # branching--> if-elif-else
# nesting if  -- if -- if statement inside another if
# connecting conditions with logical operators

# score =95
# project_submition=False
# if score>= 90 and project_submition:
#     print("A+ grade") #--. false
# elif score>= 90:
#     print("A grade")
# elif score>= 80:
#     print("B grade")
# elif score>= 70:
#     print("C grade")
# elif score>= 60:
#     print("D grade")
# else:
#     print("F grade")

# Independent ifs
# each if is checked seperately
# all conditions are tested even if one is already true
# score=50
# submitted_project=True
# if score >=90:
#     print("high score")
# else:
#     print("low score")
#
# if submitted_project:
#     print("project is submitted")
# else:
#     print("project is not submitted")


#email must contains exaly one . and '@' symbol
#email must end with '.com','.org',or '.net'
#email must not be longer than 254 characters
#EMAIL MUST STARTS WITH LETTER OR DIGIT

# email="user@gmail.com2"
# #cleaning the data
# email=email.strip()
# #email must not be empty
# if email =="":
#     print("email must not be empty")
# #email must contain '.' and '@' symbol
# elif not('.' in email and '@' in email):
#     print("email must contain contains . and @ symbols")
# #email must contains exactly one @ symbol
# elif email.count('@')!=1:
#     print("email must contain exactly one @")
# # must ends with .com or .in or .org. or .net
# elif not email.endswith(('.com','.org','.net')):
#     print("email must end with .com or .org .net ")
# #email cannot contain 254 characters
# elif len(email) > 254:
#     print("email must not longer than 254 characters")
# #email must start with letter or digit
# elif not(email[0].isalnum() and email[-1].isalnum()):
#     print("email must strat and ends with letter or digit")
# else:
#     print("email is valid")

# if condition :
#     do something
# else:
#     do something

# inline if (quick and short)
# do something if condition else do something
#  Rules: 1.you must follow up with else block
#         2. youi shouldnot use elif
#           3. USE THIS inline if for simple logics
# you can store the result of either if or else block in  to one variable
        #     variable_name = "A"  if score>=90 else "F"

# score = 50
# if score >= 90:
#     print("A")
# else:
#     print("F")

# print("A" if score >= 90 else "F")
# grade= "A" if score >= 90 else "F"
# print(grade)
# score = 80
# grade=("A" if score>=90 else "B" if score>=80 else "F")
# print(grade)

#case- Match
# evaluate a value against multiple values runs the code of the first match
#convert the full country names in to 2-letters abbreviations

# country="United states"
# if country == "India":
#     print("IND")
# elif country == "United states":
#     print("US")
# elif country == "Egypt":
#     print("EG")
# elif country == "Germany":
#     print("DE")
# else :
#     print("unknown country")

# country=" India "
# match   country:
#     case "India":
#         print("IND")
#     case "United states":
#         print("US")
#     case "Egypt":
#         print("EG")
#     case "Germany":
#         print("DE")
#     case _:
#         print("unknown country")

# Loop:
# conteol the flow of code
# repat a block of code over and over untill condition met

#for loop
# go through a group of items one by one to do something for each item
# python iterator: an object that lets you go through items one by one in a sequence
# rmember whats done and knows whats next
# items=(1,2,3,4,5)
# for item in items:
#     # print("levle :",i)
#     print(f"levle :{item}")

# for loop sequence(tuple, list,sting,file,dic)
# range(stop)
#
# items="python"
# for item in items:
#     # print("levle :",i)
#     print(f"levle :{item}")

#
# for item in range(100):
#       print(f"levle :{item}")
#
# for item in range(1,101):
#       print(f"levle :{item}")
#
# for item in range(2,16,2):
#     print(f"even numbers {item}")

#forloop

# scores=[80,50,60,75]
# total=0
# for score in scores:
#     total +=score
#     print("current total",total)
# print("final total",total)

# files=['Report.csv','DATA.csv','  final.TXT']
# for file in files:
#     file=file.strip().lower().replace('txt','csv')
#     print(f"processing {file}")

# Break -> it stops the loop immediately
# it jumps out and end the loop right away

# names=['abhi','amar','kiran','','kumar','karthik','ramu']
# for name in names:
#     if name == '':
#         print("empty value is detected")
#         break
#     print(f"name:{name}")

# continue: it skips one loop cycle without stopping the loop --> skip current execution and go for next

# names=['abhi','amar','kiran','','kumar','karthik','ramu']
# for name in names:
#     if name == '':
#         print("empty value is detected")
#         continue
#     print(f"name:{name}")
#
#pass -->it is a placeholder where nothing happens
# for now .. just keep going  .. do nothing

# names = ['abhi', 'amar', 'kiran', '', 'kumar', 'karthik', 'ramu']
# for name in names:
#     if name == '':
#         print("empty value is detected")
#         pass         #todo:just handle empty value
#     print(f"name:{name}")


# names = ['abhi', 'amar', 'kiran', '', 'kumar', 'karthik', 'ramu']
# for name in names:
#     if name == '':
#        name=name.replace('','unknown')
#     print(f"name:{name}")


# loop through a list of day  and print only the working days, skip the weekends
# days =['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
# weekends=['Sun','Sat']
# for day in days:
#     if day in weekends:
#        continue
#     print(f'workingDay: {day}')

#scan emails to block unsafe data from entering your system
# emails= [
#     'data@gmail.com',
#     'murali@gmail.com',
#     'drop table user;',
#     'ravi@clahan.com']
# for email in emails:
#     if ';' in email:
#         print('SQL injection: Hacker Attack')
#         break
#     print(f'processing Email: {email}')

# break exit from the loop immediately -->
#critical risk --> cost -->secutity-> integrity -->

#Continue: skip 1 iteration
# medium levl-> bad rows -->empty file/empty data--> skip special cases

# Nested loop/ nested forloop
# for x in range(3):   # outer loop
#     for y in range(2):   # inner loop
#         print(f"({x}, {y})")
        # for z in range(2): print(f"({x}, {y},{z})")
# colors=['red','green','blue']
# sizes=['l','m','s']
# for color in colors:
#     for size in sizes:
#         print(f"{color} - {size}")

# years=[2026,2027]
# months=['Jan','Feb']
# days=range(1,29)
# for y in years:
#     for m in months:
#         for d in days:
#             print(f'report_{y}_{m}_{d}.csv')

# select count(*) from customers where id is null:
# tables=['customer','store','orders','products','price','employe','student','manager']
# columns =['id','created_date']
# for table in tables:
#     for column in columns:
#         print(f'SELECT count(*) FROM {table} WHERE {column} IS NOT NULL')

# crossing the data , navigate hierarchy
#all the possible combinations
# while loop
# repeats a blok of code  over and over as long as condition is true
# i=1
# while i<4:
#     print(i)
#     i+=1

# build a counter from 1-10
# count =1  #-->3 -->5 --->7-->9 -->11
# while count<=10:
#     print(count)
#     count+=2

# write a program that keeps asking "do you agree?" untill the user type yes

# answer =""
# while answer !="yes":
#     answer= input("Do you have agree? (yes/no) ")
# print("thank you ")

# while True:
#   print("infinite loop")

#3 attempts
# yes with in three attempts --> "ok"
# othere wise "3 stikes are over , you are out of


# attempts=0
# while attempts<3:
#     answer=input("do you want agree ? (yes/no):")
#     if answer=="yes":
#         print("ok or on the same page ")
#         break
#     attempts+=1
# print("thank you")

#
# FORLOOP:
# fixed sequence  and predefined conditions are going to use
#     we shoud know number of iterations are occur
#     processing the data
#     simple,clear , safe, no limited

# while loop:
#     the condition true and this condition may be user defined
#     number of iterations are unknown
#     waiting for the external event :(wait for user input)
#     advanced ,flixible , not complex, risk (infinite loop)

# Functions:
# functions is a block of reusable code
# User defined functions( UDF);
# fucntion whcih is created by user/ developer based on the requirements , instead of using any builtin functions

# def -> is nothing but one key word which is used to create the UDF
# def function_name(parameters)
#     statements(s)
# return vale --> None type
# rules:-> start with def key word
#         use lower cases ,_underscores
#         parantheses()
#         indentation
#         return statement (optional) return some values to the function call
# def add_two_number():
#     print("hai")
#
# return_value=add_two_number()
#
# print(type(return_value)).

# def add_two_numbers(a, b):
#     return a+b
#
# result=add_two_numbers(10,20)
# print(f'sum of a,b result:{result}')
#
#
# def add_two_numbers(a, b):
#     result1=a+b
#     return result1
#
# result=add_two_numbers(10,20)
# print(f'sum of a,b result:{result}')

#function with default values:
# def bio(name='murali'):
#     print("helllo",name,"welcome")
#
# bio("ramu")
# bio()
#function with multiple value return
# def caluculate_stats(numbers):
#     total=sum(numbers)
#     avg=total/len(numbers)
#     return total,avg
#
# t,a=caluculate_stats([10,20,30,40])
# print(f'total: {t} - average: {a}')

#function calling another function
def square(n):
    return n * n
def sum_of_squares(a,b):
    return square(a) + square(b)
print(sum_of_squares(3,4))
