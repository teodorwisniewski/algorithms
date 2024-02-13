


class Graph:

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        print("\n\n Here is my graph:")
        for vertex, adj_vertices in self.adj_list.items():
            print(f"{vertex}: {adj_vertices}")
        
    def add_vertex(self, vertex: str) -> bool:

        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1: str, v2: str):
        if (v1 in self.adj_list and v2 in self.adj_list):
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        
        if (
            v1 in self.adj_list and
            v2 in self.adj_list and
            v2 in self.adj_list[v1] and
            v1 in self.adj_list[v2]
        ):
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False


    

if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge("C", "D")

    g.print_graph()

    g.remove_edge("A", "C")
    g.print_graph()
