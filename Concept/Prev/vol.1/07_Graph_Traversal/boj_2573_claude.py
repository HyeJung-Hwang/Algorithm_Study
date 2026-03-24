import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(u, v, ice_set):
    visited = set()
    visited.add((u,v))
    queue = deque([(u,v)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (nx,ny) in ice_set and (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny))
    return visited

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    ice_set = {(i,j) for i in range(N) for j in range(M) if graph[i][j]}

    year_cnt = 0
    while True:
        year_cnt += 1

        # 1년 녹이기
        melt_cnt = {}
        for (i,j) in ice_set:
            melt_cnt[(i,j)] = sum(1 for k in range(4) if not graph[i+dx[k]][j+dy[k]])

        new_ice_set = set()
        for (i,j) in ice_set:
            graph[i][j] = max(0, graph[i][j] - melt_cnt[(i,j)])
            if graph[i][j]:
                new_ice_set.add((i,j))
        ice_set = new_ice_set

        # 다 녹았으면 0 출력
        if not ice_set:
            year_cnt = 0
            break

        # 덩어리 체크
        si, sj = next(iter(ice_set))
        now_ice = bfs(si, sj, ice_set)

        if len(now_ice) != len(ice_set):
            break

    print(year_cnt)
