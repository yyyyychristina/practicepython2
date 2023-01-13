def get_stats(int_list):
    result_sum = 0
    result_min = int_list[0]
    result_max = int_list[0]
    for value in int_list:
        result_sum += value
        if value < result_min:
            result_min = value
        if value > result_max:
            result_max = value


    return result_sum, result_min, result_max


values = [ 6, 4, 12, 8 ]
c, a, b = get_stats(values)
print(f'{a}, {b}, {c}')
