#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
user_input=int(input("enter number"))
output=lambda output: user_input + 25
print(output(user_input))