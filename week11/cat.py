"""Define the cat class"""


class Cat:
    """New Cat class"""
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    '''def __init__(self):
        self.name = 'default name'
        self.age = 1000'''

    def meow(self):
        print(f'{self.name} says "Meow"')

    def purr(self):
        print('&lt;name&gt;')

    def print_cat(self):
        print(f'name {self.name}, age: {self.age}, coat_color: {self.coat_color}')

    def meet(animal):
        print(f'hisses at {animal.name}')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_dog(self):
        print(f'dog name {self.name}, age {self.age}')

    def bark(self):
        print(f'{self.name} barks')

    def meet(self, animal):
        if isinstance(animal, Dog):
            print(f'{self.name} wag tail at {animal.name} [Dog:{type(animal)}]')
        else:
            print(f'{self.name} hisses at {animal.name} [NonDog:{type(animal)}]')


###############
if (__name__ == "__main__"):
    dog1 = Dog('luckyDog', 3)
    cat1 = Cat('coolCat', 14, 'Blue')
    dog2 = Dog('CuteDog', 5)
