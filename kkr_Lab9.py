#  Ksenia

def encoder(string):
    nums = [] # creates list
    for letter in string:
        nums.append(str(int(letter)+3))
    return ''.join(nums)

def menu():
    print("Menu"
          "________"
          "1. Encode"
          "2. Decode"
          "3. Quit")

if __name__ == "__main__":
    while True:
        menu()
        selection = input("Please enter an option: ")
        if selection == "1":
            code = input("Please enter your password to encode: ")
            password = encoder(code)
        elif selection == "2":
            pass
        elif selection == "3":
            break
