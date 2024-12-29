from abc import ABC, abstractmethod

# Tính trừu tượng (Abstraction)
class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # Tính trừu tượng (Abstraction)
    @abstractmethod
    def make_sound(self):
        pass
    
    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}")

# Tính kế thừa (Inheritance)
class Lion(Animal):
    def __init__(self, name, age, mane_color):
        super().__init__(name, age)
        self._mane_color = mane_color

    # Tính đa hình (Polymorphism)
    def make_sound(self):
        print("Roar")
    
    def display_info(self):
        super().display_info()
        print(f"Mane Color: {self._mane_color}")

class Elephant(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self._weight = weight

    # Tính đa hình (Polymorphism)
    def make_sound(self):
        print("Trumpet")
    
    def display_info(self):
        super().display_info()
        print(f"Weight: {self._weight} ton")

class Monkey(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self._tail_length = tail_length

    # Tính đa hình (Polymorphism)
    def make_sound(self):
        print("Chatter")
    
    def display_info(self):
        super().display_info()
        print(f"Tail Length: {self._tail_length} cm")

# Tính đóng gói (Encapsulation)
lion = Lion("Leo", 5, "Golden")
elephant = Elephant("Dumbo", 10, 2.5)
monkey = Monkey("George", 3, 75)

# Sử dụng tính đa hình (Polymorphism)
animals = [lion, elephant, monkey]

for animal in animals:
    animal.display_info()
    animal.make_sound()
    print("---")
