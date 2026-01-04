
#Reverse a string without slicing
string = "Mahek"
reverse_str = "" #created an empty string
for i in string:
    reverse_str = i + reverse_str # m + ""="m", a + "m" ="am"
print(reverse_str)