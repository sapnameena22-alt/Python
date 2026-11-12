#lab 41
def add(x, y):
    """return the sum of two numbers."""
    print(x + y)

def subtract(x, y):
    """return the difference between two numbers."""
    print(x - y)    
def multiply(x, y):
    """return the product of two numbers."""
    print(x * y)

def divide(x, y):
        """return the quotient of two numbers. Raises ZeroDivisionError if the divisor is zero."""
        if y == 0:
            raise valueerror("cannot divide by zero.")
        print(x / y)

add(4,5)
subtract(4,5)
multiply(4,5)
divide(6,2)


#lab 42
#math module
import math 

#square root
print("square root of 25:", math.sqrt(25))

#factorial
print("square root of 5:", math.factorial(5))

#value of pi
print("value of pi:", math.pi)

#cosine of 45 degrees
print("cosine of 45 degrees:", math.cos(math.radians(45)))

#datewtime module
import datetime
#current date and time
now = datetime.datetime.now()
print("current date and time:", now)

#specific date
d = datetime.date(2024, 8, 24)
print("specific date:", d)

#difference between two dates
delta = now - datetime.datetime(2024, 1, 1)
print("days since january 1, 2024:", delta.days)

#formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("formatted daate and time:", formatted_date)

#OS module
import os

#current working directory
print("current working directory:", os.getcwd())

#create a new directory
os.makedirs('new_directory', exist_ok=True)
print("directory 'new_directory' created.")

#remove the directory
os.rmdir('new_directory')
print("Directory 'new_directory' removed.")

#sys module
import sys
#print python version
print("python version:", sys.version)

#print system platform
print("platform:", sys.platform)

#print command line arguments
print("command line arguments:", sys.argv)

#random module
import random
#random integer between 1 and 10
print("random integer between 1 and 10:", random.randint(1, 10))

#floating-point number between 0 and 1
print("random float between 0 and 1:", random.random())

#choice from a list 
items = ['apple', 'banana', 'cherry']
print("random choice from list:", random.choice(items))

#lab 43
#arithmetic operation
def add(x, y):
    """return the sum of two numbers."""
    print(x + y)

def subtract(x, y):
    """return the difference between two numbers."""
    print(x - y) 
    
def multiply(x, y):
    """return the product of two numbers."""
    print(x * y)

def divide(x, y):
        """return the quotient of two numbers. Raises ZeroDivisionError if the divisor is zero."""
        if y == 0:
            raise valueerror("cannot divide by zero.")
        print(x / y)

add(3,5)
subtract(3,5)
multiply(3,5)
divide(8,2)


#input two numbers to perform the oeration
def main():
    print("simple calculator")
    print("delect operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
#get user choice
choice = input("enter choice (1/2/3/4):")
#get user input for numbers
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
#perform the chosen operation
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
     print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
     print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("invaild input ! please select a vaild operation.")


#disply the result of the oprtation
if'__name__' =="__main__":
   main()




















