my_dict = {'AA':3, 'BB': 2, 'CC':1, 'DD':0}

v1 = list(my_dict.keys())[list(my_dict.values()).index(1)]

v2 = {v:k for k, v in my_dict.items()}[0]

print(v1,v2)
