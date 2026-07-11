"""
count-the-number-of-complete-components
https://leetcode.com/problems/count-the-number-of-complete-components/
"""

from typing import List


def count_complete_components(n: int, edges: List[List[int]]) -> int:
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * n
    complete = 0

    for start in range(n):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        nodes = []
        edge_count = 0

        while stack:
            node = stack.pop()
            nodes.append(node)
            edge_count += len(adj[node])

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        k = len(nodes)
        if edge_count == k * (k - 1):
            complete += 1

    return complete

if __name__ == "__main__":
    print(count_complete_components(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
    print(count_complete_components(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
