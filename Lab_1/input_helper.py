def get_number():
    while True:
        numb = input("Number: ")

        try:
            numb = int(numb)
            break
        except ValueError:
            try:
                numb = float(numb)
                break
            except ValueError:
                print("Invalid input...")

    return numb
