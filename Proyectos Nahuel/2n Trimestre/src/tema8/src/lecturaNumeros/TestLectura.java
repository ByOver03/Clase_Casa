package tema8.src.lecturaNumeros;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.Arrays;

public class TestLectura {
    public static void main(String[] args) {
        try (ObjectInputStream flujoEntrada = new ObjectInputStream(new FileInputStream("datos.dat"))){
            int[] t = new int [10];
            for(int i = 0; i< t.length; i++){
                t[i]= flujoEntrada.readInt();
            }
            System.out.println(Arrays.toString(t));
        } catch (IOException e) {
            e.getMessage();
        }
    }    
}
