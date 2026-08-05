#!/usr/bin/env python3
"""
Q9: Minimum Spanning Tree using Prim’s algorithm on a weighted, connected, undirected graph.
Uses adjacency matrix; 0 means no edge.
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple
import math

def prim_mst(graph: List[List[int]]) -> Tuple[int, List[Tuple[int,int,int]]]:
    n = len(graph)
    in_mst = [False]*n
    key = [math.inf]*n
    parent = [-1]*n
    key[0] = 0  # start from node 0
    for _ in range(n):
        # pick min key vertex not yet included
        u = -1; minval = math.inf
        for v in range(n):
            if not in_mst[v] and key[v] < minval:
                minval = key[v]; u = v
        in_mst[u] = True
        # update neighbors
        for v in range(n):
            w = graph[u][v]
            if w != 0 and not in_mst[v] and w < key[v]:
                key[v] = w
                parent[v] = u
    edges = []
    total = 0
    for v in range(1, n):
        u = parent[v]
        w = graph[u][v]
        edges.append((u, v, w))
        total += w
    return total, edges

if __name__ == "__main__":
    out_path = "Q9_prims_output.txt"
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
    total, edges = prim_mst(graph)
    s = "Graph (adjacency matrix):\n" + "\n".join(str(row) for row in graph)
    s += f"\n\nMST total weight: {total}\nMST edges (u, v, w): {edges}\n"
    print(s)
    with open(out_path, "w") as f:
        f.write(s)
    print(f"Saved output to {out_path}")
