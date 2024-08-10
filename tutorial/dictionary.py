thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)

print(thisdict["brand"])

print(len(thisdict))

print(thisdict.keys())

print(thisdict.values())

print(thisdict.items())

if "model" in thisdict:
    print("key found")

for x in thisdict:
    print(x)
