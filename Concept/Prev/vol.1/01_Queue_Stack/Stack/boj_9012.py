"""
6
(())()) NO
(((()())() No
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""
"""
NO
NO
YES
NO
YES
NO
"""
# [),),),(,(,(,]
# 앞에서 부터 또는 뒤에서 부터 탐색
# 탐색하면서 봐야하는 내용 : ()가 fail하면 NO -> (.().  다음에 나와야한나느게 ), (나오면 break [MIstake] 끝까지 와뱌할 수도

# 쓸 자료 구조 : 스택, 경로 저장이 필요한 문제라서
# 넣고 pop 하는게 필요하다 !!!! 
# 탐색한 괄호를 저장하다가, 가장 마지막에 있는 요소랑, 들어올 요소를 비교해서 ()가 완성되면 가장 마지막에 있는 요소를 pop해야함
# pop 한 요소를 또 스택으로 관리해야하나 ????
# [  ) ) ( 에서 또 ) 들어오면 No ]

# 루프 에서 해야하는 작업
# 1. 문자열 뒤에서부터 pop
# 2. 탐색 경로 스택의 마지막 요소랑 비교해서 ()가 되면 탐색 경로 스택 pop  안되면 append
import sys
input = sys.stdin.readline

N = int(input())
candidates_stack = [] 
# for i in range(N):
#     candidates_stack.append(input().strip())

candidates_stack = [input().strip()  for  i in range(N)] 
# print(candidates_stack  )
result_stack = []
# 길이 상관 없이 break 만 잘하면 되어서 , [Check] 끝까지 봐야, vps인 걸 알면, 복잡도가 커지려나 n^2될까?

ans = []
for candidate in candidates_stack:
    candidate_stack = list(candidate)
    # print(candidate_stack)
    search_stack = []
    for i in range(len(candidate)):
        # 
        check = candidate_stack.pop() # (
        if not search_stack:
            search_stack.append(check)
            # pass
            # print(f"search stack empty insert {check}  to {search_stack}")
        else:
            # print(f"check string = {check+search_stack[-1]}")
            if search_stack[-1] == check:
                search_stack.append(check)
                # print(f"added {check} in  {search_stack}")
                # print(f"{search_stack[:-1]} {check}")
            elif check+search_stack[-1] == "()":
                # print(f"popped {search_stack[-1]} & {check}")
                search_stack.pop()
            else:   
                break

    if search_stack:
        ans.append("NO")
    else:
        ans.append("YES")

# print(ans)
print("\n".join(ans))

