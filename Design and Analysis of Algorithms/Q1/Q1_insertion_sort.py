#!/usr/bin/env python3
"""
Q1: Insertion Sort with number of key comparisons.
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple

def insertion_sort(arr: List[int]) -> Tuple[List[int], int]:
    a = arr[:]  # work on a copy
    comps = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Count only element-to-element comparisons (a[j] > key)
        while j >= 0:
            comps += 1  # comparing a[j] > key
            if a[j] > key:
                a[j+1] = a[j]
                j -= 1
            else:
                break
        a[j+1] = key
    return a, comps

def demo():
    data = [12, 11, 13, 5, 6, 7, 3, 9, 0, 4]
    sorted_arr, comparisons = insertion_sort(data)
    print("Input:", data)
    print("Sorted:", sorted_arr)
    print("Comparisons:", comparisons)

if __name__ == "__main__":
    out_path = "Q1_insertion_sort_output.txt"
    demo_out = []
    # Run a few demos
    tests = [
        [12, 11, 13, 5, 6],
        [5,4,3,2,1],
        [1,2,3,4,5],
        [12, 11, 13, 5, 6, 7, 3, 9, 0, 4]
    ]
    for t in tests:
        s, c = insertion_sort(t)
        demo_out.append(f"Input: {t}\nSorted: {s}\nComparisons: {c}\n")
        print(demo_out[-1])
    with open(out_path, "w") as f:
        f.write("\n".join(demo_out))
    print(f"\nSaved output to {out_path}")
