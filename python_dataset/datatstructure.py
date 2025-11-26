#create list
# empty =list()
# empty1=[]
# print(empty)
# print(type(empty1))
#
# letters=list('python')
# print(letters)
# print(type(letters))
# numbers=list(range(15))
# print(numbers)
# print(type(numbers))
# mixed_v=[1,2,'a','b',True,None]
# print(mixed_v)
# print(type(mixed_v))
# matrix =[['a','b','c'],
#         ['d','e','f']]
# print(matrix)
# print(type(matrix))
# mixed_matrix=[['a','b'],
#               [1,2,3],
#               [True]]
# print(mixed_matrix)
import copy
from collections.abc import Iterator

#Access and read
# letters =['a','b','c','d']
# print(letters)
# print(letters[0])
# print(letters[-1])
# print(letters[-2])
matrix=[
    ['a','b','c'], #Row 0
    ['d','e','f'], #Row 1
    ['g','h','i']] #Row 2
# print(matrix)
# print(matrix[0])
# print(matrix[-1])
# print(matrix[-1][-1])
# print(matrix[0][0])
# print(matrix[-3][-3])
# print(matrix[2][:2])
# person =['kiran','25','Dataeng','bangalore']
# name= person[0]
# age= person[1]
# role= person[2]
# location= person[3]
# print(role)
# name,age,role,location=person #orde of variable
# print(age)
# name,*details,location=person -->* can be used only once
# print(name,location)
# print(details)
# name,*details=person
# print(details)
# number=[1,2,3]
# first,second,third = number
# print(first)
# number=[1]
# first ,*rest = number
# print(first)
#unpack (list, tuples,strings)
# name='muraliMohan'
# first,*rest=name
# print(rest)
# person =['kiran','25','Dataeng','bangalore']
# name,_,_,_=person
# print(name)
# print(location)
# name1,*_,location=person
# print(location)
#
# Order=[100,200,900,520]
# print('Total_bill:',sum(Order))
# print('Total_no_of_Product:',len(Order))
# print('max_rate of product:',max(Order))
# print('min_rate of product:',min(Order))
# print('All available or not:',all(Order))
#
# print('all:',all([1,0,2]))
# print('any:',any([0,0,20])) #--> oil(200,0)
# print('all:',all(['a','b','']))
# print('all:',all(['a','b','c']))

# emp_id=[100,101,102,103,101,101]
# print("count:",emp_id.count(101))
# print("index of:repeated value",emp_id.index(101))
# emp_id=[100,101,102,103]
# print(102 in emp_id)
# print(102 not in emp_id)
# emp_id= [100,101,102,103]
# emp_id1=[100,101,102,103]
# print("is both list are same?:",emp_id == emp_id1)


# list1=[5,2,3]
# list2=[5,8,3]
# print(list1 < list2) # it can check only first vlues of both list
# print("is both list are same?:",emp_id == emp_id1)

# list1=[5,8,3]
# list2=[5,8,3]
# print("both list pointing to same object?",list1 is list2)
# modifying original list
# emp_name=['abhiram','aswin','amit','Bhavya']
# emp_name.append('Gopika')
# print(emp_name)
# emp_name.insert(0,'amar')
# print(emp_name)
# emp_name.insert(3,'Alfin')
# print(emp_name)

