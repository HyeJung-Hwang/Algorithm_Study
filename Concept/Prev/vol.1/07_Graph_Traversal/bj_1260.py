"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
import sys 
input = sys.stdin.readline
N, M, V = map(int,input().strip().split(" "))

graph = [[] for i in range(N+1)] # 정점에 대해 빈 리스트를 만들고
for _ in range(M):
    u, v = map(int, input().strip().split(" "))
    graph[u].append(v)

def dfs(graph, V):
    visited = set([V])
    stack = list(V)
    while stack:
        v = stack.pop()

        for i in graph[v]:
            visited + # 방문처리 
            # 자식들 다 stack에 넣기
            # 재귀 호춣

def bfs(graph,V):
    visited = set([V])
    queueu = deque()
    queue.append(V)