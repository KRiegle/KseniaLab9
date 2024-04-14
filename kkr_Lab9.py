def encoder(string):
    nums = []
    for letter in string:
        nums.append(str((int(letter) + 3) % 10))
    return ''.join(nums)

def decoder(string):
    nums = []
    for letter in string:
        nums.append(str((int(letter) - 3) % 10))
    return ''.join(nums)

if __name__ == "__main__":
    while True:  # loops until quit option selected
        print("\nMenu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        selection = input("Please enter an option: ")
        if selection == "1":  # Encode
            code = input("Please enter your password to encode: ")
            password = encoder(code)
            print("Your password has been encoded and stored!")
        elif selection == "2":  # Decode
            original_password = decoder(password)
            print(f"The encoded password is {password}, and the original password is {original_password}.")
        elif selection == "3":  # Quit
            print("Exiting program...")
            break