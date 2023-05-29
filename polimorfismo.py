class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        return "Au au!"

class Gato(Animal):
    def emitirSom(self):
        return "Miau!"

# Uso de polimorfismo
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.emitirSom())