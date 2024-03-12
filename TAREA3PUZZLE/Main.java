package TAREA3PUZZLE;

public class Main {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        Puzzle8 juego = new Puzzle8("123450678"); // Un ejemplo de estado inicial

        //System.out.println("Resolviendo con BFS:");
        //juego.busquedaEnAnchura();
        System.out.println("\nResolviendo con DFS:");
        juego.busquedaEnProfundidad();
        
        long finishTime = System.currentTimeMillis();
        long totalTime = finishTime - startTime;
        System.out.printf("Tiempo total para resolver el puzzle en ms: %d\n", totalTime);
    }
}
