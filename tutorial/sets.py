# Sets do not allow duplicate values
thisset = {"apple", "banana", "cherry", "apple"}
thisset.add("orange")

print(thisset)

thisset.remove("banana")
print(thisset)

# union sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