# emp_name=['abhiram','aswin','amit','Bhavya']
# # print(emp_name)
# # # emp_name.clear()
# # # print(emp_name)
# # emp_name.remove('aswin')
# print(emp_name)
#pop() --> it returns the deleted values
emp_name=['abhiram','aswin','amit','Bhavya']
# emp_name.pop()
# print(emp_name)
# emp_name.pop(0)
# print(emp_name)
# removed_values=emp_name.pop(1)
# print("removed_value:",removed_values)
# print(emp_name)
matrix=[
    ['a','b','c'],# Row 0
    ['d','e','f'], # Row 1
    ['g','h','i']  # Row 2
]
# matrix.remove(['g','h','i'])
# print(matrix)
# matrix.pop()
# print(matrix)
# matrix.remove('e')
# print(matrix)
# matrix[1].remove('e')
# print(matrix)
#POP
# m_removed=matrix[-1].pop(0)
# print(m_removed)
# matrix[0].pop()
# print(matrix)
#update the List -->if you not provide any index , the whole list will be overwritten
customer_Details=['kumar','raju','lakshmi','mariyam']
# customer_Details='Kiran'
# customer_Details[3]='kiran'
# print(type(customer_Details))
#Sorting
# letters=['b','d','c','a','i']
# letters.sort()
# print(letters)
# Reverse
# letters=['b','d','c','a','i']
# letters.sort(reverse=True)
# print(letters)
#sorted()->do not change any original list
# letters=['c','a','b']
# # n_list=sorted(letters)
# n_list=sorted(letters,reverse=True)
# print("sorted list:",n_list)
# print("Original List:",letters)
#reversed()
# letters=['c','a','b']
# n_list= list(reversed(letters))
# print("ORIGINAL_LIST",letters)
# print("REVERSED_LIST",n_list)
# print(type(n_list))
# --sort()--asc
# --sort(reverse=True)-desc
# --sorted()keep original data same
# --reverse()
# --reversed()

#COPYING
# customers=['mural','ramu','kiran','vinay','vimal']
# customers_copy=customers
# print("original:",customers_copy)
# print("copy:",customers_copy)
# copy()
# customers=['mural','ramu','kiran','vinay','vimal']
# customers_copy=customers.copy()
# # customers.pop(0)
# customers_copy.append("mythri")
# print("original:",customers)
# print("copy:",customers_copy)
# matrix=[
#     ['a','b'],  # Row 0
#     ['c','d']  # Row 1
# ]
# matrix_copy=matrix.copy()
# # matrix.pop()
# matrix_copy[0].append('z')
# print("original:",matrix)
# print("copy:",matrix_copy)
# # print(id(matrix),id(matrix_copy))
# Deepercopy --> copy.deepcopy() crerates a true, independent copy for all levels

# matrix=[
#     ['a','b'],  # Row 0
#     ['c','d']  # Row 1
# ]
# matrix_copy=copy.deepcopy(matrix)
# # matrix.pop()
# matrix_copy[0].append('z')
# print("original:",matrix)
# print("copy:",matrix_copy)
#print(id(matrix),id(matrix_copy))
# is -- operator which is used to check the variables pointing to same object or not  in the memory area
# matrix=[
#     ['a','b'],
#     ['c,''d']
# ]
# #assignment
# a_matrix_c=matrix
# print("same object?",matrix is a_matrix_c,'\n' )
#
# #shallow copy
# s_matrix_c=matrix.copy()
# print("same object?",matrix is s_matrix_c,'\n' )
#
# #Deep Copy
# d_matrix_c=copy.deepcopy(matrix)
# print("same object?",matrix is d_matrix_c,'\n' )

# Combine the list
# lestter=['a','b','c']
# numbers=[1,2,3]
#
# filnal_list=lestter + numbers
# print(filnal_list)
# # print(lestter * 2)

# by using extend()
# letter=['a','b','c']
# numbers=[1,2,3]
# numbers.extend(letter)
# letter.extend(numbers)
# print(letter) #['a', 'b', 'c', 1, 2, 3]
# print(letter * 2)
# numbers=[numbers,letter]
# print(numbers)  #[['a', 'b', 'c'],[ 1, 2, 3]]
# by using Zip() --. it acts as iterator (zip object)
# letter=['a','b','c',] # if any list not having pair python stops making pairing , shortest list
# numbers=[1,2,3,4]
# final_list=zip(letter,numbers)
# final_list=list(zip(letter,numbers))
# final_list=list(zip(letter,numbers,'Hi')) # pairing with string values
# print(final_list)

