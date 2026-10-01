from animal import Animal

class Gato(Animal):
    def __init__(self,nome):
        super().__init__(nome)


    def fazer_som(self):
        return "Miau!"