import networkx as nx
import matplotlib.pyplot as plt

# Criação de um grafo de exemplo (pode ser substituído pelos seus dados reais)
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=5)
G.add_edge('C', 'D', weight=3)
G.add_edge('B', 'D', weight=7)

# Visualização do grafo (opcional, dependendo da complexidade dos seus dados)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, font_color='black', font_family='sans-serif', edge_color='gray', linewidths=1, alpha=0.7)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Execução do algoritmo de caminho mais curto (Dijkstra neste exemplo)
start_node = 'A'
end_node = 'D'
shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
shortest_path_length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')

# Resultados da análise
print(f"Rota mais eficiente de {start_node} para {end_node}: {shortest_path}")
print(f"Distância total: {shortest_path_length} unidades de peso")

# Visualização da rota mais eficiente (opcional, dependendo da complexidade dos seus dados)
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange', node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
plt.show()