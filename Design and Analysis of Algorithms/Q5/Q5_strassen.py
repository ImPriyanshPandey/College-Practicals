#!/usr/bin/env python3
"""
Q5: Strassen’s algorithm for matrix multiplication (square matrices of power-of-two size;
pads with zeros if needed). Prints input matrices and result.
Subject: Design and Analysis of Algorithms
"""
from typing import List, Tuple
import math

def add(A, B):
    n = len(A); m = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]

def sub(A, B):
    n = len(A); m = len(A[0])
    return [[A[i][j] - B[i][j] for j in range(m)] for i in range(n)]

def conventional(A, B):
    n, m, p = len(A), len(A[0]), len(B[0])
    C = [[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                C[i][j] += A[i][k]*B[k][j]
    return C

def split(A):
    n = len(A)
    mid = n//2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    return A11, A12, A21, A22

def join(A11, A12, A21, A22):
    top = [a+b for a,b in zip(A11,A12)]
    bot = [a+b for a,b in zip(A21,A22)]
    return top + bot

def next_power_of_two(n):
    return 1 if n == 0 else 2**(n-1).bit_length()

def pad_matrix(A, size):
    n = len(A); m = len(A[0])
    P = [[0]*size for _ in range(size)]
    for i in range(n):
        for j in range(m):
            P[i][j] = A[i][j]
    return P

def unpad_matrix(C, rows, cols):
    return [row[:cols] for row in C[:rows]]

def strassen(A, B, threshold=64):
    n = len(A)
    if n <= threshold:
        return conventional(A, B)
    A11,A12,A21,A22 = split(A)
    B11,B12,B21,B22 = split(B)
    M1 = strassen(add(A11, A22), add(B11, B22), threshold)
    M2 = strassen(add(A21, A22), B11, threshold)
    M3 = strassen(A11, sub(B12, B22), threshold)
    M4 = strassen(A22, sub(B21, B11), threshold)
    M5 = strassen(add(A11, A12), B22, threshold)
    M6 = strassen(sub(A21, A11), add(B11, B12), threshold)
    M7 = strassen(sub(A12, A22), add(B21, B22), threshold)
    C11 = add(sub(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(sub(add(M1, M3), M2), M6)
    return join(C11, C12, C21, C22)

def multiply(A, B):
    # Pad to square power-of-two
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    assert cA == rB, "Incompatible dimensions"
    n = max(rA, cA, rB, cB)
    s = next_power_of_two(n)
    Ap = pad_matrix(A, s)
    Bp = pad_matrix(B, s)
    Cp = strassen(Ap, Bp)
    C = unpad_matrix(Cp, rA, cB)
    return C

if __name__ == "__main__":
    out_path = "Q5_strassen_output.txt"
    # Demo with 3x3 (will be padded to 4x4)
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    C = multiply(A, B)
    def mat_to_str(M):
        return "\n".join(" ".join(f"{x:5d}" for x in row) for row in M)
    s = []
    s.append("Matrix A:\n" + mat_to_str(A))
    s.append("\nMatrix B:\n" + mat_to_str(B))
    s.append("\nA x B (Strassen):\n" + mat_to_str(C))
    out = "\n".join(s)
    print(out)
    with open(out_path, "w") as f:
        f.write(out)
    print(f"\nSaved output to {out_path}")
