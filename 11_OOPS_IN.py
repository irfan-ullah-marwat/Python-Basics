# class Student : 
#     name = "irfan"
    
# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)



# class Car :
#     module = "BMW"
#     colour = "BLACK"


# s1 = Car()
# print(s1.module)

# s2 = Car()
# print(s2.colour)


# Constructor (init)

#Constructor runs when an object is created

# class Student:
#     college_name = "ABC School"

#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print("Adding new student in database")

#     def welcome(self):
#         print("Welcome student", self.name)

#     def get_marks(self):
#         return self.marks


# s1 = Student("Irfan", 98)
# print(s1.name, s1.marks)
# print(Student.college_name)

# s2 = Student("Farman", 97)
# print(s2.name, s2.marks)
# print(s2.college_name)
# s2.welcome()
# print(s2.get_marks())



# lets practice  


# create student class that takes name and marks of three subjects as a argument 
# in constructors. then careat a method to print the average

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         total = 0
#         for val in self.marks:
#             total += val
#         print("Hi", self.name, "your average score is", total / len(self.marks))


# s1 = Student("Tony Stark", [99, 98, 97])
# s1.name = "Ironman"
# s1.get_avg()




# class Account:
#     def __init__(self,bal,account):
#         self.balance = bal
#         self.account_no = account

#     def debit(self,amount):
#         self.balance -=amount
#         print("RS.",amount,"was debit")
#         print("total balanced=",self.get_balance())

#     def credit(self,amount):
#         self.balance +=amount
#         print("RS.",amount," was credit")
#         print("total balanced=",self.get_balance())


#     def get_balance(self):
#         return self.balance
    
    
# acc1 = Account(10000, 2345)
# acc1.debit(1000)
# acc1.credit(500)

        

       


# del keyword used to delet object properties or object itself
        #del s1.name




      


