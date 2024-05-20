
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg is:",sum/3)
    


#         s1 = Student("laxman", [98, 83, 95])
#         s1.get_avg()


# class Account:
#     def __init__(self,bal, acc):
#         self.balance= bal
#         self.account_No=acc


#         #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "is debited")
#         print("Total balance=", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "is credit")
#         print("Total balance=", self.get_balance())

#     def get_balance(self):
#         return self.balance    


# acc1= Account(10000, 123456789)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(50000)
# acc1.debit(20000)



# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7)* self.radius **2  

#     def perimeter(self):
#         return 2 * (22/7) * self.radius 



# c1=Circle(21)
# print(c1.area())
# print(c1.perimeter())




# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary



#     def showDetails(self):
#         print("role=", self.role)   
#         print("dept=", self.dept)   
#         print("salary=", self.salary)   


# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#         super().__init__('Engineer', "IT", "75,000")


# eng1 = Engineer("laxman", 22)
# eng1.showDetails()


class Order:
    def __init__(self, item, price):
        self.items = item
        self.price = price
    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 = Order("Iphone", 150000)  
odr2 = Order("Mt-15", 400000)      

print(odr1 > odr2)