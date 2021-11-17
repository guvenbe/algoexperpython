class Dog:
    def speak(self):
        print("woof")

class Cat:
    def speak(self):
        print("meow")

class AnimalSound:
    def sound(self, animal):
        animal.speak()

sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.sound(dog)
sound.sound(cat)