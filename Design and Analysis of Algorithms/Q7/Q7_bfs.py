#!/usr/bin/env python3
"""
Q7: Display the data stored in a given graph using BFS.
Graph given as adjacency list. Print BFS order from a start node.
Subject: Design and Analysis of Algorithms
"""
from collections import deque
from typing import Dict, List

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set([start])
    order = []
    q = deque([start])
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

if __name__ == "__main__":
    out_path = "Q7_bfs_output.txt"
    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: [4],
        4: []
    }
    start = 0
    order = bfs(graph, start)
    s = f"Graph (adjacency list): {graph}\nBFS start: {start}\nBFS order: {order}\n"
    print(s)
    with open(out_path, "w") as f:
        f.write(s)
    print(f"Saved output to {out_path}")
