# --------
# Date:        Sep 7 2021
# Project:     Python Lab
# Chapter:     Python Function: The Basics Of Code Reuse
# URL:         https://python.land/introduction-to-python/functions
# Exercise:    python.land Tutorial: 8. Default values and named parameters
# Learner:     Russell J. Splain
# ---------
print("")

def welcome(name='learner', location='this tutorial'):
     print("Hi", name, "Welcome to", location)

welcome()
print("")

welcome('Erik', 'your home')
