my_list = [[10, 10], [100, 100], [500, 500, 1000]]

for val in my_list:
    new_list = [i for i in val if i>10]

print(new_list)



