package ejercicio1P;
import java.io.*;
import java.util.*;

public class ArchivoCliente {
	private String nomA;

	public ArchivoCliente(String n) {
		this.nomA = n;
	}

	public void crearArchivo() {
	        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
	            oos.writeObject(new ArrayList<Cliente>());
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	public void guardaCliente(Cliente c) {
        List<Cliente> lista = new ArrayList<>();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            lista = (ArrayList<Cliente>) ois.readObject();
        } catch (Exception e) {
        }

        lista.add(c);
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
            oos.writeObject(lista);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
	 public Cliente buscarCliente(int c) {
	        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
	            ArrayList<Cliente> lista = (ArrayList<Cliente>) ois.readObject();
	            for (Cliente cli : lista) {
	                if (cli.id == c) return cli;
	            }
	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	        return null;
	    }

	    public Cliente buscarCelularCliente(int c) {
	        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
	            ArrayList<Cliente> lista = (ArrayList<Cliente>) ois.readObject();
	            for (Cliente cli : lista) {
	                if (cli.telefono == c) return cli;
	            }
	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	        return null;
	    }

}