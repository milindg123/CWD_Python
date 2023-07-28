myDict = {
  "Fast" : "In a quick manner",
  "Milind": "A Coder",
  "Marks" : [1,3,4,5],
  "anotherdict":{'Milind':"Player"},
  1 : 2
}

# Dictionary Methods

print(list(myDict.keys()))      # Prints the keys of the dictionary

print(myDict.values())    # Prints the values of the dictionary

print(myDict.items())     # Prints the (key, value) for all of the contents of the dictionary


print(myDict)
updateDict= {
  "Lovish":"Friend",
  "Mayuri":"Friend",
  "Milind": "A dancer"

}
myDict.update(updateDict)    # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)



print(myDict.get("Milind"))   # Prints value associated with key "Milind"
print(myDict["Milind"])       # Prints value associated with key "Milind"


# The Difference between .get and [] syntax in Dictionary ?

print(myDict.get("Milind2"))   # Returns None as Milind2 is not present in the dictionary
print(myDict["Milind2"])       # Throws an error as Milind2 is not present int the dictionary






