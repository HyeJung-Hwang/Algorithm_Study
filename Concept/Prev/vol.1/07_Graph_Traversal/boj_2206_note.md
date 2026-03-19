# BOJ 2206 - 벽 부수고 이동하기

## 문제 핵심

BFS에서 **벽을 한 번 부술 수 있다**는 조건을 어떻게 처리할까?

---

## 접근 방식 비교

### BF로 벽 위치 일일이 선택하는 방식 (비효율)

```
벽1 부수고 BFS → 최단경로 계산
벽2 부수고 BFS → 최단경로 계산
벽3 부수고 BFS → 최단경로 계산
...
전부 다 해보고 최솟값 선택
```

벽마다 BFS를 새로 돌리는 거라 엄청 느림.

---

### flag를 상태에 포함시키는 방식 (정답)

BFS는 원래 "내가 지금 어떤 상태인지"를 큐에 넣는 자료구조.

- 일반 BFS: `(r, c)` → 위치만 상태
- 이 문제: `(r, c, flag)` → 위치 + 벽 사용 여부가 상태

BFS가 퍼져나가면서 각 경로가 알아서 벽을 쓸지 말지 결정:

```
경로A: (0,0,0) → (0,1,0) → 벽 만남 → (0,2,1) 부쉈다
경로B: (0,0,0) → (1,0,0) → (1,1,0) → 우회해서 감
```

두 경로가 **동시에** BFS 안에서 탐색됨.
벽을 어디서 부술지 미리 정하지 않아도, BFS가 퍼져나가면서 "부수는 경로", "안 부수는 경로"를 자동으로 다 탐색.

**한 줄 요약**: BF는 벽을 미리 골라서 BFS를 여러 번 돌리는 것, flag 방식은 BFS 한 번 안에서 모든 선택지를 동시에 탐색하는 것.

---

## BFS 큐 = 탐색 예정 노드 관리 + 상태

큐에 넣는 단위 = **노드를 완전히 설명하는 상태**

일반 미로에서는 `(r, c)` 만으로 노드를 완전히 설명할 수 있음.

근데 이 문제는:
```
(r, c) 만으로는 부족함

(2, 3)에 도달했다고 해도
→ 벽을 쓰고 온 건지
→ 벽을 안 쓰고 온 건지
에 따라 앞으로 갈 수 있는 경우가 달라짐
```

그래서 노드를 완전히 설명하려면 `(r, c, flag)` 가 필요.

> **"상태" = "이 노드를 탐색하기 위해 필요한 모든 정보"**
> 큐에 넣는 단위가 상태고, 문제에 따라 그 상태가 뭘 담아야 하는지가 달라짐.

---

## 이동 규칙 (분기)

일반 BFS랑 완전히 동일한 구조에서, **벽을 만났을 때 분기 하나만 추가**:

```
다음 칸이 빈 칸 → 그냥 이동 (기존 BFS와 동일)
다음 칸이 벽   → 부순다 / 못 간다 (분기 추가)
```

`visited[r][c][flag]` 의 역할: 같은 칸이어도 벽 사용 여부가 다르면 다른 상태로 취급해서 두 경로를 모두 탐색.

---

## 구현

```python
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    # visited[r][c][flag] : flag=0(벽 안 부숨), flag=1(벽 부숨)
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0, 1))  # (row, col, flag, dist)
    visited[0][0][0] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, flag, dist = queue.popleft()

        if r == N-1 and c == M-1:
            print(dist)
            return

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if grid[nr][nc] == '0':
                # 빈 칸: flag 유지
                if not visited[nr][nc][flag]:
                    visited[nr][nc][flag] = True
                    queue.append((nr, nc, flag, dist+1))

            elif grid[nr][nc] == '1' and flag == 0:
                # 벽인데 아직 안 부쉈으면: 부수고 이동
                if not visited[nr][nc][1]:
                    visited[nr][nc][1] = True
                    queue.append((nr, nc, 1, dist+1))

    print(-1)

bfs()
```
