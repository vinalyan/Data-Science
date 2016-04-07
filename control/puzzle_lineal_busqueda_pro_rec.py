#Puzzle lineal con busqueda en profundidad recursiva

from model.tree import Nodo

def buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # expandir los nodos sucesores hijos
        dato_nodo = nodo_inicial.get_datos()

        # operador izquierdo
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[3], dato_nodo[4]]

        hijo_izquierdo = Nodo(hijo)

        # operador central

        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)

        # operador derecho

        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)

