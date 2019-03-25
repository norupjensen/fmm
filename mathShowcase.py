from math_helpers import *

greeting = "Welcome to the mathTool"

print("{}".format(greeting))
userInput = ""
userGreeter = "Enter an even number, larger than 2, I will try to represent it\
as the sum of two primes:"
print(userGreeter)
while userInput !="x":
    userInput = goldbach()
