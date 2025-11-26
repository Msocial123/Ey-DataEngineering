# OOPS(Object oriented programing)
# from pandas.core.interchange.dataframe_protocol import DataFrame
# from pandas.io.clipboard import clipboard_set
import re

# Class and Object
# A class is a Blueprint or template for creating object --> contains Attributes(Variables/data), Methods (functions) -> describe the behaviour of the object
# an Object is an instance of class (enty), physical existance -> with a single class we can crete number of Objects
# class Class_name:-- class
#
# Class_name() -- object
# reference variable -> which can be stored the details available in the object
# class Employee:
#     def __init__(self,name,role,salary):
#         self.name=name
#         self.role=role
#         self.salary=salary
#
#     def print_details(self):
#         print(f"name:{self.name},Role:{self.role},salary:{self.salary}")
#
# emp1=Employee("Kumar","IT",10000)
# emp2=Employee("Kiran","Hr",5000)
# emp1.print_details()
# # emp2.print_details()
# print("details of object emp1",id(emp1))
# # print("details of object emp2",id(emp2))

#self is known as referece variable ,which is always pointg to current object
#within the python class, to access current object, we can use self
#the first argument is always self to the constructor,
#the first argument is always self to the methods ,
# PVM is always responisible to pass arguments to the self
#we can use self always with in the class only
# inside constructor we can use self to declare object related variables(instance variables)
# inside instance methods , we can use self to access the values of instance variables

# constructor will automaticall call without using any referenced variable/object(explicit call not required )
# class Student:
#     company_name = 'ey'
#     def __init__(self):
#         self.name="murali"
#         print("i am inint constructor ")
#         print(self.name)
#
#     def show(self):
#         print("i am from show() method")
#
# s1=Student()
# s1.show()
# print(s1.company_name)

# types of variables:
# 1. instance variables
# the variables /attributes that belongs ti object individually , using with self.
# 2.class varibale,
# share among all objects of the class
#it will be defined outside of the methods but inside of a class

# class Employee:
#     company_name="Ey.com" #class variable
#     def __init__(self,name,department):
#         self.name=name #instance variables
#         self.dept=department
#         print(id(self))
#
# # emp1=Employee("Amith","IT")
# emp2=Employee("aswin","hr")
# # print(emp1.name)
# # print(id(emp1))
# print(emp2.name,emp2.dept,emp2.company_name)
# print(id(emp2))
#
# instance methods and class methods
# instanc methods operates on instance data
# it has self ass first parameter

# class Employee:
#     company_name="Ey.com" #class variable
#     def __init__(self,name,department):
#         self.name=name #instance variables
#         self.dept=department
#         # print(id(self))
#     def display(self):
#         print(self.name,self.dept)
#
# # emp1=Employee("Amith","IT")
# emp2=Employee("aswin","hr")
# emp2.display()
# # print(emp1.name)
# # print(id(emp1))
# # print(emp2.name,emp2.dept,emp2.company_name)
# # print(id(emp2))

# class method:
# IT OPERATES ON CLASS VARIABLES
# USE @classmethod decorator
# first parameter is cls

# class Employee:
#     company_name="Ey.com" #class variable
#     @classmethod
#     def display(cls,new_name):
#         cls.company_name=new_name
#         print(cls.company_name)
#
# cmp=Employee.display("gbs.ey.com")

# Static methods.
# IT doesnt  DEPEND ON ANY INSTANCE OR CLASS Data
# USES @staticmethod
#
# class Utility:
#     @staticmethod
#     def convert_salary_to_lakshs(salary):
#         return salary/100000
#
# print(Utility.convert_salary_to_lakshs(900000))

# Access Specifiers (can be defined with _)

# access specifiers is also known as access modifiers
#it defines how attributes and methods of a class can be accessed or modified outside of the class
# Connect to databs e;.. user name, password , host=

# -> protecting sensitive data configuration variables
# ->preventing accidental modification of critical methods
# -> clean structure and code should be reusable

# 1.public->  name="murali" -> anywhere
# 2.protected -> _name="murali" ->within class and sub class out side classs not accesasible directly
# 3.private--> __name="murali"-->inside class only.. you cannot access directly out of the class

# class Emp:
#     def __init__(self,name,salary):
#         self.name = name #public type
#         self.sal= salary #public type
#
# emp=Emp("murali",1000)
# print(emp.name) # accessible
# print(emp.sal) # accessible
# _source,_config_path,_status
# class DataPipeline:
#     def __init__(self):
#         self._source="S3 Bucket"  #protected variable
#         self._Process_status="pending" #protected variable
# class ETLpipeline(DataPipeline):
#     def procees_data(self):
#         print(f"procees_data from {self._source}")
#         self._Process_status="completed"
#
#
# etl= ETLpipeline()
# print(etl.procees_data())
# print(etl._Process_status)

# private

