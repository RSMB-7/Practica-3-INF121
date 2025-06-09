package ejercicio1P;

public class mainEj1P {
	public static void main(String[] args) {
		ArchivoCliente archivo = new ArchivoCliente("clientes.dat");
		archivo.crearArchivo();

		Cliente c1 = new Cliente(1, "Ana", 123456);
		Cliente c2 = new Cliente(2, "Luis", 987654);
		archivo.guardaCliente(c1);
		archivo.guardaCliente(c2);

		Cliente buscado = archivo.buscarCliente(1);
		if (buscado != null)
			buscado.mostrarInfo();

		Cliente celular = archivo.buscarCelularCliente(987654);
		if (celular != null)
			celular.mostrarInfo();
	}
}
