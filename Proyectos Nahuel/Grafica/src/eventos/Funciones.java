package eventos;

import javax.swing.*;

public class Funciones {

	public static JFrame creaFormulario(String caption, int ancho, int alto) {
		
		JFrame formulario = new JFrame(caption);
		formulario.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
		formulario.setSize(ancho,alto);
		
		formulario.setLocationRelativeTo(null);
		
		return formulario;
	}
}
