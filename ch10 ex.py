

try:
    while my_index != len(new_string) / 2:
        print(new_string[my_index:len(new_string)/2])
        my_index += l
        
except (NameError, TypeError):
    print('Error Occurred')
