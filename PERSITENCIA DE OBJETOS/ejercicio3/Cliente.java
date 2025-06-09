package ejercicio1P;
import java.io.*;

public class Cliente implements Serializable {
    int id;
    String nombre;
    int telefono;

    public Cliente(int id, String nombre, int telefono) {
        this.id = id;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    public void mostrarInfo() {
        System.out.println("ID: " + id + ", Nombre: " + nombre + ", Teléfono: " + telefono);
    }
    
}
	
