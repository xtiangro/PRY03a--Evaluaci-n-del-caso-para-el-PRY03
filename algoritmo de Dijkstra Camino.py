import heapq

def matriz_a_grafo(matriz):
    grafo = {}
    n = len(matriz)

    for i in range(n):
        nodo = str(i + 1)
        grafo[nodo] = {}
        for j in range(n):
            peso = matriz[i][j]
            if peso != 0:
                grafo[nodo][str(j + 1)] = peso
    return grafo


def dijkstra(grafo, origen):
    dist = {v: float('inf') for v in grafo}
    dist[origen] = 0
    predecesor = {v: None for v in grafo}
    cola = [(0, origen)]

    while cola:
        d_actual, u = heapq.heappop(cola)
        if d_actual > dist[u]:
            continue

        for v, peso in grafo[u].items():
            nueva_dist = dist[u] + peso
            if nueva_dist < dist[v]:
                dist[v] = nueva_dist
                predecesor[v] = u
                heapq.heappush(cola, (nueva_dist, v))
    return dist, predecesor


def reconstruir_camino(predecesor, origen, destino):
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = predecesor[actual]
    if camino[0] != origen:
        return None  # No hay camino
    return camino

matriz = [
    [0, 90, 0, 0, 0, 0, 0, 0, 40, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [90, 0, 30, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 30, 0, 25, 140.155, 0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 140.155, 0, 0, 100.132, 110.139, 0, 0, 105.101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 110.139, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 60, 0, 0, 0, 0, 0, 0, 0, 0, 25.12, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [40, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 105.101, 0, 0, 0, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 25.12, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 25, 0, 0, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [25, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 0, 0, 25, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 70, 105, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 70, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 105, 50, 0, 35, 0, 15, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 35, 100.19, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 35, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100.19, 0, 0, 0, 90, 70, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 90, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 110, 90],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 110, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0],
]

grafo = matriz_a_grafo(matriz)

origen = input("Ingresa el vértice de origen (1-26): ").strip()
destino = input("Ingresa el vértice destino (1-26): ").strip()

dist, pred = dijkstra(grafo, origen)

camino = reconstruir_camino(pred, origen, destino)

print(f"\nDistancia mínima desde {origen} hasta {destino}: {dist[destino] if dist[destino] != float('inf') else '∞'}")

if camino:
    print(f"Camino más corto: {' → '.join(camino)}")
else:
    print(f"No existe camino entre {origen} y {destino}")
