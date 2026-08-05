#!/usr/bin/env python3
"""
Q2: Merge Sort with number of key comparisons (during merge).
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple

def merge(left, right):
    i = j = 0
    merged = []
    comps = 0
    while i < len(left) and j < len(right):
        comps += 1  # compare left[i] <= right[j]
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comps

def merge_sort(arr: List[int]) -> Tuple[List[int], int]:
    if len(arr) <= 1:
        return arr[:], 0
    mid = len(arr)//2
    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])
    merged, c3 = merge(left, right)
    return merged, c1 + c2 + c3

if __name__ == "__main__":
    out_path = "Q2_merge_sort_output.txt"
    demo_out = []
    tests = [
        [12, 11, 13, 5, 6],
        [5,4,3,2,1],
        [1,2,3,4,5],
        [12, 11, 13, 5, 6, 7, 3, 9, 0, 4]
    ]
    for t in tests:
        s, c = merge_sort(t)
        line = f"Input: {t}\nSorted: {s}\nComparisons: {c}\n"
        demo_out.append(line)
        print(line)
    with open(out_path, "w") as f:
        f.write("\n".join(demo_out))
    print(f"\nSaved output to {out_path}")
