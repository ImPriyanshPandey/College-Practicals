#!/usr/bin/env python3
"""
Q8: Display the data stored in a given graph using DFS.
Graph given as adjacency list. Print DFS order from a start node.
Subject: Design and Analysis of Algorithms
"""
from typing import Dict, List

def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    visited = set()
    order = []
    def rec(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                rec(v)
    rec(start)
    return order

if __name__ == "__main__":
    out_path = "Q8_dfs_output.txt"
    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: [4],
        4: []
    }
    start = 0
    order = dfs(graph, start)
    s = f"Graph (adjacency list): {graph}\nDFS start: {start}\nDFS order: {order}\n"
    print(s)
    with open(out_path, "w") as f:
        f.write(s)
    print(f"Saved output to {out_path}")
