#EXERCISE 2
#defining greet function
#printing custom greeting with name_input variable
def greet(name_input):
    print("Hello " + name_input + "!")
name_input = input("Please enter your name. ")

#I still don't understand why this is necessary (it IS necessary, the logic isn't intuitive yet)
greet("Nathan Eckel")
greet("Darth Vader")
greet("Guido van Rossum")

#list of name2 name3 myname
myname = "Nathan Eckel"
name3 = "Darth Vader"
name2 = "Guido van Rossum"

#ForLoop with my counter added just b/c I like putting a counter in here
for i in range(501):
    greet(name_input + " " + myname + " " + name2 + " " + name3 + " " + str(i))