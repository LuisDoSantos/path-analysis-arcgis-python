from arcgis.gis import GIS
from arcgis.mapping import WebMap
import networkx as nx

#Conecta-se ao ArcGIS Online (substitua 'seu_usuario' e 'sua_senha' pelas suas credenciais) <- login licenca normal
#gis = GIS("https://www.arcgis.com", "seu_usuario", "sua_senha")

# Substitua 'seu_usuario' e 'sua_senha' pelos dados da sua conta institucional
username = 'xxxxxxxx@unesp.br'
password = 'xxxxxx'

# URL do portal institucional, substitua pelo URL correto
portal_url = 'https://unesp-edu.maps.arcgis.com'

# Conecta-se ao portal institucional usando a autenticação
gis = GIS(portal_url, username, password)

# Criação de um grafo de exemplo (pode ser substituído pelos seus dados reais)
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('A', 'C', weight=5)
G.add_edge('C', 'D', weight=3)
G.add_edge('B', 'D', weight=7)

# Execução do algoritmo de caminho mais curto (Dijkstra neste exemplo)
start_node = 'A'
end_node = 'D'
shortest_path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')

# Criação da rota como uma lista de coordenadas (substitua com suas próprias coordenadas)
route_coordinates = [(0, 0), (1, 1), (2, 2), (3, 3)]  # Exemplo, substitua com suas próprias coordenadas

# Cria um mapa da web vazio
webmap = WebMap()

# Adiciona uma camada de feature para representar os pontos e a rota mais eficiente
feature_collection = gis.content.import_data(G, title='Graph')
route_feature = gis.tools.featureanalysis.find_routes(feature_collection, start_points=[start_node], end_points=[end_node],
                                                      return_directions=True, point_barrier=route_coordinates)
webmap.add_layer(route_feature, {"renderer": "simple", "opacity": 0.7})
webmap.add_layer({"type": "mapImageLayer", "url": "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer"})

# Exibe o mapa
webmap
