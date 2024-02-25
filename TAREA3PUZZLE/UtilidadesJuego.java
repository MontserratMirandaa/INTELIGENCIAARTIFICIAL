package TAREA3PUZZLE;

import java.util.ArrayList;
import java.util.List;

public class UtilidadesJuego {
    // Método para generar todos los estados sucesores posibles desde un estado dado
    public static List<String> getSucesores(String estado) {
        List<String> sucesores = new ArrayList<>();
        int index0 = estado.indexOf('0');
        int row = index0 / 3;
        int col = index0 % 3;

        // Movimientos posibles: arriba, abajo, izquierda, derecha
        int[][] movimientos = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int[] movimiento : movimientos) {
            int nuevaFila = row + movimiento[0];
            int nuevaColumna = col + movimiento[1];
            if (nuevaFila >= 0 && nuevaFila < 3 && nuevaColumna >= 0 && nuevaColumna < 3) {
                char[] nuevoEstado = estado.toCharArray();
                // Intercambiar '0' con el número en la nueva posición
                nuevoEstado[index0] = nuevoEstado[nuevaFila * 3 + nuevaColumna];
                nuevoEstado[nuevaFila * 3 + nuevaColumna] = '0';
                sucesores.add(new String(nuevoEstado));
            }
        }
        return sucesores;
    }

    // Método para imprimir la solución
    public static void imprimirSolucion(Nodo nodoFinal) {
        List<String> movimientos = new ArrayList<>();
        Nodo actual = nodoFinal;
        while (actual != null) {
            movimientos.add(0, actual.getEstado());
            actual = actual.getPadre();
        }

        for (String estado : movimientos) {
            System.out.println(estado.substring(0, 3));
            System.out.println(estado.substring(3, 6));
            System.out.println(estado.substring(6, 9));
            System.out.println();
        }
        System.out.println("Número de movimientos: " + (movimientos.size() - 1));
    }
}
