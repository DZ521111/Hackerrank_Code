#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop
from collections import defaultdict

# Complete the shortestReach function below.
def shortestReach(n, edges, s):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    visited = [True for _ in range(n + 1)]
    distance = [float("inf") for _ in range(n + 1)]
    distance[s] = 0
    minHeap = [(distance[s], s)]

    while minHeap:
        d, u = heappop(minHeap)
        if visited[u]:
            continue
        visited[u] = True
        for w, v in graph[u]:
            if not visited[v] and distance[v] > d + w:
                distance[v] = d + w
                heappush(minHeap, (distance[v], v))
    del distance[s]
    del distance[0]
    return [-1 if d == float("inf") else d for d in distance]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
