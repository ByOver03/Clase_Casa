package scanner;

import java.util.Scanner;

public class Scan {

	public static Integer ScannerInteger(Integer integer) {
		Scanner leer = new Scanner(System.in);
		integer = leer.nextInt();
		return integer;
	}
	

	public static String ScannerString (String string) {
		Scanner leer = new Scanner(System.in);
		string = leer.nextLine();
		return string;
	}
	public static double Scannerdouble(double doble){
		Scanner leer = new Scanner(System.in);
		doble = leer.nextDouble();
		return doble;
	}
	public static boolean ScannerBoolean(boolean sino){
		Scanner leer = new Scanner(System.in);
		sino= leer.nextBoolean();
		return sino;
	}
	public static char DevuelveChar(char character){
		Scanner leer= new Scanner(System.in);
		String caracter = leer.nextLine();
		character = caracter.charAt(0);
		return character;
	}

}