# class DatabaseConnection:
#     def __init__(self):
#         self.__db_password="Password@2025" #private
#         self.__connection_status="not connected "
#
#     def connect(self):
#         self.__connection_status="connected"
#         print("Database connected successfully")
#
# db=DatabaseConnection()
# db.connect()
# # print(db.__db_password) not acceptable because its having private accessspecifier
# print(db._DatabaseConnection__db_password) #not recommended
#
# Inheritance
# inheritance in OOP concept where a new class(child class or sub class ) derives
# properties and behaviours(attributes and methods ) from an existing class(super/parentclass/baseclass)

# it allows the code reusability, extendability,hierarchical classification of class

# importance:
#parentclass
# class DataSource:
#     def connect(self):
#         print("connecting to data sources.........")
#     def disconnect(self):
#         print("disconnecting from data sources.....")
# #child class
# class MySQLsource(DataSource):
#     def connect(self):
#         print("connecting to MySQL....")
#
# #creaate Object
# source=MySQLsource()
# source.connect() #child class method
# source.disconnect() # parent class method

# types of inheritances
# 1.single -->child is inherits only one parent  ,class child(parent)
# 2.multiple --> child inherits from multiple parents ,class child(parent1,parent2,)
# 3.multilevel-->inheritance through multiple levels ,
# 4.hierarchical -->multiple children inherit from one parent ,child1(parent1),child2(parent1)
# 5.hybrid -->combination of more than one type

# multiple inheritance
# class Logging:
#     def log(self,message):
#         print(f"LOG:{message}")
# class Datasource:
#     def connect(self):
#         print("connecting to data source")
#
# class MySQLSource(Logging, Datasource):
#     def run(self):
#         self.connect()
#         self.log("Connecting to MySQL successful")
# obj=MySQLSource()
# obj.run()

# multilevel
# class Datasource:
#     def connect(self):
#         print("connecting to data source...")
# class SQLSource(Datasource):
#     def run_query(self):
#         print("running SQL query....")
# class ETLPipeline(SQLSource):
#     def transformation_data(self):
#         print("transforming data....")
# etl=ETLPipeline()
# etl.connect()
# etl.run_query()
# etl.transformation_data()


# hierarchical

# class Datasource:
#     def connect(self):
#         print("connecting to data source...")
# class SQLSource(Datasource):
#     def run_query(self):
#         print("running SQL query....")
#
# class MongoSource(Datasource):
#     def mongo_query(self):
#         print("querying Mongo...")
#
# sql=SQLSource()
# mongo=MongoSource()
# sql.connect()
# sql.run_query()
# mongo.connect()
# mongo.mongo_query()


# Hybrid Inh
# class Base:
#     def show(self):
#         print("base class")
# class Datasource(Base):
#     def connect(self):
#         print("connecting to the datasource")
# class APIDatasource(Base):
#     def connect_api(self):
#         print("connecting to the api datasource")
# class UnifiedPipeline(Datasource,APIDatasource):
#     def run(self):
#         print("runing hybrid pipeline")
#
# pipeline = UnifiedPipeline()
# pipeline.show()
# pipeline.connect()
# pipeline.connect_api()
# pipeline.run()



# Polymorphism = many_forms
# polymorphism means many forms-> same function is going to work/behave  differently
# based on the object or dtatype is working with
# proceedata() --> csv,json,databsesource

# 1.compile time (overloading)->same methodname , different parameters. (def add(a,b,c=0))
# 2.runtime(overriding)  -->method in a child classs overrides method from parent class   class csvreader(filereads) overridde read_data()

# RUN-TIME OR METHOD OVERRIDING()
# WHEN CHILD CLASS DEFINES A METHOD WITH SAME NAME AS PARENT CLASS ,MODIFYING BEHAVIOUR


# class Datasource:
#     def read_data(self):
#         print("reading the data from generic source")
# class CSVSource(Datasource):
#     def read_data(self):
#         print("reading the data from CSV file....")
# class JSONSource(Datasource):
#     def read_data(self):
#         print("reading the data from JSON file....")
#
# # polymorphic behav
# sources=[CSVSource(),JSONSource(),Datasource()]
# for source in sources:
#     source.read_data()

#
# Method overloading (compile-timee poly)
# this concept not supported in python directly  as like java, c++
# we can achieve this concept by using default arguments
# class Dataprocessor:
#     def process(self,data=None,file_path=None):
#         if data is not None:
#             print("processing data in memory...")
#         elif file_path:
#             print(f"processing data from...{file_path}")
#         else:
#             print("no data source provided ")
# # class data(Dataprocessor):
# #     def process(self,data=None,file_path=None):
# #         print("chaild")
#
# dp=Dataprocessor()
# dp.process(data=[1,2,3,]) #processing the data into memory
# dp.process(file_path="data.csv") #SENDING FILE TO PROCESS
# dp.process() #NO DATA STORE IS PROVIDED

# class addNumbers():
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         sum = (self.a + self.b)
#         print("sum is ",sum)
#
#
# addNumbers()

import re
text = "Contact: alice@example.com or bob.smith@domain.co.in"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)


