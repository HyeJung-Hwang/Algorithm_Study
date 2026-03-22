# """
# 4
# 1 2
# 1 3
# 2 4
# 1 2 3 4
# """
# # 입력: 그래프 (인접리스트)
# # 알고리즘
# # 1) 인접리스트에 대해 시작점에 대해 dfs 돌리고 방문 경로(스택)을 리스트로 저장
# # 2) 리스트를 입력 string에서 가져와야하는 정보 같은 레벨의 노드들에서의 방문순서  각 노드마다 우선순위를 적용해준 뒤 탐색 하는게 필요할
# # 출력: 2) 결과


# import sys
# input = sys.stdin.readline
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def dfs(x,visited =[]):
#     visited.append(x)
#     for nx in graph[x]:
#         if 0<=nx<=N: #mistake 노드 번호 1부터셈
#             if nx not in visited:
#                 dfs(nx,visited)
#     return visited

# if __name__ == "__main__":
#     # 입출력
#     N = int(input())
#     graph = [ [] for _ in range(N+1)]
#     visited = [ ] 
#     for _ in range(1,N): # N-1번 입력 받아야함
#         u,v = map(int,input().strip().split(" "))
#         graph[u].append(v)
#         graph[v].append(u)
#     compare_ans = input().strip()

#     # dfs
#     stack = []
#     stack.append(1)
#     # x = stack.pop()

#     ans = dfs(1)
#     ans_string = " ".join(map(str,ans))
#     print(int(ans_string ==compare_ans))

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

order = list(map(int, input().split()))
priority = {node: i for i, node in enumerate(order)}  # 우선순위 부여

# 각 인접리스트를 우선순위 순으로 정렬
for node in graph:
    graph[node].sort(key=lambda x: priority[x])

# DFS 실행
result = []
visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    result.append(v)
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(1)

print(1 if result == order else 0)