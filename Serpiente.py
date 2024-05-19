import heapq
import random

class Nodo:
    def __init__(self, posicion=None, padre=None):
        self.posicion = posicion
        self.padre = padre
        self.g = 0  # Costo desde el inicio hasta el nodo actual
        self.h = 0  # Heurística: costo estimado desde el nodo actual hasta el final
        self.f = 0  # Costo total (g + h)
    
    def __lt__(self, otro):
        return self.f < otro.f

def heuristica(pos1, pos2):
    # Distancia de Manhattan
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar(tablero, inicio, fin, serpiente):
    # Inicializar tanto la lista abierta como la cerrada
    lista_abierta = []
    lista_cerrada = set()
    
    nodo_inicio = Nodo(inicio, None)
    nodo_fin = Nodo(fin, None)
    
    heapq.heappush(lista_abierta, nodo_inicio)
    
    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)
        
        if nodo_actual in lista_cerrada:
            continue
        
        if nodo_actual.posicion == nodo_fin.posicion:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.posicion)
                nodo_actual = nodo_actual.padre
            return camino[::-1]  
        
        lista_cerrada.add(nodo_actual)
        
        for nueva_posicion in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Movimientos posibles
            posicion = (nodo_actual.posicion[0] + nueva_posicion[0], nodo_actual.posicion[1] + nueva_posicion[1])
            
            if posicion[0] < 0 or posicion[0] >= len(tablero) or posicion[1] < 0 or posicion[1] >= len(tablero[0]):
                continue  # Si la posición está fuera del tablero
            
            if posicion in serpiente or tablero[posicion[0]][posicion[1]] == 1:
                continue  # Si la posición es parte de la serpiente o hay un obstáculo
            
            nuevo_nodo = Nodo(posicion, nodo_actual)
            nuevo_nodo.g = nodo_actual.g + 1
            nuevo_nodo.h = heuristica(posicion, fin)
            nuevo_nodo.f = nuevo_nodo.g + nuevo_nodo.h
            
            # Verificar si el nuevo nodo ya está en lista_abierta o lista_cerrada
            if nuevo_nodo in lista_cerrada:
                continue
            
            heapq.heappush(lista_abierta, nuevo_nodo)
    
    return None  # Si no hay camino
def imprimir_tablero(tablero, serpiente, comida):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if (fila, columna) == comida:
                print("C", end=" ")
            elif (fila, columna) in serpiente:
                print("S", end=" ")
            elif tablero[fila][columna] == 1:
                print("O", end=" ")  # Obstáculo
            else:
                print(".", end=" ")  # Espacio vacío
        print()  # Nueva línea al final de cada fila

def main():
    # Configuración inicial del juego
    tamano_tablero = (10, 10)
    tablero = [[0 for _ in range(tamano_tablero[1])] for _ in range(tamano_tablero[0])]
    
    serpiente = [(5, 5)]  # La serpiente comienza en el centro del tablero
    comida = (random.randint(0, tamano_tablero[0]-1), random.randint(0, tamano_tablero[1]-1))
    
    # Añadir algunos obstáculos de forma aleatoria
    for _ in range(5):
        tablero[random.randint(0, tamano_tablero[0]-1)][random.randint(0, tamano_tablero[1]-1)] = 1
    
    while True:
        # Limpiar el tablero para la nueva posición de la serpiente y obstáculos
        tablero = [[0 for _ in range(tamano_tablero[1])] for _ in range(tamano_tablero[0])]
        for _ in range(5):  # Añadir 5 obstáculos aleatorios
            tablero[random.randint(0, tamano_tablero[0]-1)][random.randint(0, tamano_tablero[1]-1)] = 1
        
        camino = astar(tablero, serpiente[0], comida, serpiente)
        
        if not camino:
            print("No hay camino hacia la comida. Reintentando...")
            comida = (random.randint(0, tamano_tablero[0]-1), random.randint(0, tamano_tablero[1]-1))
            continue
        
        # Mover la serpiente hacia la comida
        serpiente.insert(0, camino[1])  # Actualizar la posición de la serpiente con el siguiente paso hacia la comida
        if serpiente[0] == comida:  # Comprobar si la serpiente ha alcanzado la comida
            print("¡Comida alcanzada!")
            comida = (random.randint(0, tamano_tablero[0]-1), random.randint(0, tamano_tablero[1]-1))  # Generar nueva comida
        else:
            serpiente.pop()  # Mantener el mismo tamaño si no se ha alcanzado la comida
        
        imprimir_tablero(tablero, serpiente, comida)
        
        input("Presiona Enter para continuar...")  # Pausa después de cada movimiento

if __name__ == "__main__":
    main()
 
