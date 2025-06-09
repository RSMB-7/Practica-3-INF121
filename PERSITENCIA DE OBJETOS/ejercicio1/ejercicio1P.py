import pickle
import os

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}")
        
class ArchivoEmpleado:
    def __init__(self, n: str):
        self.nomA = n

    def crearArchivo(self):
        if not os.path.exists(self.nomA):
            with open(self.nomA, 'wb') as archivo:
                pickle.dump([], archivo)

    def guardarEmpleado(self, e: Empleado):
        empleados = []
        if os.path.exists(self.nomA):
            with open(self.nomA, 'rb') as archivo:
                empleados = pickle.load(archivo)
        empleados.append(e)
        with open(self.nomA, 'wb') as archivo:
            pickle.dump(empleados, archivo)

    def buscaEmpleado(self, n: str) -> Empleado:
        if os.path.exists(self.nomA):
            with open(self.nomA, 'rb') as archivo:
                empleados = pickle.load(archivo)
                for emp in empleados:
                    if emp.nombre == n:
                        return emp
        return None

    def mayorSalario(self, s: float) -> Empleado:
        if os.path.exists(self.nomA):
            with open(self.nomA, 'rb') as archivo:
                empleados = pickle.load(archivo)
                for emp in empleados:
                    if emp.salario > s:
                        return emp
        return None
# Crear archivo
archivo = ArchivoEmpleado("empleados.dat")
archivo.crearArchivo()

# Agregar empleados
archivo.guardarEmpleado(Empleado("Luis", 30, 1200.50))
archivo.guardarEmpleado(Empleado("Ana", 28, 2500.00))
archivo.guardarEmpleado(Empleado("Carlos", 40, 1800.00))

# Buscar por nombre
emp = archivo.buscaEmpleado("Ana")
if emp:
    print("Empleado encontrado:")
    emp.mostrar_info()
else:
    print("Empleado no encontrado.")

# Buscar por salario mayor
emp2 = archivo.mayorSalario(1500.00)
if emp2:
    print("Empleado con salario mayor a 1500:")
    emp2.mostrar_info()
else:
    print("No hay empleado con salario mayor al ingresado.")
