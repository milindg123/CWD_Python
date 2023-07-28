# Dictionary -> Key-value pair

myDict = {
  "Fast" : "In a quick manner",
  "Milind": "A Coder",
  "Marks" : [1,3,4,5],
  "anotherdict":{'Milind':"Player"}

}
print(myDict["Fast"])
print(myDict["Milind"])
print(myDict["Marks"])
print(myDict['anotherdict']['Milind'])


# Properties of Dictionary

# 1.unordered
# 2.mutable
# 3.indexed
# 4.cannot contain duplicate keys



# ******************  SameType practice Example ************************************

myDict['Marks'] = [45,70]
print(myDict['Marks'])
print(myDict['anotherdict']['Milind'])


MayurDict = {
    "SoftSkill" : "Communication",
    "Subject" : "DBMS",
    "Language" : "Java",
    "SomeoneDict":{"Language":"Python"}
}

print(MayurDict["SomeoneDict"]["Language"])


