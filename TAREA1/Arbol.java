public class Arbol {

    private Nodo raiz;

    // Constructor para el árbol binario de búsqueda
    public Arbol() {
        raiz = null;
    }

    // Método para insertar un nuevo valor en el árbol
    public void insertar(int valor) {
        raiz = insertarRecursivo(raiz, valor);
    }

    // Método recursivo para insertar un valor
    private Nodo insertarRecursivo(Nodo actual, int valor) {
        if (actual == null) {
            return new Nodo(valor);
        }

        if (valor < actual.valor) {
            actual.izquierdo = insertarRecursivo(actual.izquierdo, valor);
        } else if (valor > actual.valor) {
            actual.derecho = insertarRecursivo(actual.derecho, valor);
        } else {
            return actual;
        }

        return actual;
    }

    // Método para imprimir el árbol en orden
    public void imprimirArbol() {
        imprimirRecursivo(raiz);
    }

    // Método recursivo para imprimir el árbol en orden
    private void imprimirRecursivo(Nodo actual) {
        if (actual != null) {
            imprimirRecursivo(actual.izquierdo);
            System.out.println(actual.valor);
            imprimirRecursivo(actual.derecho);
        }
    }

    // Método para verificar si el árbol está vacío
    public boolean estaVacio() {
        return raiz == null;
    }

    // Método principal para probar el árbol
    public static void main(String[] args) {
        Arbol arbol = new Arbol();
        
        // Insertamos algunos valores en el árbol
        arbol.insertar(5);
        arbol.insertar(3);
        arbol.insertar(7);
        arbol.insertar(2);
        arbol.insertar(4);
        arbol.insertar(6);
        arbol.insertar(8);
        arbol.insertar(1);

        // Verificamos si el árbol está vacío
        System.out.println("¿El árbol está vacío? " + arbol.estaVacio());

        // Imprimimos el árbol en orden
        arbol.imprimirArbol();
    }
}
