#  Ksenia

def encoder(string):
    nums = []
    for letter in string:
        nums.append(str(int(letter)+3))
    return ''.join(nums)

print(encoder("123456"))

