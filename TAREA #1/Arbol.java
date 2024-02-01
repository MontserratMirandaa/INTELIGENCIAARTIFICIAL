public class Arbol {

    private Nodo raiz;

    // Clase interna para Nodo
    private class Nodo {
        int valor;
        Nodo izquierdo;
        Nodo derecho;

        public Nodo(int valor) {
            this.valor = valor;
            izquierdo = null;
            derecho = null;
        }
    }

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
        // Si el nodo actual es nulo, hemos encontrado la ubicación para insertar el nuevo nodo
        if (actual == null) {
            return new Nodo(valor);
        }

        // Si el valor a insertar es menor que el valor del nodo actual, vamos hacia la izquierda
        if (valor < actual.valor) {
            actual.izquierdo = insertarRecursivo(actual.izquierdo, valor);
        // Si el valor a insertar es mayor que el valor del nodo actual, vamos hacia la derecha
        } else if (valor > actual.valor) {
            actual.derecho = insertarRecursivo(actual.derecho, valor);
        } else {
            // El valor ya existe, no hacemos nada
            return actual;
        }

        // Devolvemos el nodo actual después de insertar
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

        // Imprimimos el árbol en orden
        arbol.imprimirArbol();
    }
}
