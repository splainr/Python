# --------
# Date:        Aug 24 2021")
# Project:     Python Lab")
# Exercise:    python.land Tutorial: Functions")
# Learner:     Russell J. Splain")
# ---------
# print("")

# Use the keyword 'def' to fine a function, like so:  def MyFunction():
# def say_hi():
#    print('Hi!')
# say_hi()

# def say_hi(name):
#    print('Hi' , name)
# say_hi('Erik')

# This sequence demostrates the local scope of variable 'answer' withing the function say_hi(),
# and the global scope of variable 'name' defined outside of the function say_hi().
# The say_hi() function can call the global variable 'name', but the print(answer) global
# function cannot evaluate the variable 'answer' within function say_hi().
# def say_hi():
#    print("Hi" , name)
#    answer = "Hi"
 
# name = 'Erik'
# say_hi()
# print(answer)

# This sequence demostrates the function welcome(), containing the parameters 'name' and 'location'.
# The function welcome() is then given the arguments of 'Russell' and 'This tutorial.'
# The function is designed to print "Hi Russell welcome to this tutorial."

# def welcome(name, location):
#     print("Hi", name, "Welcome to", location)
# welcome('Russell', 'This tutorial.')

#
def welcome(name='learner', location='this tutorial.'):
     print("Hi", name, "welcome to", location)
 
welcome()
welcome(name='John')
welcome(location='this epic tutorial')
welcome(name='John', location='this epic tutorial')


