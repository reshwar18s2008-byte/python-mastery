my_str="Hello, World!"
print("dr" in my_str)
print("Hello" in my_str)
print(my_str[0])
print(my_str[9])

name="john doe"
age=26
name_and_age=name
name_and_age+=str(age)
print(name_and_age)

#F-strings start with f (either lowercase or uppercase) before the quotes, and allow you to 
# embed variables or expressions inside replacement 
# fields indicated by curly braces ({}). Here's an example:
 
print(f"my name {name} and my age is {age}")
print(my_str[0:5])
print(my_str[8:])
