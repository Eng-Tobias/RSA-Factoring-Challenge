#!/usr/bin/env python3
import sys

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return n, 1

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

file_name = sys.argv[1]

with open(file_name) as f:
    for line in f:
        number = int(line.strip())
        p, q = factorize(number)
        print(f"{number}={p}*{q}")
