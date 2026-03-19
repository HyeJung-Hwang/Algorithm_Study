import sys
from collections import deque

input = sys.stdin.readline
MAX_LEN = 100001

def bfs(N, K):
    dist = [float('inf')] * MAX_LEN
    dist[N] = 0
    queue = deque([N])

    while queue:
        x = queue.popleft()

        if x == K:
            return dist[x]

        for nx, cost in [(2*x, 0), (x-1, 1), (x+1, 1)]:
            if 0 <= nx < MAX_LEN and dist[x] + cost < dist[nx]:
                dist[nx] = dist[x] + cost
                if cost == 0:
                    queue.appendleft(nx)
                else:
                    queue.append(nx)

N, K = map(int, input().split())
print(bfs(N, K))