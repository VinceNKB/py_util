#!/usr/bin/env python3

import os


# 1. 遍历文件夹
# 有两种方法。第一种是直接获取文件树中的所有文件夹及文件，第二种是递归遍历
# 所以第二种方法可以用来输出文件树

def visit1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            print(os.path.join(root, f))

def visit2(rootDir):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print(path)
        if os.path.isdir(path):
            visit2(path)


def visit3(rootDir, level=1):
    if level==1: print(rootDir)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        print('│  '*(level-1)+'│--'+lists)
        if os.path.isdir(path):
            visit3(path, level+1)

# if __name__ == '__main__':
#     visit3('E:\\code\\py_util')






if __name__ == '__main__':
    pass