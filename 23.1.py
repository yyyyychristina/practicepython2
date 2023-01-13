def laps_to_miles(num_laps):
    num_miles = num_laps * 0.25
    return num_miles

if __name__ == '__main__':
    num_laps = float(input())
    print(f'{laps_to_miles(num_laps):.2f}')
