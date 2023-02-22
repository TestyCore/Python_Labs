def calculate(numb1, numb2, op):
    if op == "+":
        result = numb1 + numb2
    elif op == "-":
        result = numb1 - numb2
    elif op == "*":
        result = numb1 * numb2
    elif op == "/" and numb2 != 0:
        result = numb1 / numb2
    elif op == "/" and numb2 == 0:
        result = "Cannot divide by zero"
    else:
        result = "Invalid operation"

    return result