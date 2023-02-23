from my_functions import calculate
from my_functions import remove_odd
from input_helper import get_number


print('Hello world!')

numb1 = get_number()
numb2 = get_number()
operation = input("Operation: ")

print("Result: " + calculate(numb1, numb2, operation).__str__())

my_list = []
print('\nEntering elements. Enter 999 to stop')

while True:
    numb = get_number()

    if numb == 999:
        break

    my_list.append(numb)

print('\nEntire list: ' + my_list.__str__())
print('Even items: ' + remove_odd(my_list).__str__())
