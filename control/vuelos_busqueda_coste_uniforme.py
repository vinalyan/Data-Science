from model.tree import Nodo

def buscar_solucion_UCS (conexiones, estado_inicial, solucion):

    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_coste(0)
    nodos_frontera.append(nodo_inicial)
    while (not solucionado) and len(nodos_frontera) !=0:
        # ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, cmp=Nodo.compara())
        nodo = nodos_frontera [0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo

