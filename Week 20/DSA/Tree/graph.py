class Graph:
    def __init__(self, routes=[]):
        self.graph = {}
        for v, e in routes:
            self.add_vertex(v, e)

    def add_vertex(self, vertex, edge):
        if vertex not in self.graph:
            self.graph[vertex] = [edge]
            return
        self.graph[vertex].append(edge)

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            print(f"{vertex} not present in graph")

    def remove_edge(self, vertex, edge):
        if vertex in self.graph and edge in self.graph[vertex]:
            self.graph[vertex].remove(edge)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            return True
        return False

    def bfs(self, node):
        queue = [node]
        visited = []
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.append(curr)
                queue.extend(self.graph.get(curr, []))
        return visited

    def dfs(self, node):
        stack = [node]
        visited = []
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)
                stack.extend(reversed(self.graph.get(curr, [])))
        return visited

    def find_paths(self, start, end, path=None):
        if path is None:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.graph:
            return []
        path = path  + [start]
        paths = []
        for p in self.graph[start]:
            if p not in path:
                sp = self.find_paths(p, end, path)
                paths.extend(sp)
        return paths
    def shortest_paths(self,start,end,path=None):
        if not path:
            path = []
        if start == end:
            return [path + [end]]
        if start not in self.graph:
            return []
        path = path + [start]
        shortest_path = None
        for p in self.graph[start]:
            if p not in path:
                sp = self.shortest_paths(p,end,path)
                if sp:
                    if (shortest_path is None or len(sp) < len(shortest_path)):
                        shortest_path = sp
        return shortest_path

    def print_graph(self):
        print(self.graph)


routes = [('Bengaluru', 'Mumbai'), ('Chennai', 'Karnataka'), ('Bengaluru', 'Chennai'), ('Chennai', 'Comibathore'),
        ('Chennai', 'Delhi'), ('Bengaluru', 'Hyderabad'), ('Bengaluru', 'Surat'), ('Bengaluru', 'Kochi')]
graph = Graph(routes)
graph.add_vertex('Kochi', 'Chennai')
graph.add_vertex('Kochi', 'Comibathore')
graph.add_edge('Kochi', 'Trivandrum')
graph.print_graph()
print(graph.dfs('Bengaluru'))
print(graph.bfs('Bengaluru'))
print(graph.find_paths('Bengaluru', 'Comibathore'))
print(graph.shortest_paths('Bengaluru', 'Comibathore'))
# graph.remove_edge('Kochi','Chennai')
# graph.remove_vertex('Chennai')
# graph.print_graph()
