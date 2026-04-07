# 이중 연결 리스트 (Doubly Linked List)

> 프로그래머스 - 표 편집 문제를 통해 학습

---

## 문제 요약

행을 선택/삭제/복구하는 명령어 기반 표 편집 프로그램

| 명령어 | 설명 |
|--------|------|
| `U X` | 현재 선택된 행에서 X칸 위 행 선택 |
| `D X` | 현재 선택된 행에서 X칸 아래 행 선택 |
| `C` | 현재 선택된 행 삭제 후 바로 아래 행 선택 (마지막 행이면 윗 행) |
| `Z` | 가장 최근 삭제된 행 복구 (현재 선택된 행은 변경 없음) |

---

## 왜 리스트로 풀면 안 되는가?

- `C` 명령어마다 삭제 후 뒤 원소를 앞으로 당김 → **O(n)**
- 최악의 경우 O(n × cmd 수) = O(1,000,000 × 200,000) → **시간 초과**

---

## 이중 연결 리스트란?

각 노드가 **앞 노드(prev)** 와 **뒤 노드(next)** 양쪽을 모두 가리키는 자료구조

```
단방향: [A] → [B] → [C] → [D]
이중:   [A] ⇄ [B] ⇄ [C] ⇄ [D]
```

---

## 배열로 구현하는 방법

노드 객체 대신 **`prev[]`, `next[]` 배열 2개**로 연결 관계를 표현

### 초기 상태 (행 5개: 0~4번)

```
0번행: 어피치
1번행: 콘
2번행: 라이언  ← 현재 선택
3번행: 네오
4번행: 튜브
```

```python
인덱스:  0    1    2    3    4
prev = [-1,   0,   1,   2,   3]   # -1 = 위에 없음
next = [ 1,   2,   3,   4,   5]   # 5  = 아래에 없음
```

- `prev[2] = 1` → 2번행의 윗 행은 1번행
- `next[2] = 3` → 2번행의 아랫 행은 3번행

---

### 삭제 (C) - O(1)

1번행(콘)을 삭제할 때, 배열에서 실제로 지우지 않고 **이웃 정보만 수정**

```python
# 삭제 전
next = [1, 2, 3, 4, 5]
prev = [-1, 0, 1, 2, 3]

next[prev[1]] = next[1]   # 0번의 next를 2번으로
prev[next[1]] = prev[1]   # 2번의 prev를 0번으로

# 삭제 후 연결 흐름
# 0 ⇄ 2 ⇄ 3 ⇄ 4  (1번은 연결에서 제외, 배열엔 여전히 존재)
```

리스트처럼 뒤 원소를 당길 필요 없이 포인터 2개만 바꾸면 끝 → **O(1)**

---

### 복구 (Z) - O(1)

삭제 시 스택에 `(삭제된 행, prev, next)` 저장해두면:

```python
deleted.append((1, prev[1], next[1]))  # (1, 0, 2) 저장

# 복구 시
row, p, nx = deleted.pop()   # (1, 0, 2)
next[p] = row    # 0번의 next를 다시 1번으로
prev[nx] = row   # 2번의 prev를 다시 1번으로

# 0 ⇄ 1 ⇄ 2 ⇄ 3 ⇄ 4  원상복구
```

---

## 전체 풀이 코드

```python
def solution(n, k, cmd):
    prev = list(range(-1, n - 1))
    next = list(range(1, n + 1))

    deleted = []  # (삭제된 행, prev, next)
    cur = k

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                cur = prev[cur]
        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                cur = next[cur]
        elif c[0] == 'C':
            deleted.append((cur, prev[cur], next[cur]))
            if prev[cur] != -1:
                next[prev[cur]] = next[cur]
            if next[cur] != n:
                prev[next[cur]] = prev[cur]
            cur = next[cur] if next[cur] != n else prev[cur]
        elif c[0] == 'Z':
            row, p, nx = deleted.pop()
            if p != -1:
                next[p] = row
            if nx != n:
                prev[nx] = row

    deleted_set = {row for row, _, _ in deleted}
    return ''.join('X' if i in deleted_set else 'O' for i in range(n))
```

---

## 시간 복잡도

| 연산 | 복잡도 |
|------|--------|
| C (삭제) | O(1) |
| Z (복구) | O(1) |
| U/D X | O(X) |
| 전체 | O(n + cmd + 모든 X의 합) |

> U/D가 O(X)이지만, 제한사항에 "모든 X의 합 ≤ 1,000,000" 이 보장되므로 전체적으로 효율적

---

## 배열로 구현하는 이유

코딩테스트에서는 노드 객체보다 배열이 유리:
- 객체 생성 비용 없음 → 메모리/속도 유리
- n이 100만이면 Node 100만개보다 배열 2개가 훨씬 가벼움

### 같은 패턴이 쓰이는 곳

| 자료구조 | 배열 표현 |
|---------|----------|
| 연결 리스트 | `prev[]`, `next[]` |
| 트리 | `parent[]`, `left[]`, `right[]` |
| 그래프 | `adj[]` (인접 리스트) |

**핵심: "관계"를 배열 인덱스로 표현하는 것**
