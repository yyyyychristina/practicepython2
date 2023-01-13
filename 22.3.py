user_input = int(input())
my_list = []

while user_input > 0:
    my_list.append(user_input)
    user_input = int(input())
    
print(f'{min(my_list)} and {max(my_list)}')
    
