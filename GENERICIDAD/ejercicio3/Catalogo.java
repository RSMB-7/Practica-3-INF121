package ejercicio3G;
import java.util.ArrayList;

public class Catalogo<T> {
	private ArrayList<T> elementos;

	public Catalogo() {
		elementos = new ArrayList<>();
	}

	public void agregar(T elemento) {
		elementos.add(elemento);
	}

	public boolean buscar(T elemento) {
		return elementos.contains(elemento);
	}

	public void mostrar() {
		for (T elem : elementos) {
			System.out.println(elem);
		}
	}
}