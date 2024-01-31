import sys

def add(num1, num2):
    add = num1+num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    mul = num1*num2
    return mul

def div(num1, num2):
    div = num1/num2
    return div

def rem(num1, num2):
    reminder = num1%num2
    return reminder

num1 = int(sys.argv[1])
operand = sys.argv[2]
num2 = int(sys.argv[3])

if operand == "add":
    output = add(num1, num2)
    print(output)

if operand == "sub":
    output = sub(num1, num2)
    print(output)
if operand == "mul":
    output = mul(num1, num2)
    print(output)

if operand == "div":
    output = div(num1, num2)
    print(output)

if operand == "reminder":
    output = rem(num1, num2)
    print(output)