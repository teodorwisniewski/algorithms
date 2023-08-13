class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        FIRST_NODE = 0
        LAST_NODE = len(graph) - 1
        def backtrack(paths, path, idx=0):

            if FIRST_NODE in path and LAST_NODE in path:
                paths.append(path.copy())
                return

            nodes_to_follow = graph[idx]
            for next_node_idx in nodes_to_follow:
                path.append(next_node_idx)
                backtrack(paths, path, next_node_idx)
                path.pop()
        paths = []
        path = [0]
        backtrack(paths, path)
        return paths

