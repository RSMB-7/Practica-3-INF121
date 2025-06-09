package ejercicio3G;

public class Libro {
	private String titulo;

	public Libro(String titulo) {
		this.titulo = titulo;
	}

	public String toString() {
		return "Libro: " + titulo;
	}

	public boolean equals(Object obj) {
		if (obj instanceof Libro) {
			return this.titulo.equals(((Libro) obj).titulo);
		}
		return false;
	}
}
