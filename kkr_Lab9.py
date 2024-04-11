#  Ksenia

def encoder(string):
    nums = []  # creates list to store encoded numbers
    for letter in string:  # goes through each number in the string
        nums.append(str(int(letter)+3))  # changes the letter into an int, adds 3, changes back to string
    return ''.join(nums)  # outputs the joined list of encoded numbers


if __name__ == "__main__":
    while True:  # loops until quit option selected
        print("Menu"
              "________"
              "1. Encode"
              "2. Decode"
              "3. Quit")
        selection = input("Please enter an option: ")
        if selection == "1":  # Encode
            code = input("Please enter your password to encode: ")  # input original value
            password = encoder(code)  # saved encoded value in variable
        elif selection == "2":  # Decode
            pass  # insert decode func here
        elif selection == "3":  # Quit
            break
