package ejercicio1G;

public class Caja<T> {
	 private T contenido;

	    public void guardar(T valor) {
	        this.contenido = valor;
	    }

	    public T obtener() {
	        return contenido;
	    }
	}
