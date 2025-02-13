package Casino.RuletaBien;

public class Banca {

    int dinero = 50000;
    int numero;
    int jugadoresEsperando = 0;
    int jugadoresDisponibles = 12;

    synchronized int obtenerNumeroGanador() {
        while (!Ruleta.disponible) { 
            try {
                wait();
            } catch (InterruptedException e) {
            }
        }
        jugadoresEsperando++;

        if (jugadoresEsperando < jugadoresDisponibles) {
            try {
                wait();
            } catch (InterruptedException e) {
            }
        } else {
            notifyAll();
            jugadoresEsperando = 0;
        }

        return numero;
    }

    synchronized void ganarDinero(int cantidad) {
        dinero += cantidad;
    }

    synchronized void perderDinero(int cantidad) {
        dinero -= cantidad;
    }
}
