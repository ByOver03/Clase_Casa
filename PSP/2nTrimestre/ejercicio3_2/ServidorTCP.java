package ejercicio3_2;

import java.io.*;
import java.net.*;

public class ServidorTCP {
    public static void main(String[] args) {
        final int PUERTO = 5000;
        ServerSocket servidor = null;

        try {
            // Crear el servidor en el puerto especificado
            servidor = new ServerSocket(PUERTO);
            System.out.println("Servidor iniciado en el puerto " + PUERTO);

            // Aceptar dos clientes
            for (int i = 1; i <= 2; i++) {
                System.out.println("Esperando conexión del cliente " + i + "...");
                Socket cliente = servidor.accept();
                System.out.println("Cliente " + i + " conectado.");
                
                // Obtener y mostrar los puertos locales y remotos
                int puertoLocal = cliente.getLocalPort();
                int puertoRemoto = cliente.getPort();
                System.out.println("Cliente " + i + ": Puerto local: " + puertoLocal + ", Puerto remoto: " + puertoRemoto);
                
                // Cerrar el cliente después de mostrar información
                cliente.close();
            }

            System.out.println("Ambos clientes se han conectado. Cerrando el servidor.");
        } catch (IOException e) {
            System.out.println("Error en el servidor: " + e.getMessage());
        } finally {
            if (servidor != null) {
                try {
                    servidor.close();
                } catch (IOException e) {
                    System.out.println("Error al cerrar el servidor: " + e.getMessage());
                }
            }
        }
    }
}
