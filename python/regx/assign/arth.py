import sys
import os
def sum(num1, num2):
    num3= num1 + num2
    return num3
def diffe(num1, num2):
    num3= num1 - num2
    return num3
def product(num1, num2):
    num3= num1 * num2
    return num3
def qu(num1, num2):
    num3= num1 // num2
    return num3
op=sys.argv[1]

anum= int(os.getenv("a")) 
bnum= int(os.getenv("b"))
if op == "sum":
    print(sum(anum, bnum))
if op == "diff":
    print(diffe(anum, bnum))
if op == "pro":
    print(product(anum, bnum))
if op == "quo":
    print(qu(anum, bnum))