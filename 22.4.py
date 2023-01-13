num_of_integer = int(input())
my_list = []

for i in range(num_of_integer):
    user_input = int(input())
    my_list.append(user_input)
    
threshold = int(input())
    
for i in my_list:
    if i <= threshold:
        print(i, end=',')
    
