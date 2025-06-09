from typing import Generic, TypeVar

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido = None

    def guardar(self, valor: T):
        self.contenido = valor

    def obtener(self) -> T:
        return self.contenido

# Crear cajas de diferentes tipos
caja1 = Caja[str]()
caja1.guardar("Hola mundo")

caja2 = Caja[int]()
caja2.guardar(123)

# Mostrar contenido
print("Contenido de caja1:", caja1.obtener())
print("Contenido de caja2:", caja2.obtener())
