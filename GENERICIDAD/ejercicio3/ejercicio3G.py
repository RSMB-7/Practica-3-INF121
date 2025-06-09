from typing import Generic, TypeVar, List

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, elemento: T):
        self.elementos.append(elemento)

    def buscar(self, elemento: T) -> bool:
        return elemento in self.elementos

    def mostrar(self):
        for elem in self.elementos:
            print(elem)
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __eq__(self, other):
        return isinstance(other, Libro) and self.titulo == other.titulo

    def __str__(self):
        return f"Libro: {self.titulo}"

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __eq__(self, other):
        return isinstance(other, Producto) and self.nombre == other.nombre

    def __str__(self):
        return f"Producto: {self.nombre}"
# Libros
catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar(Libro("Cien años de soledad"))
catalogo_libros.agregar(Libro("El principito"))

print("Catálogo de libros:")
catalogo_libros.mostrar()
print("¿Está 'El principito'?", catalogo_libros.buscar(Libro("El principito")))

# Productos
catalogo_productos = Catalogo[Producto]()
catalogo_productos.agregar(Producto("Laptop"))
catalogo_productos.agregar(Producto("Celular"))

print("\nCatálogo de productos:")
catalogo_productos.mostrar()
print("¿Está 'Tablet'?", catalogo_productos.buscar(Producto("Tablet")))
