package ejercicio5P;

public class Farmacia {
    private String nombreFarmacia;
    private int sucursal;
    private String direccion;
    private int nroMedicamentos;
    Medicamento[] m = new Medicamento[100];

    public Farmacia() {
        nroMedicamentos = 0;
    }

    public void agregarMedicamento(Medicamento med) {
        if (nroMedicamentos < m.length) {
            m[nroMedicamentos++] = med;
        }
    }

    public void mostrar() {
        System.out.println("Farmacia: " + nombreFarmacia + ", Sucursal: " + sucursal + ", Dirección: " + direccion);
        for (int i = 0; i < nroMedicamentos; i++) {
            m[i].mostrar();
        }
    }

    public int getSucursal() {
        return sucursal;
    }

    public String getDireccion() {
        return direccion;
    }

    public void mostrarMedicamentos(String tipo) {
        for (int i = 0; i < nroMedicamentos; i++) {
            if (m[i].getTipo().equalsIgnoreCase(tipo)) {
                m[i].mostrar();
            }
        }
    }

    public boolean buscaMedicamento(String nombre) {
        for (int i = 0; i < nroMedicamentos; i++) {
            if (m[i].getNombre().equalsIgnoreCase(nombre)) {
                return true;
            }
        }
        return false;
    }

    // Setters
    public void setNombreFarmacia(String nombre) {
        nombreFarmacia = nombre;
    }

    public void setSucursal(int suc) {
        sucursal = suc;
    }

    public void setDireccion(String dir) {
        direccion = dir;
    }
}
