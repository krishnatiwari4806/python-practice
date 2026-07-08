class animal :
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class dog(animal):
    def speak(self):
        return f"{self.name} says Woof!"