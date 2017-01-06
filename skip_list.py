#!/usr/bin/env python3
import random

class SLNode(object):
    def __init__(self, level, key, value):
        self.key = key
        self.value = value
        self.forward = [None] * level


class SkipList(object):
    def __init__(self, max_level):
        self.MAX_LEVEL = max_level
        self.m_level = 0
        self.m_length = 0
        self.header = SLNode(self.MAX_LEVEL, 0, 0)

    def search(self, key):
        p = self.header

        for i in range(self.m_level)[::-1]:
            while p.forward[i] and p.forward[i].key <= key:
                if p.forward[i].key == key:
                    return p.forward[i].value
                p = p.forward[i]

        return None

    def insert(self, key, value):
        level = self.random_level()
        update = SLNode(self.MAX_LEVEL, 0, 0)
        p = self.header

        for i in range(self.m_level)[::-1]:
            while p.forward[i] and p.forward[i].key <= key:
                if p.forward[i].key == key:
                    p.forward[i].value = value
                    return
                p = p.forward[i]
            update.forward[i] = p

        newNode = SLNode(level, key, value)

        if level > self.m_level:
            temp = level
            while level > self.m_level:
                update.forward[level-1] = self.header
                level -= 1
            self.m_level = temp
            level = temp

        for i in range(level):
            newNode.forward[i] = update.forward[i].forward[i]
            update.forward[i].forward[i] = newNode

        self.m_length += 1

    def random_level(self):
        level = 1
        while level <= self.MAX_LEVEL:
            if random.randint(0, 1):
                level += 1
                if level > self.m_level:
                    self.m_level += 1
                    return self.m_level
            else:
                return level
        return level

    def delete(self, key):
        update = SLNode(self.MAX_LEVEL, 0, 0)
        p = self.header

        level = 0
        for i in range(self.m_level)[::-1]:
            while p.forward[i] and p.forward[i].key <= key:
                if p.forward[i].key == key:
                    level += 1
                    break
                p = p.forward[i]
            update.forward[i] = p

        if not update.forward[0]:
            return False

        for i in range(level):
            if update.forward[i]:
                update.forward[i].forward[i] = update.forward[i].forward[i].forward[i]

        i = self.m_level-1
        while i >= 0 and not self.header.forward[i]:
            self.m_level -= 1
            i -= 1

        self.m_length -= 1
        return True

    def show(self):
        count_list = []
        for i in range(self.m_level)[::-1]:
            p = self.header.forward[i]
            count = 0
            while p:
                print('(%d,%d)-->' % (p.key, p.value), end='')
                p = p.forward[i]
                count += 1
            print('None')
            count_list.append(count)

        print(count_list)





skip_list = SkipList(20)
for i in range(1000)[::-1]:
    skip_list.insert(i, i)

delSet = set()
for i in range(1000):
    delSet.add(random.randint(0,999))

print(skip_list.m_level)
print(skip_list.m_length)

for item in delSet:
    skip_list.delete(item)

missList = []
hitList = []
for i in range(1000):
    if skip_list.search(i) is not None:
        hitList.append(i)
    else:
        missList.append(i)


print(skip_list.m_level)
print(skip_list.m_length)
print(len(hitList))
print(len(missList))
print(len(delSet))

if len(missList) == len(delSet):
    delList = list(delSet)
    missList.sort()
    delList.sort()
    count = 0
    for i in range(len(missList)):
        if missList[i] != delList[i]:
            count += 1

    print(count)
