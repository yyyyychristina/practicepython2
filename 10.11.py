# Define your method here
def steps_to_miles(num_steps):
    miles = num_steps / 2000
    if num_steps < 0:
        raise ValueError('Exception: Negative step count entered.')
    return miles
    

if __name__ == '__main__':
    # Type your code here.
    try:
        num_steps = int(input())
        print(f'{steps_to_miles(num_steps):.2f}')
            
    except ValueError as excpt:
        print(excpt)
