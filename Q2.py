# Count frequency of characters in a string
name = input("Enter a Name:")
string = {}
for i in name:
    if i == " ": #ignore spaces
       continue
    if i not in string:
       string[i] = 1
    else:
        string[i]+=1
print(string)
        
    