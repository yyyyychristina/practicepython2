class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0
        
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def print_info(self):
        print('Pet Information:')
        print('   Name:', self.name)
        print('   Age:', self.age)

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''
    
    def set_breed(self, breed):
        self.breed = breed
    
    def print_info(self):
        Pet.print_info(self)
        print('   Breed:', self.breed)

my_pet = Pet()
my_dog = Dog()

pet_name = input()
pet_age = int(input())
dog_name = input()
dog_age = int(input())
dog_breed = input()

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()
my_pet.set_name(pet_name)
my_pet.set_age(pet_age)
my_pet.print_info()

# TODO: Create dog pet (using dog_name, dog_age, dog_breed) and then call print_info()
my_dog.set_name(dog_name)
my_dog.set_age(dog_age)
my_dog.set_breed(dog_breed)
my_dog.print_info()

# TODO: Use my_dog.breed to output the breed of the dog

