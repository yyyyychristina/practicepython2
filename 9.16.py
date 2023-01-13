class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    user_input = VendingMachine()
    
    # TODO: Purchase input number of drinks
    user_input.purchase(int(input()))
    
    # TODO: Restock input number of bottles
    user_input.restock(int(input()))
    
    # TODO: Report inventory
    user_input.report()
