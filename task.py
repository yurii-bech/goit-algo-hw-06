import networkx as nx
import matplotlib.pyplot as plt
import heapq


# Завдання 1
# Створення пустого графа
G = nx.Graph()

# Додавання вершин (людей) та ребер (зв'язків) між ними
G.add_nodes_from([
    (1, {"name": "Alice"}),
    (2, {"name": "Bob"}),
    (3, {"name": "Charlie"}),
    (4, {"name": "David"}),
    (5, {"name": "Eve"})
])

G.add_edges_from([
    (1, 2), (1, 3), (2, 3),
    (3, 4), (4, 5)
])

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Позиціонування вершин
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
plt.title("Соціальна мережа")
plt.show()

# Аналіз основних характеристик графа
print("Основні характеристики графа:")
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Список вершин:", list(G.nodes))
print("Список ребер:", list(G.edges))
print("Ступінь вершин:", dict(G.degree()))


# Завдання 2
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            yield from dfs_paths(graph, neighbor, goal, path + [neighbor])

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_vertex in set(graph.neighbors(vertex)) - set(path):
            if next_vertex == goal:
                yield path + [next_vertex]
            else:
                queue.append((next_vertex, path + [next_vertex]))

# Знаходження шляхів за допомогою DFS
print("Шляхи за допомогою DFS:")
for path in dfs_paths(G, 1, 5):
    print(path)

# Знаходження шляхів за допомогою BFS
print("\nШляхи за допомогою BFS:")
for path in bfs_paths(G, 1, 5):
    print(path)


# Завдання 3
G.add_edges_from([
    (1, 2, {'weight': 2}), (1, 3, {'weight': 3}), (2, 3, {'weight': 1}),
    (3, 4, {'weight': 4}), (4, 5, {'weight': 5})
])

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, edge_data in graph[current_node].items():
            distance = current_distance + edge_data['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Знаходження найкоротших шляхів від вершини 1 до всіх інших вершин
shortest_paths = {}
for node in G.nodes:
    shortest_paths[node] = dijkstra(G, node)

# Виведення результатів
for source, distances in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {source}:")
    for target, distance in distances.items():
        print(f"Вершина {target}: Відстань {distance}")
    print()