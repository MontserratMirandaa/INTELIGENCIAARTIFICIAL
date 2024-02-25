package TAREA3PUZZLE;

import java.util.*;

public class Puzzle8 {
    private String estadoInicial;
    private String estadoObjetivo = "123456780"; // Estado objetivo

    public Puzzle8(String estadoInicial) {
        this.estadoInicial = estadoInicial;
    }

    public void busquedaEnAnchura() {
        Set<String> visitados = new HashSet<>();
        Queue<Nodo> cola = new LinkedList<>();
        cola.add(new Nodo(estadoInicial));

        while (!cola.isEmpty()) {
            Nodo actual = cola.poll();
            visitados.add(actual.getEstado());

            // Comprobar si es el estado objetivo
            if (actual.getEstado().equals(estadoObjetivo)) {
                UtilidadesJuego.imprimirSolucion(actual);
                return;
            }

            // Generar sucesores
            for (String sucesor : UtilidadesJuego.getSucesores(actual.getEstado())) {
                if (!visitados.contains(sucesor)) {
                    Nodo nodoSucesor = new Nodo(sucesor);
                    actual.agregarHijo(nodoSucesor);
                    cola.add(nodoSucesor);
                }
            }
        }
    }

    public void busquedaEnProfundidad() {
        Set<String> visitados = new HashSet<>();
        Stack<Nodo> pila = new Stack<>();
        pila.push(new Nodo(estadoInicial));

        while (!pila.isEmpty()) {
            Nodo actual = pila.pop();

            // Comprobar si es el estado objetivo
            if (actual.getEstado().equals(estadoObjetivo)) {
                UtilidadesJuego.imprimirSolucion(actual);
                return;
            }

            if (!visitados.contains(actual.getEstado())) {
                visitados.add(actual.getEstado());

                // Generar sucesores
                for (String sucesor : UtilidadesJuego.getSucesores(actual.getEstado())) {
                    if (!visitados.contains(sucesor)) {
                        Nodo nodoSucesor = new Nodo(sucesor);
                        actual.agregarHijo(nodoSucesor);
                        pila.push(nodoSucesor);
                    }
                }
            }
        }
    }
}
