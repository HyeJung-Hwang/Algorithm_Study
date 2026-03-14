"""
3
1 100 3
0
0
"""
"""
5
1 10 3
0
1 100 2
1 20 1
0
"""
# 입력 배열 관리: 딕셔너리
# 중간산출물(과제 스택): 스택, 가장 최근 작업을 이어서 해야해서 
# 루프: N 분 동안 , 리스트를 iterate해야함 N 번
# 루프 내에서 해야하는 일
# (1) 1로 시작하면 1분 동안 과제 처리하고 워킹에 넣기
# (1) 0으로 시작하면 과제 스택에서 pop해서 과제 처리하기
# (2) 다시 과제를 스택에 넣기

# [Check] 딕셔너리에는 순서가 있나???

import sys
input = sys.stdin.readline

N = int(input())
task_list = [list(map(int, input().strip().split(" "))) for i in range(N)] 
# print(task_list)

working_list = []
done_list = []
for i in range(N):
    task = task_list[i]

    if task[0] == 1:
        task[2] -= 1
        # print(f"task {i} done for 1 minute {task} ")
        if task[2] == 0:
            done_list.append(task)
        else:
            working_list.append(task)
    else:
        # 맨처음 들어온 task가 0으로 시작하는 경우 처리!
        if working_list:
            working_task = working_list.pop()
            # print(f"popped task {i} as {working_task }and done for 1 minute {working_task} ")
            working_task[2] -= 1
            if working_task[2] == 0:
                done_list.append(working_task)
            else:
                working_list.append(working_task)
        else:
            pass


score = 0
# print(working_list)
# print(done_list)
if done_list:
    for w_task in done_list:
        if w_task[2] == 0:
            score += w_task[1]
    print(score)
else:
    print(0)