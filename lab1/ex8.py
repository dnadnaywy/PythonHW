def numberOfBits():
    number = input("A number, please: ")
    contor = 0
    if number.isdigit():
        number = int(number)
        binary_number = bin(number)
        for char in binary_number:
            if (char == "1"):
                contor = contor + 1
        print("Your number in binary format is: " + binary_number + ". Number of bits of 1: " + str(contor))
    else:
        print("Invalid input. Please enter a valid integer.")

numberOfBits()