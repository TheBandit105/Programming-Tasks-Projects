from Person import *
"A derived class to define Hombre properties."
class Hombre(Person):
    def speak(self, msg):
        print(self.name, ':\n\tHola!', msg)
    
