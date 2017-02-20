#!/usr/bin/env python3

class UF(object):
    def __init__(self, count):
        self.count = count
        self.id = [i for i in range(count)]
        self.unionCount = count

    def count(self):
        return self.count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pID = self.id[p]
        qID = self.id[q]

        if pID == qID:
            return

        self.unionCount -= 1
        for i in range(len(self.id)):
            if self.id[i] == pID:
                self.id[i] = qID

    def getSets(self):
        remainId = set()

        for index in self.id:
            remainId.add(index)

        tmpSet = []

        for index in remainId:
            tmpList = []
            for i in range(len(self.id)):
                if self.id[i] == index:
                    tmpList.append(i)
            tmpSet.append(tmpList)

        return tmpSet