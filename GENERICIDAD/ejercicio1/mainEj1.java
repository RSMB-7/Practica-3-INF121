package ejercicio1G;

public class mainEj1 {

	public static void main(String[] args) {
		Caja<String> caja1 = new Caja<>();
        caja1.guardar("Hola mundo");

        Caja<Integer> caja2 = new Caja<>();
        caja2.guardar(123456);

        System.out.println("Contenido de caja 1: " + caja1.obtener());
        System.out.println("Contenido de caja 2: " + caja2.obtener());
	}

}
