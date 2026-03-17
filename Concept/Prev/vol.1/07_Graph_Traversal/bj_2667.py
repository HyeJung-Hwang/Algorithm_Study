"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
# 입력 배열 관리 : 그래프
# 알고리즘: 전체 데이터에 대해 다 봐야해서 DFS
# 시작점을 여러개로 dfs를 여러번 호출헤야하지 않을까?
# 루플르 돌되 1이 있는 지점에 대해, 앞선 단지에 1이 속해있으면 pass

import sys
input = sys.stdin.readline

N = int(input())
graph =[list(map(int, input().strip())) for _ in range(N)] # [ [int(c) for c in input().strip().split()] for _ in range(N) ]
# [Mistake] 문자열은 이미하나하나가 원소다
# print(graph)
visited = [[0 for _ in range(N)] for _ in range(N)]
# print(visited)
result = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
    size = 1
    visited[i][j] = 1
    for _ in range(4):
        nx, ny = i + dx[_], j + dy[_]
        if  0<= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                size += dfs(nx,ny)
    return size

for i in range(N):                                                        
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:  # 미방문 집이면       
            size = dfs(i, j)   # 이 단지 탐색
            result.append(size)  

result.sort() 
print("\n".join(map(str, [len(result)]+result)))