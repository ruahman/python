# Tuples are unchangeable, meaning that you cannot change, add, or remove items after the tuple has been created.
mytuple = ("apple", "banana", "cherry")

# unpack a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# rest of the items
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
