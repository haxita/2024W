""" 
File: Dijkstra.py

Description:
This file contains the implementation of various classes to model and manipulate a graph. 
It includes:
- Node: Represents a graph node with a name.
- Edge: Represents a weighted, undirected edge connecting two nodes.
- Step: Represents a step in a path, including the covered distance.
- Graph: A general graph structure with methods to manage nodes and edges.
- JKUMap: A specific graph implementation modeling a map of locations and their connections.

Classes and Key Functionalities:
1. **Node**:
   - Represents a node in the graph.
   - Supports equality comparison and hashing based on the node name.

2. **Edge**:
   - Represents an undirected, weighted connection between two nodes.
   - Ensures edges are treated as equal irrespective of node order.

3. **Step**:
   - Models a step in a path with a reference to the node and the distance covered to reach it.

4. **Graph**:
   - A generic graph implementation supporting:
     - Adding nodes and edges.
     - Querying nodes, edges, neighbors.
     - Finding nodes and edges by name.

5. **JKUMap (Extends Graph)**:
   - A concrete implementation of a graph modeling specific locations (e.g., "Spar", "LIT", "Porter").
   - Predefines nodes and edges representing connections between locations.
   - Includes methods (some to be implemented):
     - get_shortest_path: Determines the shortest path between two nodes.
     - get_shortest_distances: Finds shortest distances from a start node to all nodes.
     - reachable: Checks if there exists a path between two nodes.
     - init_shortest_path_structures: Initializes structures for shortest path calculations.
     - dijkstra: An optional method for Dijkstra's algorithm.

TODO:
- Implement the methods in JKUMap marked with #TODO.

Usage:
- This module can be used for educational purposes or extended for more advanced graph operations.

Author: [IPC Teaching JKU]
Date: [13.12.24]
"""

import heapq
from collections import deque

# Class node
class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, Node):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


# Class Edge
class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __str__(self):
        return f"({self.first} -- {self.weight} -> {self.second})"

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or not isinstance(other, Edge):
            return False
        return (self.weight == other.weight and
                ((self.first == other.first and self.second == other.second) or
                 (self.first == other.second and self.second == other.first)))

    def __hash__(self):
        return hash((self.first, self.second, self.weight))


# Class Step
class Step:
    def __init__(self, point, covered_distance):
        self.point = point            # Node visited on this path
        self.covered_distance = covered_distance  # Covered distance from the start to this point


# Class Graph
class Graph:
    def __init__(self):
        # Using lists that resize automatically
        self.nodes = []
        self.edges = []
        self.n_nodes = 0
        self.n_edges = 0

    def get_number_of_nodes(self):
        return self.n_nodes

    def get_number_of_edges(self):
        return self.n_edges

    def get_nodes(self):
        return self.nodes.copy()

    def get_edges(self):
        return self.edges.copy()

    def add(self, name):
        if self.find(name) is not None:
            return None
        v = Node(name)
        self.nodes.append(v)
        self.n_nodes += 1
        return v

    def add_edge(self, v1_name, v2_name, weight):
        n1 = self.find(v1_name)
        n2 = self.find(v2_name)
        if n1 is None or n2 is None:
            return None
        if self.find_edge(v1_name, v2_name) is not None:
            return None
        e = Edge(n1, n2, weight)
        self.edges.append(e)
        self.n_edges += 1
        return e

    def find(self, name):
        for v in self.nodes:
            if v.name == name:
                return v
        return None

    def find_edge(self, v1_name, v2_name):
        for e in self.edges:
            if ((e.first.name == v1_name and e.second.name == v2_name) or
                    (e.first.name == v2_name and e.second.name == v1_name)):
                return e
        return None

    def neighbors(self, name):
        v = self.find(name)
        if v is None:
            return None
        neighbor_nodes = []
        for e in self.edges:
            if e.first.name == v.name:
                neighbor_nodes.append(e.second)
            elif e.second.name == v.name:
                neighbor_nodes.append(e.first)
        return neighbor_nodes


