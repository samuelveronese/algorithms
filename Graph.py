import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.distance = 0
        self.dfs_start_time = None
        self.dfs_end_time = None
        self.predecessor = None
        self.key = None

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, u, v, w=1):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return "{} --{}--> {}".format(self.u, self.w, self.v)


class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = set()
        self.edges = set()
        # time for DFS
        self.time = 0

    def reset(self):
        for node in self.nodes:
            node.color = None
            node.distance = 0
            node.dfs_start_time = None
            node.dfs_end_time = None
            node.predecessor = None

    def add_node(self, node):
        self.nodes.add(node)

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_edge(self, u, v, w=1):
        self.edges.add(Edge(u, v, w))

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2] if len(edge) == 3 else 1)

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += str(node) + ": " + "\n"
            for adj in self.adj(node):
                string += "\t - " + str(adj) + " weight: " + \
                    str(self.get_weight(node, adj)) + "\n"
        return string

    def visualize(self):
        G = nx.Graph()
        edges = []
        for edge in self.edges:
            edges.append((edge.u.name, edge.v.name))
        G.add_edges_from(edges)
        nx.draw_networkx(G)
        plt.show()

    def adj(self, node):
        adj = []
        for edge in self.edges:
            if edge.u == node:
                adj.append(edge.v)
        return adj

    def bfs(self, s):
        for node in self.nodes:
            node.color = 'white'
            node.distance = float('inf')
            node.predecessor = None

        s.color = 'gray'
        s.distance = 0
        s.predecessor = None

        queue = []
        queue.append(s)

        while queue:
            u = queue.pop(0)
            for v in self.adj(u):
                if v.color == 'white':
                    v.color = 'gray'
                    v.distance = u.distance + 1
                    v.predecessor = u
                    queue.append(v)
            u.color = 'black'

    def dfs(self):
        for node in self.nodes:
            node.color = 'white'
            node.predecessor = None

        self.time = 0

        for u in self.nodes:
            if u.color == 'white':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1
        u.dfs_start_time = self.time
        u.color = 'gray'

        for v in self.adj(u):
            if v.color == 'white':
                v.predecessor = u
                self.dfs_visit(v)

        u.color = 'black'
        self.time += 1
        u.dfs_end_time = self.time

    def topological_sort(self):
        self.dfs()
        t_s = list(self.nodes)
        t_s.sort(key=lambda x: x.dfs_end_time, reverse=True)
        return t_s

    def transpose(self):
        g = Graph(self.name+'_T')
        for node in self.nodes:
            g.add_node(node)
        for edge in self.edges:
            g.add_edge(edge.v, edge.u, edge.w)
        g.reset()
        return g

    def strongly_connected_components(self):
        self.dfs()
        g_t = self.transpose()
        return g_t.get_scc(self)

    def get_scc(self, g):
        self.time = 0

        sorted_nodes = g.topological_sort()
        self.nodes = sorted_nodes
        self.reset()

        for node in self.nodes:
            node.color = 'white'

        # list of the strongly connected components
        scc = []
        for u in self.nodes:
            if u.color == 'white':
                scc.append(self.dfs_visit_t(u, []))
        return scc

    def dfs_visit_t(self, u, sc):
        sc.append(u)

        self.time += 1
        u.dfs_start_time = self.time
        u.color = 'gray'

        for v in self.adj(u):
            if v.color == 'white':
                v.predecessor = u
                self.dfs_visit_t(v, sc)

        u.color = 'black'
        self.time += 1
        u.dfs_end_time = self.time

        return sc

    def find_set(self, sets, u):
        if sets[u][0] == u:
            return u
        return self.find_set(sets, sets[u][0])

    def union(self, sets, u, v):
        x_root = self.find_set(sets, u)
        y_root = self.find_set(sets, v)
        if sets[x_root][1] < sets[y_root][1]:
            sets[x_root][0] = y_root
        elif sets[x_root][1] > sets[y_root][1]:
            sets[y_root][0] = x_root
        else:
            sets[y_root][0] = x_root
            sets[x_root][1] += 1

    def kruskal(self):
        result = []

        # sort edges by weight
        edges = list(self.edges)
        edges.sort(key=lambda x: x.w)

        # make set for each node
        sets = {}
        for v in self.nodes:
            sets[v] = [v, 0]

        for edge in edges:
            u = edge.u
            v = edge.v
            if self.find_set(sets, u) != self.find_set(sets, v):
                result.append(edge)
                self.union(sets, u, v)

        return result

    def get_weight(self, u, v):
        for edge in self.edges:
            if edge.u == u and edge.v == v:
                return edge.w
        return float('inf')

    def prim(self, r):
        for u in self.nodes:
            u.key = float('inf')
            u.predecessor = None

        r.key = 0
        queue = list(self.nodes)
        while queue:
            u = min(queue, key=lambda x: x.key)
            queue.remove(u)
            for v in self.adj(u):
                if v in queue and self.get_weight(u, v) < v.key:
                    v.predecessor = u
                    v.key = self.get_weight(u, v)

        result = []
        for u in self.nodes:
            if u.predecessor:
                result.append(Edge(u.predecessor, u, u.key))
        return result

    def relax(self, u, v):
        if v.distance > u.distance + self.get_weight(u, v):
            v.distance = u.distance + self.get_weight(u, v)
            v.predecessor = u

    def initialize_single_source(self, s):
        for node in self.nodes:
            node.distance = float('inf')
            node.predecessor = None
        s.distance = 0

    def bellman_ford(self, s):
        self.initialize_single_source(s)

        for _ in range(len(self.nodes)-1):
            for edge in self.edges:
                self.relax(edge.u, edge.v)

        for edge in self.edges:
            if edge.v.distance > edge.u.distance + self.get_weight(edge.u, edge.v):
                return False

        return True

    def dag_shortest_paths(self, s):

        nodes = self.topological_sort()
        self.initialize_single_source(s)
        for u in nodes:
            for v in self.adj(u):
                self.relax(u, v)

    def dijkstra(self, s):
        self.initialize_single_source(s)
        S = []
        Q = list(self.nodes)
        while Q:
            u = min(Q, key=lambda x: x.distance)
            Q.remove(u)
            S.append(u)
            for v in self.adj(u):
                self.relax(u, v)


if __name__ == '__main__':
    graph = Graph('G')
