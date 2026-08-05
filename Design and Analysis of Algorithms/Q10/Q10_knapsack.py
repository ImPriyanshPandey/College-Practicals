#!/usr/bin/env python3
"""
Q10: 0-1 Knapsack problem (DP). Prints maximum value and chosen items.
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(weights)
    # dp[i][w]: max value using first i items with capacity w
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        wt = weights[i-1]
        val = values[i-1]
        for w in range(capacity+1):
            dp[i][w] = dp[i-1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-wt] + val)
    # reconstruct chosen items
    w = capacity
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen.append(i-1)
            w -= weights[i-1]
    chosen.reverse()
    return dp[n][capacity], chosen

if __name__ == "__main__":
    out_path = "Q10_knapsack_output.txt"
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 8]
    capacity = 5
    best, chosen = knapsack_01(weights, values, capacity)
    s = []
    s.append(f"Weights: {weights}")
    s.append(f"Values : {values}")
    s.append(f"Capacity: {capacity}")
    s.append(f"Max value: {best}")
    s.append(f"Chosen item indices: {chosen} (0-based)")
    out = "\n".join(s) + "\n"
    print(out)
    with open(out_path, "w") as f:
        f.write(out)
    print(f"Saved output to {out_path}")
