synonyms = {}   # Define dictionary

# Type your code here
word = input()
letter = input()

file_name = word + ".txt"
with open(file_name, 'r+') as f:
    lines = f.readlines()
    for row in lines:
        tokens = row.split()
        synonyms[tokens[0][0]] = tokens
        

    
    if letter in synonyms:
        for meaning in synonyms[letter]:
                print(meaning)
    else:
        print(f'No synonyms for {word} begin with {letter}.')
    
    
