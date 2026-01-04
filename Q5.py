#Find duplicate elements in a list

def find_duplicates(lst):
    unique = []
    duplicates = []
    for item in lst:
        if item in unique:
            duplicates.add(item)
        else:
            unique.add(item)
    return list(duplicates)
print(find_duplicates([1,2,3,2,4,5,1]))
# Output: [1, 2]