# ids= [101,102,103]
# names =['abhiram','aswin','amit']
# print(list(zip(ids,names)))
#Iterator

# ids=[101,102,103]
# for id in ids:
#     print(id)

# customer_name=['amit','raju','','kiran']
#
# transformation_customer=[]
# for letter in customer_name:
#     transformation_customer.append(letter.capitalize())
# print(transformation_customer)

#enumerate --> which is used to fetch list along ith index values (enumerate object) , by using enumerate we can find exact position of bad data in your list
# customer_name=['amit','raju','','kiran']
# print(list(enumerate(customer_name))) #[(0, 'amit'), (1, 'raju'), (2, ''), (3, 'kiran')]
# print(list(enumerate(customer_name,start = 1))) #[(1, 'amit'), (2, 'raju'), (3, ''), (4, 'kiran')]
# customer_name=['amit','raju','','kiran']
# for index,value in enumerate(customer_name,start=1):
#     print(index,value)

#reverse
# customer_name=['amit','raju','','kiran']
# for customer in reversed(customer_name):
#     print(customer)

# combine two list
# customer_name=['amit','raju','kiran']
# customer_id=[101,102,103]
# # print(list(zip(customer_id,customer_name)))
# for customer,id in zip(customer_name,customer_id):
#     print(customer,id)


#map() --> object type , map is fast,clean way to do data transformations
# customer_name=['amit','raju','kiran']
# print(list(map(str.capitalize,customer_name)))
# id=[101,102,103]
# print(list(map(int,id)))

# customer_name=['  raju','  kiran','mythri  ']
# print(customer_name)
# for name in map(str.strip,customer_name):
#     print(name)

# filter the data by using filter(function,Iterable).
# removes all falsy values like, 0,"",or false  0="" false
#clean up the list by removing invalid data
# letters=['a','','b',None,'c',False]
# print(list(filter(None,letters)))
# letters=['a','','b',None,'c',False]
# print(list(filter(bool,letters)))
# customer_name=['amit','101','raju','102','kiran','103']
# # print(list(filter(str.isalpha,items)))
# for item in filter(str.isalpha, customer_name):
#     print(item)

                        #TUPLE( )
        #    -> its an ordered, immutable sequence type
        # ->fixed size records exampl:(x, y) date(year,month,day)
# how to create tuple
# id=(101,102,103)
# print(id[0])
# id1=1,2,3 # alterantive method to create tuple
# print(type(id))
# print(type(id1))
# num=1 #not a tuple
# print(type(num))

# numbers=(40) #not a tuple
# print(type(numbers))
# numbers1=(40,) #valid single value tuple
# print(type(numbers1))
# e=() #tuple type variable (empty tuple)
# print(type(e))
#you cannot add or revoe or replace elements:TypeError: 'tuple' object does not support item assignment

# immutability is shallow:if a tuple contains a mutable object(list), that inner object can be change
# id=([101,102],103)
# print(type(id))
# id[0].append(100)
# # print(id[0],id[1])
# print(id)
#core operations indexing and slicing
# id=(100,101,102,103,103)
# customer=('ramu','raju','mani')
# print(id[1],id[-1],customer[1])
# print(id[1:3])
# print((1,2) + (3,4))
# print(id + customer)
# print(id * 3)
#membership
# print('ramu' in customer)
#iterations
# for customers in customer:
#     print(customers)

# pair=(10,20,'a') #packing
# x,y,z=pair #unpacking
#
# print(x,y,z)

# id=(100,101,102,103,103)
# for i,value in enumerate(id, start=1):
#     print(i,value)

# built-in functions
# id = (100,102,104, 103,106,101)
# print("lenght:",len(id))# len() --> find out the length
# print(min(id))# min() --> whats min value
# print(max(id))# max()--> max value
# print(sum(id))# sum() --> sum of all the values
# print(sorted(id))# sorted() --> return in the form of list is sorted
# all() -->t/f
# any()-->t/f
# tuple(set(t_name)) --> remove duplicates

