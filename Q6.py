#Remove duplicates while preserving order
original_list=[2,3,4,1,22,2,3]
new_list = []
for i in original_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

