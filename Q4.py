#Difference between exception and error
"""
Exception can be handled it occur during compilation time while error cannot be handled  it can be synatx error,logical error forgotting the bracket etc.
Exception handled through try-except keyword,error usually not handled"""
#Syntax error
n =int(input("enter a number"))
print(n
#Type error as trying to concatenate string with number
x ="hello"
y=1
print(x+y)
#Exception
n=[1,2,3,4]
print(n[0])
try: #error will occur if index is 10
    print(n[10])
except IndexException as e: #to handle error it will display error msg
    print("Index error",e)


