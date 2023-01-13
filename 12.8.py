f = open(input())
lower_bound = input()
upper_bound = input()

lines = f.readlines()
for ln in lines:
    ln = ln.strip('\n')
    if lower_bound <= ln <= upper_bound:
        print(ln)
        
f.close()
