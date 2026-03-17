"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""
# 입력 배열 관리: 그래프
# 방문 경로를 dfs로 찾아서 길이 구하기 ? (끝까지 한 방향씩, 시작 노드와 연결된 모든 방향을 다봐야해서 dfs)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v  = map(int,input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v, visited = []):
    visited.append(v)
    # print(f"add {v} in {visited}")
    for next_v in graph[v]:
        if next_v not in visited:
            visited = dfs(next_v,visited)
    return visited
    
if __name__ == "__main__":
    connected_with_v = dfs(1,[])
    print(len(connected_with_v)-1)