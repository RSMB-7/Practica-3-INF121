package ejercicio5P;

public class mainEj5P {
	public static void main(String[] args) {
		ArchFarmacia archivo = new ArchFarmacia("farmacias.txt");

		Farmacia f1 = new Farmacia();
		f1.setNombreFarmacia("Farmacia Central");
		f1.setSucursal(1);
		f1.setDireccion("Av. Principal 123");

		f1.agregarMedicamento(new Medicamento("Golpex", 101, "tos", 10.5));
		f1.agregarMedicamento(new Medicamento("Paracetamol", 102, "resfrio", 5.0));

		Farmacia f2 = new Farmacia();
		f2.setNombreFarmacia("Farmacia Sur");
		f2.setSucursal(2);
		f2.setDireccion("Calle Secundaria 456");

		f2.agregarMedicamento(new Medicamento("Ibuprofeno", 103, "resfrio", 7.0));
		f2.agregarMedicamento(new Medicamento("Golpex", 104, "tos", 9.0));

		archivo.adicionar(f1);
		archivo.adicionar(f2);

		System.out.println("Todas las farmacias:");
		archivo.listar();

		System.out.println("\nMedicamentos para la tos en sucursal 1:");
		archivo.mostrarMedicamentosTosSucursal(1);

		System.out.println("\nFarmacias con Golpex:");
		archivo.mostrarSucursalConGolpex();
	}
}