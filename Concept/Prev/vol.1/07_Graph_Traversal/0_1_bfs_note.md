# 0-1 BFS

## 핵심 질문: 왜 visited 대신 dist 비교가 필요할까?

---

## 일반 BFS가 visited만으로 충분한 이유

모든 간선 비용이 **동일(1)** 하기 때문에, 먼저 도달한 게 무조건 최단.

```
한 번 방문 = 최단경로로 방문했다는 보장
```

---

## 0-1 BFS는 그 보장이 없음

비용이 0과 1이 섞여 있어서, **나중에 도달해도 더 짧을 수 있음.**

```
경로A: N → (x+1) → (x+2)  비용 1+1 = 2  (먼저 도달)
경로B: N → (2*N) → ...     비용 0+... = ? (나중에 도달했지만 더 짧을 수도)
```

그래서 같은 칸을 **더 짧은 비용으로 다시 도달하면 업데이트** 해줘야 함.

```python
if dist[x] + cost < dist[nx]:   # 지금 경로가 기존보다 짧으면
    dist[nx] = dist[x] + cost   # 갱신하고
    queue.append(nx)             # 다시 탐색
```

---

## appendleft vs append

```python
if cost == 0:
    queue.appendleft(nx)  # 비용 0 → 앞에 삽입 (우선 탐색)
else:
    queue.append(nx)      # 비용 1 → 뒤에 삽입 (나중에 탐색)
```

비용 0인 이동은 현재 비용과 동일하므로 앞에 넣어서 먼저 처리.
이렇게 해야 dist가 단조증가 순서로 처리되어 올바른 최단경로 보장.

---

## 일반 BFS vs 0-1 BFS 비교

| | 일반 BFS | 0-1 BFS |
|---|---|---|
| **간선 비용** | 모두 동일(1) | 0 또는 1 |
| **중복 방문 처리** | visited 체크 | dist 비교로 갱신 |
| **큐 삽입** | 뒤에만 (append) | 0이면 앞, 1이면 뒤 |
| **먼저 도달 = 최단?** | O | X |

---

## 한 줄 요약

일반 BFS: 먼저 도달 = 최단 → visited로 충분
0-1 BFS: 먼저 도달 ≠ 최단 → dist 비교로 갱신 필요

---

## 예제 코드 (숨바꼭질)

```python
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
```
