# Type your code here.
file_name = input()
new_name = ''
new_new_name = ''

with open(file_name, 'r+') as f:
    lines = f.readlines()

    for row in lines:
        new_name += row 
    if "_photo.jpg" in new_name:
        tokens = new_name.split("_photo.jpg")
        new_new_name = "_info.txt".join(tokens)
        print(new_new_name[0:-1])
