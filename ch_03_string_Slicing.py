# String Slicing --> TUkade karna String ke

greeting = "Good Morning, "

name = "Milind"
print(type(name))
c = greeting  +  name  #Concatenation in Two Strings (+) sybol is used
print(c)

# The indexing is start from 0 to (length - 1)

name = "Milind"
print(name[0])
print(name[2])
print(name[5])

# name[3]= "l"  --> does not work we can not change it as

print(name[0:3])  # In this case the 3 rd index is not conclude it print only 2nd index

print(name[1:5])  # String slicing means hum String ke tukade kar sakate hai

print(name[:4])    # Min index replace kar dega (is same as [0:4]) 

print(name[0:])    # is same as [0:6]     (length ki string aa jayegi)


# Negative Indexes

# M     i      l      i      n    d 
# 0     1      2      3      4    5        
#(-6)  (-5)   (-4)   (-3)   (-2)  (-1)        Negative Indexing

d = name[-4:-1]   # is same as [2:4]
print(d)


# Slicing with skip value

e = name[0::2]
print(e)