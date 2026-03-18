"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""
# 입력 관리 자료구조: 그래프(이차원 배열)
# 알고리즘: 최소 일수니까 BFS 예상, 가까운 레벨당 +하루 씩 1개이웃이면 +1
# 시작점 찾아서 푸는 그래프 탐색
# 시작점을 전부 찾아서 다돌려야하나 ?? 그 중 최소 값구하기
# 내가 걱정했던 케이스: 1이 여러 개인 케이스 -> 내가 생각한, for loop으로 브루트포스로 보기  -> (정답) 큐에 처음에 한 번에 다 넣으면 됨., 정답대로해야하는 이유는 , 양쪽에 익은 토마토가 있을 때 양방향에서 익어오면 빠른 경우가 있을 수 있음
dx = [-1,1,0,0]
dy = [0,0,-1,1]


from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
# # print(N,M)
# graph = [ [map(int,input().split())] for _ in range(N)]
# visited = [ [0 for _ in range(M)] for _ in range(N)]
# print(graph)
graph =[list(map(int, input().strip().split(" "))) for _ in range(M)] # [ [int(c) for c in input().strip().split()] for _ in range(N) ]
# [Mistake] 문자열은 이미하나하나가 원소다
# print(graph)
visited = [[0 for _ in range(N)] for _ in range(M)]
def bfs(queue):
    # print(i,)
    # cnt = 0
    # visited[i][j] = 1
    # queue = deque([(i,j)])
    while queue:
        u,v = queue.popleft()
        # print(f"방문할 노드 {(u,v)}")
        # cnt += 1
        for _ in range(4):
            
            nx, ny  = u + dx[_], v + dy[_]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == 0: # [Mistake] 경계 체크
                visited[nx][ny] = 1
                graph[nx][ny] = graph[u][v] + 1 
                queue.append((nx,ny))
                # print(f"added {(nx,ny)} in queue")
    
    
    # unrolled_graph = [lambda x_list: *x_list for row in graph ] [Mistake] 2차원 배열 -> 1차원 배열
    unrolled_graph = [x for row in graph for x in row]
    if 0 in unrolled_graph:
        ans = -1
    else:
        ans = max(unrolled_graph)-1
    return ans
    # return cnt
if __name__ == "__main__":
    ans = []
    queue = deque()
    sum_graph = sum([x for row in graph for x in row]) 
    if sum_graph == N*M:
        ans = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                # print(f"{ (i,j)} 에서 bfs 해보기")
                queue.append((i,j))
    ans = bfs(queue)
    print(ans)
    #             ans.append(count)
    # print(min(ans))
# ans 중 min 값으로 ans




# 예외 케이스
# 처음부터 모든 토마토 익은