#!/bin/python3

import os
import sys
import heapq

#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads):
    global s
    graph = dict()
    for i in range(1, n+1):
        graph[i] = dict()
        graph[i]["color"] = 'white'
        graph[i]["distance"] = -1
        graph[i]["neighbours"] = []
    for i in range(len(roads)):
        graph[roads[i][0]]["neighbours"].append(roads[i][1])
        graph[roads[i][1]]["neighbours"].append(roads[i][0])
    graph[s]["color"] = 'grey'
    graph[s]["distance"] = 0
    q = [s]
    l1 = [j for j in range(1, n+1) if j!=s]
    l2 = []
    while len(q):
        #print(l1)
        u = q.pop(0)
        #if graph[u]["color"] == 'black':
        #    continue
        for i in graph[u]["neighbours"]:
            if graph[i]["color"] == 'white':
                l1.remove(i)
                l2.append(i)
        for i in l1:
            graph[i]["distance"] = graph[u]["distance"] + 1
            graph[i]["color"] = 'grey'
            q.append(i)
        graph[u]["color"] = 'black'
        l1 = l2[:]
        l2 = []

    answer = []
    for i in range(1, n+1):
        if i != s:
            answer.append(graph[i]["distance"])
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
