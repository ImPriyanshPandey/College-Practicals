#!/usr/bin/env python3
"""
Q6: Counting Sort (non-comparison sort). Assumes non-negative integers.
Subject: Design and Analysis of Algorithms
"""
from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return []
    k = max(arr)
    count = [0]*(k+1)
    for x in arr:
        count[x] += 1
    # prefix sums for stable version
    total = 0
    for i in range(len(count)):
        total += count[i]
        count[i] = total
    out = [0]*len(arr)
    for x in reversed(arr):
        count[x] -= 1
        out[count[x]] = x
    return out

if __name__ == "__main__":
    out_path = "Q6_counting_sort_output.txt"
    tests = [
        [4,2,2,8,3,3,1],
        [0,5,3,1,2,5,4,0],
        [9,9,9,1,0,2],
    ]
    lines = []
    for t in tests:
        s = counting_sort(t)
        line = f"Input: {t}\nSorted: {s}\n"
        lines.append(line)
        print(line)
    with open(out_path, "w") as f:
        f.write("\n".join(lines))
    print(f"\nSaved output to {out_path}")
