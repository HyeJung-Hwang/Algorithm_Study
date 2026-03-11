''''
Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow
'''
import sys
input_full = sys.stdin
input = sys.stdin.readline

# [Mistake] 몇 개 들어오는 지 모르는 경우 어떻게 처리 ??
# [Mistake] species_list = list(map(str.strip(), input_full()))\
# check_string = input_full

# print(check_string)
species_list = list(map(str.strip, input_full))
print(species_list)
# # print(len(set(species_list)))
# # 그대로 리스트 로 받아야함
# # 만들어야하는 딕셔너리 = {key: list에서 key가 나오는 횟수}
# # [Check] 리스트를 전부 순회해야하는짘 O(n), 보통 알고리즘에서 O(N)이면 통과하는지
# ans_dict = {}
# for specie in species_list:
#     ans_dict.setdefault(specie,0)
#     ans_dict[specie] += 1
# total = len(species_list)
# for key, value in sorted(ans_dict.items()):
#     # print(key,value)
#     print(f"{key} {value/total*100:.4f}")
# ans
# 사전 순은 sorted(dictioary_items())로 처리