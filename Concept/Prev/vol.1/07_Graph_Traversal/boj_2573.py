"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""
# 입력: 그래프
# 알고리즘: BFS()
# 1) 1년 진행 후 , 멀티소스 BFS로 빙산 전부 탐색하기 ,(다른 빙산이 바다가 되는 거로 인해 녹는게 달라져서 ) 
# 2) 덩어리 개수 세기 (dfs로 방문해서 방문경로에 현재 빙산 노드들 다 안들어가면 덩아리가 2개 이상인거로 간주 )

import sys
input = sys.stdin.readline
from collections import queue

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(queue):
    while queue:
        u,v = queue.popleft()

        for i in range(4):
            nx,ny = u+ dx[i], v+dy[i]
            if 0<= nx < N and 0<= ny < M:
                if not visited[nx][ny]: # [Mistake]계속하는 실수
                    if graph[nx][ny] == 0:
                        graph[u][v] -= 1
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
def dfs(u,v, stack = []):
    stack.append((u,v))
    for i in range(4):
        nx,ny = u+ dx[i], v+dy[i]
        if 0<= nx < N and 0<= ny < M:
            if visited[nx][ny]:
                dfs(nx, ny,stack)

    return stack

if __name__ == "__main__":
    N, M = map(int,input().strip().split(" "))
    graph = [ list(map(int,input().strip().split(" "))) for _ in range(N)]
    # print(N,M)
    # print(graph)
    year_cnt = 1
    while True:
        year_cnt += 1
        # dist에 대해 bfs] [Mistake]
        for i in range(N):
            for j in range(M):
                if graph[i][j]:
                    queue.append((i,j))
        visited = [ [0]*M for _ in range(N)] 
        bfs(queue)
        ice_list = []
        for i in range(N):
            for j in range(M):
                ice_list.append((i,j))
        now_ice_list = dfs()
        if len(now_ice_list) != len(ice_list):
            break
        # dfs로 덩어리 수 세가 (아무 시작점에 대해 
    print(year_cnt)