package TAREA3PUZZLE;

import java.util.ArrayList;
import java.util.List;

public class Nodo {
    private String estado;
    private Nodo padre;
    private List<Nodo> hijos;

    public Nodo(String estado) {
        this.estado = estado;
        this.padre = null;
        this.hijos = new ArrayList<>();
    }

    public String getEstado() {
        return estado;
    }

    public void setPadre(Nodo padre) {
        this.padre = padre;
    }

    public Nodo getPadre() {
        return padre;
    }

    public void agregarHijo(Nodo hijo) {
        hijos.add(hijo);
        hijo.setPadre(this);
    }

    public List<Nodo> getHijos() {
        return hijos;
    }
}