#tuple methods==>
id = (100,102,104, 103,106,101,103)
# print(id.count(103)) # it is used to count perticular element how many time got repeated
# print(id.index(102)) #it is used to find the index of given element , if the tuple contains any duplicates it return the first occurence
# Tuples: whenever fixed size, fixed meaning(records),hashable keys,
# list: if you want  to modify anything at any time
#tuples are very fast access and smaller memory needed , because its no need of resizing
                    #dictionary
        # it is mutbale ,unordered.
        # we need to work with key -> value pair
        # key must be hashable (immutable type like, str,int,float,tuple of immutable)
        #value can be any python object
employee = {"id":101,"Name":"Murali","Dept":"IT","Skills":["SQL","PYTHON","DEVOPS"]}

# Why dict:

# --> fast lookup:
# --> structured data:json from API,
# --> counting & grouping:frequency of tables
# -->join- like tasks :

# how to create dictionarie:
# d1={"a":1,"b":2,"c":3}
#dict() constructor -- able to create dictionaries
# print(type(d1))
# d2=dict(a=1,b=2,c=3)
# print(type(d2))
# d3=dict(zip(["a","b"],[1,2,3])) #from two lists
# print(type(d3))
# d4=dict([("a",1),("b",2)]) #from list of tuples
# print(type(d4))
#empty dic
# d5={}
# d5["a"]=1
# print(d5)
# print(type(d5))
#it allows number of values for single key
# d6=dict.fromkeys(["a","b","c"],1)
# print(d6)
# print(type(d6))
#nested
# schema={
#     "customer":{"id":"int","Name":"string","age":"int"},
#     "transactions":{"tid":"int","amount":"float"}
# }
# print(type(schema))
# print(schema)
# print(type(schema["customer"]))

#accessing and updating

# student={"name":"raju","age":12}
# print(student["age"])
# print(student.get("name"))

# student["age"]=21 #insert
# print(student["age"])
# student.update({"city":"chennai","grade":"A+"}) #update
# print(student)
#Remove
# student.pop("grade")
# print(student)
# del student["city"]
# print(student)
# key,va =student.popitem()
# print("popitem:",key,va)
# print(student)
#membership
# print("grade" in student)
# print("grade" not in student)
# d={"name":"ramu","age":20}
# print(len(d))
# students={'name': 'raju', 'age': 21, 'city': 'chennai', 'grade': 'A+'}
# for student in students:
#     print(student) #it returns only the keys inside your dictionary
# print(students.keys())  #this is same as for loop
# for value in students.values(): # this return the values inside the dict
#     print(value)
# for key,val in students.items(): # it will return key and values at single time as iteration
#     print(key,val)
# Sorted by key
# for key in sorted(students):
#     print(key,students[key])

# for key,val in sorted(students.items()):
#     print(key,val)

# print("before clear\n",students)
# students.clear()
# print("after clear ",students)
#copy
#shallow copy
# students={'name': 'raju', 'age': 21, 'city': 'chennai', 'grade': 'A+'}
# stdent_backup=students
#student_backup=students.copy()
# print("original dict",students)
# students["name"]="kiran"
# print("backup_student",stdent_backup)

# deepcopy

# students={'name': 'raju', 'age': 21, 'city': 'chennai', 'grade': 'A+'}
# c_student = copy.deepcopy(students)
# # print(students)
# students["age"]=12 #updating original dict
# print(c_student) #copied dic
# print(students)
                            #SET
                # * unordered..not supported indexing and slicing
                # * not allowed duplicate
                # create empty set,set()
                # mutable -> you can add/ remove elements
                # add(),update(),pop(),clear()
