import random

def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    randoms_list = []
    retries = 0
    while how_many != len(randoms_list):
        x = random.randint(0, max_num)
        if x not in randoms_list:
            randoms_list.append(x)
        else:
            retries += 1
    randoms_list.append(f'retries={retries}')
    return randoms_list
        
        
if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    # Type your code here. #
    random.seed(seed)
    print(*unique_random_ints(how_many, max_num))
