#!/usr/bin/env python3
"""
Q4: Quick Sort with number of key comparisons (during partition using Lomuto).
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple

def partition(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    comps = 0
    for j in range(lo, hi):
        comps += 1  # a[j] <= pivot comparison
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[hi] = a[hi], a[i+1]
    return i+1, comps

def quick_sort_recursive(a, lo, hi):
    comps = 0
    if lo < hi:
        p, c = partition(a, lo, hi)
        comps += c
        c1 = quick_sort_recursive(a, lo, p-1)
        c2 = quick_sort_recursive(a, p+1, hi)
        comps += c1 + c2
    return comps

def quick_sort(arr: List[int]) -> Tuple[List[int], int]:
    a = arr[:]
    comps = quick_sort_recursive(a, 0, len(a)-1) if a else 0
    return a, comps

if __name__ == "__main__":
    out_path = "Q4_quick_sort_output.txt"
    demo_out = []
    tests = [
        [12, 11, 13, 5, 6],
        [5,4,3,2,1],
        [1,2,3,4,5],
        [12, 11, 13, 5, 6, 7, 3, 9, 0, 4]
    ]
    for t in tests:
        s, c = quick_sort(t)
        line = f"Input: {t}\nSorted: {s}\nComparisons: {c}\n"
        demo_out.append(line)
        print(line)
    with open(out_path, "w") as f:
        f.write("\n".join(demo_out))
    print(f"\nSaved output to {out_path}")
