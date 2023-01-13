user_text = input()

count = 0

for i in user_text:
    if i == ' ':
        continue
    if i == ',':
        continue
    if i == '!':
        continue
    if i == '.':
        continue
    count += 1
    
print(count)
    
