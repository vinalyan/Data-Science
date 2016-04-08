# Vuelos con busqueda con profundidad iterativa

from model.tree import Nodo
def DFS_prof_iter(nodo, solucion):
    for limite in range(0,100):
        visitados=[]
        #sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        #if sol != None:
        #    return None