# employee={101,'kumar',30,'hyd',101}
# print(employee)
# #removes duplicates automatically
# s1=set([1,2,2,3,3])
# print(s1)
# fruit=set("banana")
# print(fruit)
# number={1,3,4}
# number.add(5)
# print(number)
# number.remove(3)
# print(number)
# p_element=number.pop()
# print(p_element)
# print(number)
#make an immutable set : as dict key , a member of another set
# frozenset()-> by using this method we will be able to make this set as immutable


# employee={101,'kumar',30,'hyd',101}
# frozen_set=frozenset(employee)
# frozen_set.add('kiran@gmail.com')
# print(employee)
# employee=[101,101,102,102,103,104]
# unique_emp_ids= set(employee)
# print(unique_emp_ids)
# print(type(employee))
# print(type(unique_emp_ids))
# cities=['mumbai','chennai','hyd','chennai','mumbai']
# unq_cities= set(cities)
# print(unq_cities)

# 1.union (combine all unique elements from both sets ->eliminates duplicates automatically
#     |, union()
# a={1,2,3}
# b={3,4,5}
# # print(a | b)
# print(a.union(b))
# web_users={100,101,102,103}
# app_users={103,104,105,102}
# all_user=web_users | app_users
# print(all_user)
# 2.intersection (get common elements which are present in the both sets)
# & , intersection()
# A={1,2,3,4}
# B={3,4,5,6}
# print(A & B)
# print(A.intersection(B))
# web_users={100,101,102,103}
# app_users={103,104,105,102}
# print(web_users.intersection(app_users))
# 3.difference(A-B,difference()) get the elements that are in A but not in B
# A={1,2,3,4}
# B={3,4,5,6}
# print(A - B)
# # A-b int equal to B-A
# print(B- A)
# comparisions
# issubset()
# issuperset()
# isdisjoint()

# issubset()-> check whether all elements one set aer presented in another set it return True/False

# A={1,2,3}
# B={1,2,3,4,5}
#
# print(A.issubset(B))
# print(B.issubset(A))
# expected_cols={'id','name','salary'}
# incmoing_cols={'id','name','salary','dept'}
# if expected_cols.issubset(incmoing_cols):
#     print("all required columns are present")
# else:
#     print("some columns are missing")

# issuperset()->checks one set contains all elements of another set
# A={1,2,3,4,5}
# B={2,3}
#
# print(A.issuperset(B)) # A is  a superset of B because A contains everything in B
# print(B.issuperset(A))

# 3.isdisjoint()-->checks whether two sets have no common element  true-> if A and B sharing nothing in common ,
# if both have overlap at all
# A={1,2,3,}
# B={4,5,6}
# C={3,5,7}
# # print(A.isdisjoint(B)) true
# print(A.isdisjoint(C)) # False

# A lambda expression in Python, also known as a lambda function,
# is a small, anonymous (nameless) function that can contain only a single expression.
# It is defined using the lambda keyword.

# multiple=lambda X:X*2
# print(multiple(2))
# When a lambda has two parameters, you must pass two values when you are calling
# add=lambda X,Y:X+Y
# print(add(10,220))
# a lambda can contains any expressions , include conditions also

# check=lambda i:i in "python" # n in "python"
# print(check('l'))

# lambda with map (data transformation)
# price=['$12.50','$9.90','$100.0'] #map(function,iterable )
# print(list(map(lambda p:float(p.replace('$','')),price)))

#lambda with filet
# remove all the prices lower than 100
# price=[120,30,300,80]
# print(list(filter(lambda p:p>=100,price)))
# i want to print who are getting marks >70
# i want to print whos name starts with M
#matrix iteration happen one row at a time
# students=[
#     ['maria',85], #Row 0
#     ['kumar',90], #row 1
#     ['mythri',60] #row 2
# ]
# # print(list(filter(lambda row:row[1]>70,students)))
#
# print(list(filter(lambda row:row[0].startswith('m'),students)))









