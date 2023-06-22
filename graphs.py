class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.distance = 0
        self.start_time = None
        self.end_time = None
        self.predecessor = None


class AdjNode:
    def __init__(self, node):
        self.node = node
        self.next = None


class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.graph = {}
        self.time = 0

    def add_node(self, node):
        self.nodes.append(node)
        self.graph[node.name] = None

    def add_edge(self, source, destination):
        adj_node = AdjNode(destination)
        adj_node.next = self.graph[source.name]
        self.graph[source.name] = adj_node

    def print_agraph(self):
        for node in self.nodes:
            print("Node " + node.name + ":", end="")
            temp = self.graph[node.name]
            while temp:
                print(" -> {}".format(temp.node.name), end="")
                temp = temp.next
            print(" \n")

    def adj(self, node):
        adj = []
        temp = self.graph[node.name]
        while temp:
            adj.append(temp.node)
            temp = temp.next
        return adj

    def BFS(self, s):
        # Queue to keep track of nodes to be visited.
        queque = []

        for u in self.nodes:
            u.color = 'white'
            u.distance = float('inf')
            u.predecessor = None
        s.color = 'gray'
        s.distance = 0
        s.predecessor = None
        queque.append(s)
        while queque:
            u = queque.pop(0)
            for v in self.adj(u):
                if v.color == 'white':
                    v.color = 'gray'
                    v.distance = u.distance + 1
                    v.predecessor = u
                    queque.append(v)
            u.color = 'black'

    def DFS(self):
        for node in self.nodes:
            node.color = 'white'
            node.predecessor = None
        self.time = 0
        for node in self.nodes:
            if node.color == 'white':
                self.DFS_visit(node)

    def DFS_visit(self, node):
        self.time += 1
        node.start_time = self.time
        node.color = 'gray'

        for v in self.adj(node):
            if v.color == 'white':
                v.predecessor = node
                self.DFS_visit(v)
        
        node.color = 'black'
        self.time += 1
        node.end_time = self.time


def create_graph(nodes, edges):
    graph = Graph('grafo')
    for node in nodes:
        graph.add_node(node)

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    # graph.print_agraph()

    return graph


def main():
    s = Node('s')
    r = Node('r')
    v = Node('v')
    w = Node('w')
    t = Node('t')
    x = Node('x')
    u = Node('u')
    y = Node('y')
    nodes = [s, r, v, w, t, x, u, y]
    edges = [(s, r), (s, w), (r, s), (r, v), (v, r), (w, s), (w, t), (w, x), (t, w), (t, x),
             (t, u), (x, w), (x, t), (x, u), (x, y), (u, t), (u, x), (u, y), (y, x), (y, u)]

    graph = create_graph(nodes, edges)
    graph.DFS()

    for node in graph.nodes:
        print(node.name, node.start_time, node.end_time,
              node.predecessor.name if node.predecessor else None)


if __name__ == "__main__":
    main()
