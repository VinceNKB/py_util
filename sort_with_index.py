#!/usr/bin/env python3


# 将要排序的数组
to_sort = [9,8,7,6,5,4,3,2,1]
# 给数组设置index
index = range(len(to_sort))
# 使用zip组合
new_list = [x for x in zip(to_sort, index)]
# 排序
new_list = sorted(new_list, key=lambda x:x[0])

print(new_list)

'''
[(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)]
'''