class Graph:
    def __init__(self, routes=None):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        if vertex not in self.graph:
            self.add_vertex(vertex)
            self.graph[vertex] = [edge]
        if edge not in self.graph[vertex]:
            self.graph[vertex].append(edge)
        return True

    def remove_vertex(self, vertex):
        for ver in self.graph:
            if vertex in self.graph[ver]:
                self.graph[ver].remove(vertex)
        del self.graph[vertex]

    def remove_edge(self, vertex, edge):
        if edge in self.graph[vertex]:
            self.graph[vertex].remove(edge)

    def bfs(self, node):
        queue = [node]
        visted = []
        while queue:
            curr = queue.pop(0)
            if curr not in visted:
                visted.append(curr)
                queue.extend(self.graph.get(curr, []))
        return visted

    def dfs(self, node):
        stack = [node]
        visited = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)
                stack.extend(self.graph.get(curr, []))
        return visited

    def find_path(self, start, end, path=None):
        if start not in self.graph:
            return []
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        
        paths = []
        for i in self.graph[start]:
            if i not in path:
                p = self.find_path(i,end,path)
                if p:
                    paths.extend(p)
        return paths
    def shortest_path(self,start,end,path=None):
        if start not in self.graph:
            return []
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        shortest_path = None
        for i in self.graph[start]:
            if i not in path:
                p = self.shortest_path(i,end,path)
                if p:
                    if shortest_path is None or len(p) < len(shortest_path):
                        shortest_path = p
        return shortest_path

    def display(self):
        print(self.graph.items())


g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D','E')
g.add_edge('B','E')
g.add_edge('E','O')
g.display()
print(g.bfs('A'))
print(g.dfs('A'))
print(g.find_path('A','E'))
print(g.shortest_path('A','E'))
