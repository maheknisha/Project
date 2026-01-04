#Explain try-except in Python
n=int(input("Enter any number : "))
try:#Try block contain code to monitor exceptions
    print(n%0)
except ZeroDivisionError:#Except block execute block of code to handle the exceptions
    print("cannot be divided by zero")