class Animal:
    def __init__(self, nome):
        self._nome = nome  # Atributo protegido

    def get_nome(self):
        return self._nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

# Uso de encapsulamento
cachorro = Cachorro("Pretinho")
print(f"{cachorro.get_nome()} faz: {cachorro.emitir_som()}") 
# Acesso ao atributo protegido por meio de um método e chamar um método público.

gato = Gato("Princesa")
print(f"{gato.get_nome()} faz: {gato.emitir_som()}")
# Acesso ao atributo protegido por meio de um método e chamar um método público.