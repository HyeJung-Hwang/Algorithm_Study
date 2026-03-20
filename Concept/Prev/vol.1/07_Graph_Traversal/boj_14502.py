"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
# 입력: 그래프(2차원 배열)
# 알고리즘:  멀티소스 BFS(최소값), 상태에 세운 벽의 수 넣기
# 고민: [바이러스를 따라가면서 탐색] / 안전영역을 따라가면서 탐색
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
# 49 -7 - 15

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(input_graph):
    queue = deque([])
    # 시작점을 뭐로 할꼬? -> 바이러스, 웬만하면 멀티소스로 구현하기.. 바이러스바다 .
    for i in range(N):
        for j in range(M):
            if input_graph[i][j] == 2:
                queue.append((i,j)) # 바이러스 위치 큐에 넣기, 벽 세운 개수도 같이 넣기

    while queue:
        x,y = queue.popleft()
        # 탐색해야 하는 내용: 상하좌우에 대해서 바이러스이면 큐에 넣기, 빈칸이면, 1로 바꾸고 cnt하기, cnt = 3이 되면 break. 
        for _ in range(4):
            nx, ny = x + dx[_], y + dy[_]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    # 바이러스면 큐잉
                    # if input_graph[nx][ny] == 2:
                    #     queue.append((nx,ny))
                    #     visited[nx][ny] = 1
                    # 빈칸이면 1로 
                    if input_graph[nx][ny] == 0:
                        input_graph[nx][ny] = 2
                        queue.append((nx,ny))
                        visited[nx][ny] = 1
                    # else:
                    #     pass
                    # 1이면 pass

    return sum( [  row.count(0) for row in input_graph]) #2차원 배열에서 0의 개수 세기, 

if __name__ == "__main__":
    N, M = map(int,input().strip().split(" "))
    graph =  [ list(map(int, input().strip().split(" "))) for _ in range(N)]
    # 3차원 배열로 정의 

    # dist = [ list(map(lambda x: (int, 0), input().strip())) for _ in range(N)] # 거리를 업데이트 할 떄 만 dist가 필요한가?

    # 모든 벽 설치 위치 조합 구하기 
    # zeros = [(r,c) for r in range(N) for c in range(M) if graph[r][c] == 0]
    walls = combinations([ (n,m) for n in range(N) for m in range(M)  if graph[n][m] == 0],3)
    # 모든 벽 설치 위치 조합에 대해 브루트포스
    ans = []
    for wall_case in walls:
        tmp_graph = [ row[:] for row in graph]
        visited = [ [0]*M for _ in range(N)]

        # wall_case로 벽 넣기
        for (i,j) in wall_case:
            tmp_graph[i][j] = 1
        ans.append(bfs(tmp_graph))
    print(max(ans))
