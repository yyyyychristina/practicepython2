try:
    user_num = int(input())
    div_num = int(input())
    output = user_num / div_num
    print(int(output))
    
    if (not int(user_num)) and (user_num != 0):
        raise ValueError(f'invalid literal for int() with base 10: {user_num}')
    elif (not int(div_num)) and (user_num != 0):
        raise ValueError(f'invalid literal for int() with base 10: {div_num}')
    
except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')
    
except ValueError as excpt:
    print(f'Input Exception: {excpt}')
    
