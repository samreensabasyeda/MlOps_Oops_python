str = "samreen"
print(len(str))
print(str[1])

# slicing -- accessing a range of characters in a string
print(str[2:5])
print(str[ :4])
print(str[1:])

#backward slicing
print(str[-4:-1])

#string functions 
#1.ends with
str1 = "I am learning python, it is easy"
print(str1.endswith("sy"))
# 2. starts with
print(str1.startswith("I"))
#3 capitalize
print(str1.capitalize())
#or
str2 = str1.capitalize()
print(str2)
# replace function
str3 = str1.replace("am", "was")
print(str3)
#4 find function
print(str1.find("python"))
#5 lower function
print(str1.lower())
#6 COunt function
print(str1.count("a"))


# WAP to input ur name and print the length of ur name
name = input("Enter ur name : ")
print("Length of ur name is : ", len(name))