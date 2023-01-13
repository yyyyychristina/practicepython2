name = input()
my_dict = {}

with open(name, 'r') as f:
    lines = f.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        

    for i in range(0, len(lines), 2):
        if lines[i] in my_dict:
            my_dict[(lines[i])].append(lines[i+1])
            
        else:
            my_dict[(lines[i])] = [lines[i+1]]
            
    print(my_dict)            #delete later
#FIXME: I already make the dictionary but I dont know how to sort it and output to output_keys.txt
    #and don't know how to output to output_titles.txt.  
    output_keys_file = open('output_keys.txt', 'w')
    
    for key, value in my_dict.items():
        output_keys_file.write(f'{key}: {value}')
    output_keys_file.close()



    

