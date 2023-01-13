user_input = int(input())

if not ((user_input >= 11) and (user_input <= 100)):
    print('Input must be 11-100')

else:
    while (user_input >= 11) and (user_input <= 100):
        ten_digit = user_input // 10
        one_digit = user_input % 10
        print(user_input)
        user_input -= 1
        if ten_digit == one_digit:
            break
    
