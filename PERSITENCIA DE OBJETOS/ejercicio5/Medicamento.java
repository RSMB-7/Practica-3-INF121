package ejercicio5P;

public class Medicamento {
    private String nombre;
    private int codMedicamento;
    private String tipo;
    private double precio;

    public Medicamento() {}

    public Medicamento(String nombre, int codMedicamento, String tipo, double precio) {
        this.nombre = nombre;
        this.codMedicamento = codMedicamento;
        this.tipo = tipo;
        this.precio = precio;
    }

    public void mostrar() {
        System.out.println("Nombre: " + nombre + ", Código: " + codMedicamento + ", Tipo: " + tipo + ", Precio: " + precio);
    }

    public String getTipo() {
        return tipo;
    }

    public double getPrecio() {
        return precio;
    }

    public String getNombre() {
        return nombre;
    }
}
