class animal :
    def sound(self):
        print("Animal makes a sound")

class dog(animal):
    def sound(self):
        print("Dog barks")

class cat(animal):
    def sound(self):
        print("Cat meows")

# Creating objects of each class
a = animal()
d = dog()
c = cat()

# Calling the sound method
a.sound()  # Output: Animal makes a sound
d.sound()  # Output: Dog barks
c.sound()  # Output: Cat meows  