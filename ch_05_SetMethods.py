# Creating an empty set

b = set()
print(type(b))


# Adding values to an empty set
b.add(4)
b.add(4)
b.add(6)      # Adding a value repetatively does not changes a set
b.add(6)
# b.add([4,5,6])  # We can not add a List in the Set

b.add((4,5,6))    # We can add a tuple in the set

# b.add({4:5})    # We can not add a Dictionary in the 

print(b)

# length of the set
print(len(b))    # Prints the length of the sets


# Removal of an item
b.remove(6)      # Removes 6 from the set b
# b.remove(5)      # Throws an error while trying to remove 5(Which is not present in the set)
print(b)


b.pop(4)
print(b)



# Properties of Sets

# 1. unordered
# 2. unindexed
# 3. There is no way to change items in the set
# 4. Sets cannot contain duplicate values