'''
Jacob Corbley
Project Range
'''
from time import *
from math import *
from sys import *
again = True
print("with this program, you can:\n\n")
sleep(1)
while again == True:
    again = False
    print("a. pick a starting value")
    sleep(.5)
    print("b. pick an ending value")
    sleep(.5)
    print("c. pick an increment value\n")
    print("\nin turn, this will display a series of numbers, according to your choices\n")

    start = int(input("starting value:"))
    end = int(input("ending value:"))
    increment = int(input("incremental value:"))

    for x in range(start,end,increment):
        print(x, end = " ")
    aYN = True
    while aYN == True:
        aYN = False
        print("\nWant to go again?")
        again = input("y or yes, n or no: ")
        if again == ("y" or "yes"):
            again = True
        elif again == ("n" or "no"):
            exit( )
        else:
            print("it\'s y, yes, n or no: ")
            aYN = True
