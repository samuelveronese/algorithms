class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.distance = 0
        self.dfs_start_time = None
        self.dfs_end_time = None
        self.predecessor = None

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
                string += "\t - " + str(adj) + "\n"
        return string

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


if __name__ == '__main__':
    graph = Graph('G')

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    graph.add_nodes([a, b, c, d, e, f, g, h])

    edges = [(a, b, 1),
             (b, e, 1),
             (b, f, 1),
             (b, c, 1),
             (c, d, 1),
             (c, g, 1),
             (d, c, 1),
             (d, h, 1),
             (e, a, 1),
             (e, f, 1),
             (f, g, 1),
             (g, f, 1),
             (g, h, 1),
             (h, h)]
    graph.add_edges(edges)

    scc = graph.strongly_connected_components()
    for sc in scc:
        print("[", end="")
        for node in sc:
            print(node, end="")
        print("]")