# Class JKUMap
class JKUMap(Graph):

    SPAR = "Spar"
    LIT = "LIT"
    PORTER = "Porter"
    OPEN_LAB = "Open Lab"
    BANK = "Bank"
    KHG = "KHG"
    CHAT = "Chat"
    PARKING = "Parking"
    BELLA_CASA = "Bella Casa"
    LIBRARY = "Library"
    LUI = "LUI"
    TEICHWERK = "Teichwerk"
    SP1 = "SP1"
    SP3 = "SP3"
    CASTLE = "Castle"
    PAPAYA = "Papaya"
    JKH = "JKH"

    def __init__(self):
        super().__init__()
        self.add(self.SPAR)
        self.add(self.LIT)
        self.add(self.PORTER)
        self.add(self.OPEN_LAB)
        self.add(self.BANK)
        self.add(self.KHG)
        self.add(self.CHAT)
        self.add(self.PARKING)
        self.add(self.BELLA_CASA)
        self.add(self.LIBRARY)
        self.add(self.LUI)
        self.add(self.TEICHWERK)
        self.add(self.SP1)
        self.add(self.SP3)
        self.add(self.CASTLE)
        self.add(self.PAPAYA)
        self.add(self.JKH)
        self.add_edge(self.JKH, self.PAPAYA, 80)
        self.add_edge(self.PAPAYA, self.CASTLE, 85)
        self.add_edge(self.SP3, self.SP1, 130)
        self.add_edge(self.SP1, self.LUI, 175)
        self.add_edge(self.SP1, self.PARKING, 240)
        self.add_edge(self.PARKING, self.BELLA_CASA, 145)
        self.add_edge(self.PARKING, self.KHG, 190)
        self.add_edge(self.KHG, self.BANK, 150)
        self.add_edge(self.KHG, self.SPAR, 165)
        self.add_edge(self.SPAR, self.LIT, 50)
        self.add_edge(self.SPAR, self.PORTER, 103)
        self.add_edge(self.LIT, self.PORTER, 80)
        self.add_edge(self.PORTER, self.OPEN_LAB, 70)
        self.add_edge(self.PORTER, self.BANK, 100)
        self.add_edge(self.CHAT, self.BANK, 115)
        self.add_edge(self.CHAT, self.LIBRARY, 160)
        self.add_edge(self.CHAT, self.LUI, 240)
        self.add_edge(self.LUI, self.TEICHWERK, 135)
        self.add_edge(self.LUI, self.LIBRARY, 90)

    def get_shortest_path(self, from_node, to_node):
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" node to all other nodes.
        The number of steps (or -1 if no path exists) to each node is returned
        as a dictionary, using the node name as key and the distance as value.
        E.g., the "from" node has a step count of 0 to itself and 1 to all adjacent nodes.
        @:param from_node: start node
        @return:
        The path, with all intermediate steps, returned as an ArrayList. This list * sequentially contains each
        node along the shortest path, together with * the already covered distance. * Returns null if there is
        no path between the two given nodes.
        :raises ValueError: If from_node or to_node is None.
        """
        #TODO

        # 1) 检查参数合法性
        if from_node is None or to_node is None:
            raise ValueError("from_node or to_node is None.")
        if from_node == to_node:
            raise ValueError("from_node and to_node cannot be the same node.")

        # 2) 初始化距离与路径
        distances = {node: float('inf') for node in self.nodes}
        distances[from_node] = 0
        # paths[v] 用来存「从 from_node 出发到达 v 的节点列表（按访问顺序）」 
        paths = {node: [] for node in self.nodes}
        paths[from_node] = [from_node]

        # 3) 用最小堆（Dijkstra）
        visited = set()
        pq = [(0, from_node)]  # (当前最短距离, 当前节点)

        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            if cur_node in visited:
                continue
            visited.add(cur_node)

            # 如果已经到达 to_node，可以break（可选优化）
            if cur_node == to_node:
                break

            # 对 cur_node 的所有邻居尝试松弛
            for nbr in self.neighbors(cur_node.name):
                edge = self.find_edge(cur_node.name, nbr.name)
                if edge is not None:
                    new_dist = cur_dist + edge.weight
                    if new_dist < distances[nbr]:
                        distances[nbr] = new_dist
                        # paths[nbr] = 原来 paths[cur_node] + [nbr]
                        paths[nbr] = paths[cur_node] + [nbr]
                        heapq.heappush(pq, (new_dist, nbr))

        # 4) 判断是否可达
        if distances[to_node] == float('inf'):
            # 不可达则返回 None
            return None

        # 5) 根据最终的 path 列表生成 [Step(node, 累积距离), ...]
        route_nodes = paths[to_node]
        step_list = []
        cumulative_distance = 0

        for i, node in enumerate(route_nodes):
            if i == 0:
                # 第一个节点（起点），距离 0
                step_list.append(Step(node, 0))
            else:
                # 从前一个节点到当前节点的边权
                prev_node = route_nodes[i - 1]
                edge = self.find_edge(prev_node.name, node.name)
                cumulative_distance += edge.weight
                step_list.append(Step(node, cumulative_distance))

        return step_list


    def get_shortest_distances(self, from_node):
        """
        This method determines the shortest paths from a given "from" node to all other nodes.
        The shortest distance (or -1 if no path exists) to each node is returned
        as a dictionary, using the node name as key and the distance as value.
       :param from_node: Start node
       :return
       A dictionary containing the shortest distance (or -1 if no path exists) to each node,
       using the node name as key and the distance as value.
       :raises ValueError: If from_node is None.
       """
        # TODO
        if from_node is None:
            raise ValueError("from_node is None.")

    # 后面就是正常的 Dijkstra 过程
        distances = {node: float('inf') for node in self.nodes}
        distances[from_node] = 0

        visited = set()
        pq = [(0, from_node)]  # (dist, node)

        while pq:
            cur_dist, cur_node = heapq.heappop(pq)
            if cur_node in visited:
                continue
            visited.add(cur_node)

            # 松弛邻居节点
            for nbr in self.neighbors(cur_node.name):
                edge = self.find_edge(cur_node.name, nbr.name)
                if edge is not None:
                    new_dist = cur_dist + edge.weight
                    if new_dist < distances[nbr]:
                        distances[nbr] = new_dist
                        heapq.heappush(pq, (new_dist, nbr))

        # 把不可达的节点距离变成 -1
        for node in distances:
            if distances[node] == float('inf'):
                distances[node] = -1

        # 返回映射 (节点名 -> 距离)
        result = {}
        for node in self.nodes:
            result[node.name] = distances[node]
        return result

    def reachable(self, from_node, to_node):
        """
        This method determines whether there exists a path between from_node and to_node.
        :param from Start node
        :param from Target node
        :return true if a path exists, false otherwise
        :throws ValueError If from or to is null.
        """
        # TODO
        if from_node is None or to_node is None:
            raise ValueError("from_node or to_node is None.")

        # 用 BFS: queue + visited
        queue = deque()
        visited = set()

        queue.append(from_node)
        visited.add(from_node)

        while queue:
            cur = queue.popleft()
            if cur == to_node:
                return True

            for neighbor in self.neighbors(cur.name):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def init_shortest_path_structures(self, from_node, distances, paths):
        for v in self.get_nodes():
            distances[v] = float('inf')
        distances[from_node] = 0
        for v in self.get_nodes():
            paths[v] = []
        paths[from_node].append(from_node)

    def dijkstra(self, cur, visited, distances, paths):
        #This method is optional but recommended
        """
        This method is expected to be called with correctly initialized data structures and recursively calls
    itself.

        :param cur: Current node being processed
        :param visited: Set which stores already visited nodes.
        :param distances: Dict (nNodes entries) which stores the min. distance to each node.
        :param paths: Dict (nnodes entries) which stores the shortest path to each node.
        """
