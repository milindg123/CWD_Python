myDict = {
  "pankha" : "Fan",
  "Manjar" : "cat",
  "Kutra"  : "Dog"
}
print("Options are",myDict.keys())
a = input("Enter the marathi word\n")

print("The meaning of your word is : ", myDict[a])

# Below line does not give an error if the word is not present in the dictionary

print("The meaning of your word is : ", myDict.get(a))