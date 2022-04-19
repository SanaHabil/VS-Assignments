class Pet:
# implement __init__( name , type , tricks, noise ):
    def __init__(self, name , type , tricks, noise) -> None:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        self.noise = noise 
        
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return energy 
        # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)

#Inhiritance from class Pet
class Dogs(Pet):
    def __init__(self, name, type, tricks, noise, age):
        super().__init__(name, type, tricks, noise)
        self.age = age

class Cats(Pet):
    def __init__(self, name, type, tricks, noise, age):
        super().__init__(name, type, tricks, noise)
        self.age = age

favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console

first_name = input("What is your First Name?")
Last_name = input("What is your Last Name?")
print(f'My name is: {first_name}', f' My last name is: {Last_name}')
