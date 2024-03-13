import math
#defining exponentiate to include 2 ints as arguments

#NEED MATHPOW
def exponentiate(num1, num2):
    return math.pow(num1, num2)

#defining raise to 4th power;
def raise_to_the_fourth_power(given_number):
    return exponentiate(given_number, 4)

    # creating variables with lambda function
square = lambda num: exponentiate(num,2)
cube = lambda num: exponentiate(num,3)

print(square(2))
print(cube(2))
print(raise_to_the_fourth_power(2))