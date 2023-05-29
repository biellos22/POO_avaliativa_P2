
# Uso de herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Au au!"

class Gato(Animal):
    def emitir_som(self):
        return f"{self.nome} diz: Miau!"

cachorro = Cachorro("Pretinho")
gato = Gato("Princesa")

print(cachorro.emitir_som())  # Saída: "Pretinho diz: Au au!"
print(gato.emitir_som())  # Saída: "Princesa diz: Miau!"
