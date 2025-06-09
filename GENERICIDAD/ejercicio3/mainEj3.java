package ejercicio3G;

public class mainEj3 {

	public static void main(String[] args) {
		Catalogo<Libro> catalogoLibros = new Catalogo<>();
		catalogoLibros.agregar(new Libro("Cien años de soledad"));
		catalogoLibros.agregar(new Libro("El principito"));

		System.out.println("Catálogo de libros:");
		catalogoLibros.mostrar();
		System.out.println("¿Está 'El principito'? " + catalogoLibros.buscar(new Libro("El principito")));

		Catalogo<Producto> catalogoProductos = new Catalogo<>();
		catalogoProductos.agregar(new Producto("Laptop"));
		catalogoProductos.agregar(new Producto("Celular"));

		System.out.println("\nCatálogo de productos:");
		catalogoProductos.mostrar();
		System.out.println("¿Está 'Tablet'? " + catalogoProductos.buscar(new Producto("Tablet")));
	}
}