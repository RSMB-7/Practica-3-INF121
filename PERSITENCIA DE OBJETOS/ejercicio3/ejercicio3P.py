import pickle

class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def mostrar_info(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}")


class ArchivoCliente:
    def __init__(self, nomA):
        self.nomA = nomA

    def crearArchivo(self):
        with open(self.nomA, "wb") as f:
            pickle.dump([], f)

    def guardaCliente(self, cliente):
        clientes = []
        try:
            with open(self.nomA, "rb") as f:
                clientes = pickle.load(f)
        except:
            pass
        clientes.append(cliente)
        with open(self.nomA, "wb") as f:
            pickle.dump(clientes, f)

    def buscarCliente(self, c):
        with open(self.nomA, "rb") as f:
            clientes = pickle.load(f)
            for cliente in clientes:
                if cliente.id == c:
                    return cliente
        return None

    def buscarCelularCliente(self, c):
        with open(self.nomA, "rb") as f:
            clientes = pickle.load(f)
            for cliente in clientes:
                if cliente.telefono == c:
                    return cliente
        return None

c1 = Cliente(1, "Ana", 123456)
c2 = Cliente(2, "Luis", 987654)

archivo = ArchivoCliente("clientes.dat")
archivo.crearArchivo()
archivo.guardaCliente(c1)
archivo.guardaCliente(c2)

cliente_busqueda = archivo.buscarCliente(2)
if cliente_busqueda:
    cliente_busqueda.mostrar_info()

cliente_cel = archivo.buscarCelularCliente(123456)
if cliente_cel:
    cliente_cel.mostrar_info()
