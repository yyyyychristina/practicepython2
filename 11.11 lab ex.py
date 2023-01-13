import random



def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""

    # Type your code here. #
    #Generate a list of how_many random integers from 0 to max_num (inclusive).
    
    #When a random number exists in the list, a new random number must be generated; use a global variable, 
    #retries, to count the number of times an existing number is generated.
    
    #return the list    
    
    deck = [random.randint(0, max_num)] * how_many
        
    global retries
    retries = 0
    
    card = random.choice(deck)
    deck.remove(card)
    retries += 1
        

    return deck


if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    # Type your code here. #
    random.seed(seed)
    
    output = unique_random_ints(how_many, max_num)
  
    print(f'{output}, retries={retries}')
    
    
