from animal import Animal
from gato import Gato
from animal_abs import Animal as animal_abstrato 
from cachorro import Cachorro 

if __name__ == '__main__':
 
 cachorro = Cachorro()
 print(cachorro.fazer_som())

 gato = Gato("Leoncio")
 print(gato.fazer_som())

 animal = Animal(gato.nome)
 print(animal.fazer_som())