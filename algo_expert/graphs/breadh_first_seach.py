



class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # TC O(v+e) SC O(v)
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array




nodes_to_introduce = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
root = Node(nodes_to_introduce[0])

# Create level 2
root.addChild(nodes_to_introduce[1])
root.addChild(nodes_to_introduce[2])
root.addChild(nodes_to_introduce[3])

# Create level 3
root.children[0].addChild(nodes_to_introduce[4])
root.children[0].addChild(nodes_to_introduce[5])
root.children[1].addChild(nodes_to_introduce[6])
root.children[1].addChild(nodes_to_introduce[7])
root.children[2].addChild(nodes_to_introduce[8])

# Create level 4
root.children[0].children[0].addChild(nodes_to_introduce[9])
root.children[0].children[1].addChild(nodes_to_introduce[10])


res = root.breadthFirstSearch([])
print(f"breadthFirstSearch {res}")


