def exact_change(user_total):
    money_total = user_total
   
    num_quarters = money_total // 25
    money_total -= num_quarters * 25
   
    num_dimes = money_total // 10
    money_total -= num_dimes * 10
   
    num_nickels = money_total // 5
    money_total -= num_nickels * 5
   
    num_pennies = money_total;
    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__':
    input_val = int(input()) 
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)
   
    if input_val <= 0:
        print("no change")
        # Could return at this point
        
    if num_pennies > 0:
        print (str(num_pennies), end=' ')
        if num_pennies == 1:
            print("penny")
        else:
            print("pennies")
            
    if num_nickels > 0:
        print (str(num_nickels), end=' ')
        if num_nickels == 1:
            print ("nickel")
        else:
            print ("nickels")
            
    if num_dimes > 0:
        print (str(num_dimes), end=' ')
        if num_dimes == 1:
            print ("dime")
        else:
            print ("dimes")            
            
    if num_quarters > 0:
        print (str(num_quarters), end = ' ')
        if num_quarters == 1:
            print ("quarter")
        else: 
            print ("quarters")
