import math
def max_magnitude(first_input, second_input, third_input):
    my_list = []
    new_list = []
    my_list.append(first_input)
    my_list.append(second_input)
    my_list.append(third_input)
    if (first_input > 0) and (second_input > 0) and (third_input > 0):
        return max(my_list)

    elif (first_input > 0) and (second_input <= 0) and (third_input < 0):
        for i in my_list:
            i = math.fabs(i)
            new_list.append(i)
            return max(new_list) 
    else:
        for i in my_list:
            j = math.fabs(i)
            new_list.append(j)
            return max(new_list) * -1
    

if __name__ == '__main__':
    first_input = int(input())
    second_input = int(input())
    third_input = int(input())
    print(int(max_magnitude(first_input, second_input, third_input)))
