# Question No. 1

name = input("Enter the name: ")
# b = "Good Aftenoon"

# print(name,b)   

print("Good Afternoon, ", name)


# Question No. 2

letter = '''Dear <|NAME|>,
You are Selected ! 

Date: <|DATE|>'''

name = input("Enter your name : \n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)


print(letter)