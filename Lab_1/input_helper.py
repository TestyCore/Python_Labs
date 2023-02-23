def get_number():

    while True:
        numb = input("Number: ")

        try:
            numb = float(numb)
            break
        except ValueError:
            print("Invalid input...")

    return numb
