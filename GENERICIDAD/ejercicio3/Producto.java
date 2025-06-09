package ejercicio3G;

public class Producto {
	private String nombre;

	public Producto(String nombre) {
		this.nombre = nombre;
	}

	public String toString() {
		return "Producto: " + nombre;
	}

	public boolean equals(Object obj) {
		if (obj instanceof Producto) {
			return this.nombre.equals(((Producto) obj).nombre);
		}
		return false;
	}
}
