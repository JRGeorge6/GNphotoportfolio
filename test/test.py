def encrypt():
    user_string = input()
    print(user_string)
    reverse_string = user_string[::-1]
    print(reverse_string)
    half_way = int(len(reverse_string)/2)
    print(half_way)
    encrypted_string = (reverse_string[half_way:]) + (reverse_string[:half_way])
    print(encrypted_string)

encrypt()