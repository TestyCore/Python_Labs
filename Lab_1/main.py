from my_functions import calculate
from input_helper import get_number


print('Hello world!')

numb1 = get_number()
numb2 = get_number()
operation = input("Operation: ")

print("Result: " + calculate(numb1, numb2, operation).__str__())
