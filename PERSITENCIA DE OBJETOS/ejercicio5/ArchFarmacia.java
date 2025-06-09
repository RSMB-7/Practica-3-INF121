package ejercicio5P;

import java.util.ArrayList;

public class ArchFarmacia {
    private String na;
    private ArrayList<Farmacia> farmacias = new ArrayList<>();

    public ArchFarmacia(String na) {
        this.na = na;
    }

    public void adicionar(Farmacia f) {
        farmacias.add(f);
    }

    public void listar() {
        for (Farmacia f : farmacias) {
            f.mostrar();
        }
    }

    public void mostrarMedicamentosResfrios() {
        for (Farmacia f : farmacias) {
            f.mostrarMedicamentos("resfrio");
        }
    }

    public double precioMedicamentoTos() {
        double total = 0;
        for (Farmacia f : farmacias) {
            for (Medicamento m : f.m) {
                if (m != null && m.getTipo().equalsIgnoreCase("tos")) {
                    total += m.getPrecio();
                }
            }
        }
        return total;
    }

    public void mostrarMedicamentosMenorTos() {
        for (Farmacia f : farmacias) {
            f.mostrarMedicamentos("tos");
        }
    }

    public void mostrarMedicamentosTosSucursal(int sucursal) {
        for (Farmacia f : farmacias) {
            if (f.getSucursal() == sucursal) {
                f.mostrarMedicamentos("tos");
            }
        }
    }

    public void mostrarSucursalConGolpex() {
        for (Farmacia f : farmacias) {
            if (f.buscaMedicamento("Golpex")) {
                System.out.println("Sucursal: " + f.getSucursal() + " - Dirección: " + f.getDireccion());
            }
        }
    }
}
