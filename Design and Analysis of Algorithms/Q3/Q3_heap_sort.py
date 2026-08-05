#!/usr/bin/env python3
"""
Q3: Heap Sort with number of key comparisons (element-to-element).
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple

def heapify(a, n, i):
    comps = 0
    while True:
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n:
            comps += 1
            if a[l] > a[largest]:
                largest = l
        if r < n:
            comps += 1
            if a[r] > a[largest]:
                largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            i = largest
        else:
            break
    return comps

def heap_sort(arr: List[int]) -> Tuple[List[int], int]:
    a = arr[:]
    n = len(a)
    comps = 0
    # Build heap (max-heap)
    for i in range(n//2 - 1, -1, -1):
        comps += heapify(a, n, i)
    # Extract elements
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        comps += heapify(a, i, 0)
    return a, comps

if __name__ == "__main__":
    out_path = "Q3_heap_sort_output.txt"
    demo_out = []
    tests = [
        [12, 11, 13, 5, 6],
        [5,4,3,2,1],
        [1,2,3,4,5],
        [12, 11, 13, 5, 6, 7, 3, 9, 0, 4]
    ]
    for t in tests:
        s, c = heap_sort(t)
        line = f"Input: {t}\nSorted: {s}\nComparisons: {c}\n"
        demo_out.append(line)
        print(line)
    with open(out_path, "w") as f:
        f.write("\n".join(demo_out))
    print(f"\nSaved output to {out_path}")
