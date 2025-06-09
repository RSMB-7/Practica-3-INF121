from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def apilar(self, elemento: T):
        self.elementos.append(elemento)

    def desapilar(self) -> Optional[T]:
        if self.elementos:
            return self.elementos.pop()
        return None

    def mostrar(self):
        print("Contenido de la pila (de abajo hacia arriba):")
        for elem in self.elementos:
            print(elem)
# Pila de enteros
pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
print("Pila de enteros:")
pila_enteros.mostrar()
print("Desapilado:", pila_enteros.desapilar())
pila_enteros.mostrar()
print()
# Pila de cadenas
pila_cadenas = Pila[str]()
pila_cadenas.apilar("uno")
pila_cadenas.apilar("dos")
pila_cadenas.apilar("tres")
print("Pila de cadenas:")
pila_cadenas.mostrar()
print("Desapilado:", pila_cadenas.desapilar())
pila_cadenas.mostrar()
print()
# Pila de booleanos
pila_booleanos = Pila[bool]()
pila_booleanos.apilar(True)
pila_booleanos.apilar(False)
print("Pila de booleanos:")
pila_booleanos.mostrar()
print("Desapilado:", pila_booleanos.desapilar())
pila_booleanos.mostrar()
