import math

# class Str:
#     def getString(self):
#         self.text = input("Enter a string: ")

#     def printString(self):
#         print(self.text.upper())

# obj = Str()
# obj.getString()
# obj.printString()

# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
# a = int(input())

# shape = Shape()
# print("Shape area:", shape.area())

# square = Square(a)
# print("Square area:", square.area())

# class Shape:
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# a, b = int(input()), int(input())

# shape = Shape()
# print("Shape area:", shape.area())

# rectangle = Rectangle(a, b)
# print("Rectangle area:", rectangle.area())

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Point coordinates: ({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y

#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# x1 = int(input("Enter x-coordinate of first point: "))
# y1 = int(input("Enter y-coordinate of first point: "))
# x2 = int(input("Enter x-coordinate of second point: "))
# y2 = int(input("Enter y-coordinate of second point: "))

# p1 = Point(x1, y1)
# p2 = Point(x2, y2)

# p1.show()
# p2.show()
# print("Distance:", p1.dist(p2))

# new_x = int(input("Enter new x-coordinate for first point: "))
# new_y = int(input("Enter new y-coordinate for first point: "))
# p1.move(new_x, new_y)
# p1.show()


# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")

# owner_name = input("Enter account owner's name: ")
# initial_balance = int(input("Enter initial balance: "))

# account = Account(owner_name, initial_balance)

# deposit_amount = int(input("Enter deposit amount: "))
# account.deposit(deposit_amount)

# withdraw_amount = int(input("Enter withdrawal amount: "))
# account.withdraw(withdraw_amount)

# withdraw_amount = int(input("Enter another withdrawal amount: "))
# account.withdraw(withdraw_amount)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# numbers = input("Enter numbers separated by spaces: ").split()
# numbers = [int(num) for num in numbers]

# prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# print("Prime numbers:", prime_numbers)

