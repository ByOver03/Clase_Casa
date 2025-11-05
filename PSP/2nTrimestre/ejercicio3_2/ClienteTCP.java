package ejercicio3_2;

import java.io.*;
import java.net.*;

public class ClienteTCP {
    public static void main(String[] args) {
        final String HOST = "127.0.0.1"; // Dirección IP del servidor (localhost)
        final int PUERTO = 5000; // Puerto del servidor

        Socket cliente = null;

        try {
            // Conectar al servidor
            cliente = new Socket(HOST, PUERTO);
            System.out.println("Conectado al servidor.");

            // Obtener información del socket
            int puertoLocal = cliente.getLocalPort(); // Puerto local del cliente
            int puertoRemoto = cliente.getPort(); // Puerto remoto del servidor
            String ipRemota = cliente.getInetAddress().getHostAddress(); // IP remota del servidor

            // Mostrar información
            System.out.println("Puerto local del cliente: " + puertoLocal);
            System.out.println("Puerto remoto del servidor: " + puertoRemoto);
            System.out.println("IP remota del servidor: " + ipRemota);

        } catch (IOException e) {
            System.out.println("Error en el cliente: " + e.getMessage());
        } finally {
            // Cerrar el socket
            if (cliente != null) {
                try {
                    cliente.close();
                    System.out.println("Conexión cerrada.");
                } catch (IOException e) {
                    System.out.println("Error al cerrar el cliente: " + e.getMessage());
                }
            }
        }
    }
}
