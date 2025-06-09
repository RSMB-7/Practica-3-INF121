class Medicamento:
    def __init__(self, nombre, cod_medicamento, tipo, precio):
        self.nombre = nombre
        self.cod_medicamento = cod_medicamento
        self.tipo = tipo
        self.precio = precio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Código: {self.cod_medicamento}, Tipo: {self.tipo}, Precio: {self.precio}")

    def get_tipo(self):
        return self.tipo

    def get_precio(self):
        return self.precio

    def get_nombre(self):
        return self.nombre


class Farmacia:
    def __init__(self, nombre, sucursal, direccion):
        self.nombre_farmacia = nombre
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def mostrar(self):
        print(f"Farmacia: {self.nombre_farmacia}, Sucursal: {self.sucursal}, Dirección: {self.direccion}")
        for m in self.medicamentos:
            m.mostrar()

    def mostrar_medicamentos(self, tipo):
        for m in self.medicamentos:
            if m.get_tipo().lower() == tipo.lower():
                m.mostrar()

    def busca_medicamento(self, nombre):
        return any(m.get_nombre().lower() == nombre.lower() for m in self.medicamentos)


class ArchFarmacia:
    def __init__(self, nombre_archivo):
        self.na = nombre_archivo
        self.farmacias = []

    def adicionar(self, farmacia):
        self.farmacias.append(farmacia)

    def listar(self):
        for f in self.farmacias:
            f.mostrar()

    def mostrar_medicamentos_resfrios(self):
        for f in self.farmacias:
            f.mostrar_medicamentos("resfrio")

    def precio_medicamento_tos(self):
        return sum(m.get_precio()
                   for f in self.farmacias
                   for m in f.medicamentos
                   if m.get_tipo().lower() == "tos")

    def mostrar_medicamentos_tos_sucursal(self, sucursal):
        for f in self.farmacias:
            if f.sucursal == sucursal:
                f.mostrar_medicamentos("tos")

    def mostrar_sucursal_con_golpex(self):
        for f in self.farmacias:
            if f.busca_medicamento("Golpex"):
                print(f"Sucursal: {f.sucursal} - Dirección: {f.direccion}")

if __name__ == "__main__":
    arch = ArchFarmacia("farmacias.txt")

    f1 = Farmacia("Farmacia Central", 1, "Av. Principal 123")
    f1.agregar_medicamento(Medicamento("Golpex", 101, "tos", 10.5))
    f1.agregar_medicamento(Medicamento("Paracetamol", 102, "resfrio", 5.0))

    f2 = Farmacia("Farmacia Sur", 2, "Calle Secundaria 456")
    f2.agregar_medicamento(Medicamento("Ibuprofeno", 103, "resfrio", 7.0))
    f2.agregar_medicamento(Medicamento("Golpex", 104, "tos", 9.0))

    arch.adicionar(f1)
    arch.adicionar(f2)

    print("Listado de farmacias:")
    arch.listar()

    print("\nMedicamentos para la tos en sucursal 1:")
    arch.mostrar_medicamentos_tos_sucursal(1)

    print("\nFarmacias que tienen Golpex:")
    arch.mostrar_sucursal_con_golpex()
