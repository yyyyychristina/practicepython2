file_name = input()

user_file = open(str(file_name))

output_list = user_file.readlines()

my_dict = {}
show_list = []
show_list_split = []

# Starting from first item in list, add every other item in list as a key
# and every value inbetween is the value associated with the preceeding key.
# If one key with multiple values, append to list
for index in range(len(output_list)):
    temp_list = []
    list_object = output_list[index].strip('\n')
    if (index + 1 < len(output_list) and (index % 2 == 0)):
        if int(list_object) in my_dict:
            my_dict[int(list_object)].append(output_list[index + 1].strip('\n'))
        else:
            temp_list.append(output_list[index + 1].strip('\n'))
            my_dict[int(list_object)] = temp_list

# Sort by keys (years) from least amount of years to greatest amount of years
my_dict_sorted_by_keys = dict(sorted(my_dict.items()))

# Change from dictionary to list
for x in my_dict.keys():
    show_list.append(my_dict[x])

# Split the list of lists into a single list
for x in show_list:
    for i in x:
        show_list_split.append(i)

# Sort list and output
show_list_split = sorted(show_list_split)

f = open('output_keys.txt', 'w')  # Open file
for key, value in my_dict_sorted_by_keys.items():
    f.write(str(key) + ": ")
    for item in value[:-1]:
        f.write(item + "; ")
    f.write(value[-1])
    f.write("\n")
f.close()  # Close the file

f = open('output_titles.txt', 'w')
for item in show_list_split:
    f.write(item + '\n')
f.close()





