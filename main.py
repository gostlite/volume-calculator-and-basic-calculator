import argparse
import math

parse = argparse.ArgumentParser(prog="Calculator", description= "The calculator")
parse.add_argument("-f","--first", metavar="", required=True,type=int, help="Put in a sirst digit")
parse.add_argument("-s","--sign", metavar="", required=True, help="put in an operator: *+/-, or use 'v' to calculate volume")
parse.add_argument("-l","--last", metavar="", required=True, type=int, help="put in the last num")
args = parse.parse_args()

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a /b 

def calc_volume(radius, height):
    return math.pi * (radius ** 2) * height

def calculate():
    if args.sign == "v":
        return "The result for your volume calculation is: {:.2f}".format(calc_volume(args.first, args.last))
    elif args.sign == "+":
        return f"The result for your addition calculation is: {add(args.first, args.last)}"
    elif args.sign == "-":
        return f"The result for your subtraction calculation is: {sub(args.first, args.last)}"
    elif args.sign == "*":
        return f"The result for your multiplication calculation is: {mul(args.first, args.last)}"
    elif args.sign == "/":
        return (f"The result for your division calculation is {div(args.first, args.last): .02f}")
    else:
        return "Please check --help on how to use the program"
if __name__ == "__main__":
    print(calculate())
