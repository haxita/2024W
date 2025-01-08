# Ford-Fulkerson algorithm in Python

from collections import deque

class Graph:

    def __init__(self, graph):
        self.graph = graph  # original graph
        self.residual_graph = [[cell for cell in row] for row in graph]  # cloned graph
        self.latest_augmenting_path = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph
        self.current_flow = [[0 for _ in row] for row in graph]  # empty graph with same dimension as graph

    def ff_step(self, source, sink):
        """
        Perform a single flow augmenting iteration from source to sink. Update the latest augmenting path, the residual
        graph and the current flow by the maximum possible amount, according to the path found by BFS.
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the amount by which the flow has increased.
        """
        # TODO
        n = len(self.residual_graph)
        visited = [False] * n
        parent = [-1] * n

        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            if u == sink:
                break
            for v in reversed(range(n)):
                if not visited[v] and self.residual_graph[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)

        if not visited[sink]:
            self.latest_augmenting_path = [[0]*n for _ in range(n)]
            return 0

        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, self.residual_graph[u][v])
            v = u

        self.latest_augmenting_path = [[0]*n for _ in range(n)]
        v = sink
        while v != source:
            u = parent[v]
            self.latest_augmenting_path[u][v] = path_flow
            v = u

        v = sink
        while v != source:
            u = parent[v]
            self.current_flow[u][v] += path_flow
            self.residual_graph[u][v] -= path_flow
            self.residual_graph[v][u] += path_flow
            v = u

        return path_flow

    def ford_fulkerson(self, source, sink):
        """
        Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step())
        @param source the source's vertex id
        @param sink the sink's vertex id
        @return the max flow from source to sink
        """
        # TODO
        max_flow = 0
        while True:
            flow = self.ff_step(source, sink)
            if flow == 0:
                break
            max_flow += flow
        return max_flow
