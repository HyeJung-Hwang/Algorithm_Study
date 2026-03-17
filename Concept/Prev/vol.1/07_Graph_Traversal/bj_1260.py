"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""
from collections import deque
import sys 
input = sys.stdin.readline
N, M, V = map(int,input().strip().split(" "))
graph = [[] for i in range(N+1)] # 정점에 대해 빈 리스트를 만들고
for _ in range(M):
    u, v = map(int, input().strip().split(" "))
    graph[u].append(v)
    graph[v].append(u) # 양방향 그래프니까

def dfs(v,visited = []):
    visited.append(v)
    for next_item in graph[v]:
        if next_item not in visited:
            visited = dfs(next_item, visited)
    return visited # 탈출 조건 

def bfs(v):
    visited = set([v])
    queue = deque()
    queue.append(v)
    ans = []
    while queue:
        v = queue.popleft()
        ans.append(v)
        for next_item in graph[v]:
            if next_item not in visited:
                visited.add(next_item)
                queue.append(next_item)
    return ans
# def bfs(graph,V):
#     visited = set([V])
#     queueu = deque()
#     queue.append(V)
if __name__ == "__main__":

    

    # print(graph)
    dfs_ans = dfs(V,[])
    print(" ".join(map(str,dfs_ans)))
    bfs_ans = bfs(V)
    print(" ".join(map(str,bfs_ans)))
    

