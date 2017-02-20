#!/usr/bin/env python3

class Graph_matrix(object):
    def __init__(self, maps = [], edgenum = 0, directed = True):
        self.directed = directed
        self.maps = maps
        self.nodenum = len(maps)
        self.edgenum = edgenum
        self.nodeId = set([id for id in range(len(maps))])
        self.NOT_CONNECT = float('inf')
        # self.getNodenum()
        # self.getEdgenum()

    def addNode(self):

        for i in range(self.nodenum):
            self.maps[i].append(self.NOT_CONNECT)

        self.maps.append([self.NOT_CONNECT] * (self.nodenum + 1))
        self.nodeId.add(self.nodenum)
        self.nodenum += 1

    def delNode(self, id):
        if id in self.nodeId:
            self.nodeId.remove(id)
            if self.directed:
                for i in range(self.nodenum):
                    if self.maps[i][id] != self.NOT_CONNECT:
                        self.maps[i][id] = self.NOT_CONNECT
                        self.edgenum -= 1

                    if self.maps[id][i] != self.NOT_CONNECT:
                        self.maps[id][i] = self.NOT_CONNECT
                        self.edgenum -= 1
                return True
            else:
                for i in range(self.nodenum):
                    if self.map[i][id] != self.NOT_CONNECT:
                        self.maps[i][id] = self.NOT_CONNECT
                        self.maps[id][i] = self.NOT_CONNECT
                        self.edgenum -= 1
                return True
        else:
            return False

    def addEdge(self, i, j, val):
        if i in self.nodeId and j in self.nodeId:
            if self.directed and self.maps[i][j] == self.NOT_CONNECT:
                self.maps[i][j] = val
                self.edgenum += 1
                return True
            elif not self.directed and self.maps[i][j] == self.NOT_CONNECT and self.maps[j][i] == self.NOT_CONNECT:
                self.maps[i][j] = val
                self.maps[j][i] = val
                self.edgenum += 1
                return True
            else:
                return False
        else:
            return False

    def updateEdge(self, i, j, val):
        if i in self.nodeId and j in self.nodeId:
            if self.directed:
                self.maps[i][j] = val
                self.edgenum += 1 if self.maps[i][j] == self.NOT_CONNECT else 0
            else:
                self.maps[i][j] = val
                self.maps[j][i] = val
                self.edgenum += 1 if self.maps[i][j] == self.NOT_CONNECT else 0
        else:
            return False

    def delEdge(self, i, j):
        if i in self.nodeId and j in self.nodeId:
            if self.directed and self.maps[i][j] != self.NOT_CONNECT:
                self.maps[i][j] = self.NOT_CONNECT
                self.edgenum -= 1
                return True
            elif not self.directed and self.maps[i][j] != self.NOT_CONNECT and self.maps[j][i] != self.NOT_CONNECT:
                self.maps[i][j] = self.NOT_CONNECT
                self.maps[j][i] = self.NOT_CONNECT
                self.edgenum -= 1
                return True
            else:
                return False
        else:
            return False

    def checkMaps(self):
        row_num = len(self.maps)
        for col in self.maps:
            if len(col) != row_num:
                return False

        if not self.directed:
            for i in range(self.nodenum):
                if self.maps[i][i] != self.NOT_CONNECT:
                    return False
            for i in range(self.nodenum):
                for j in range(i+1, self.nodenum):
                    if self.maps[i][j] != self.maps[j][i]:
                        return False
        return True

    def getNodenum(self):
        if self.checkMaps():
            self.nodenum = len(self.maps)
        else:
            self.nodenum = 0
            raise Exception

    def getEdgenum(self):
        self.edgenum = 0
        if self.directed:
            for i in range(self.nodenum):
                for j in range(self.nodenum):
                    if self.maps[i][j] != self.NOT_CONNECT:
                        self.edgenum += 1
        else:
            for i in range(self.nodenum):
                for j in range(i+1, self.nodenum):
                    if self.maps[i][j] != self.NOT_CONNECT:
                        self.edgenum += 1

    def getEdge(self):
        if self.directed:
            edge = []
            for i in range(self.nodenum):
                for j in range(self.nodenum):
                    if self.maps[i][j] != self.NOT_CONNECT:
                        edge.append((i, j, self.maps[i][j]))
            return edge
        else:
            edge = []
            for i in range(self.nodenum):
                for j in range(i+1, self.nodenum):
                    if self.maps[i][j] != self.NOT_CONNECT:
                        edge.append((i, j, self.maps[i][j]))
            return edge

    def getWeight(self, i, j):
        if i in self.nodeId and j in self.nodeId:
            return self.maps[i][j]
        else:
            return self.NOT_CONNECT

    def getOutNode(self, i):
        if i in self.nodeId:
            out_node = [j for j in range(self.nodenum) if self.maps[i][j] != self.NOT_CONNECT]
            return out_node
        else:
            return []

    def getInNode(self, j):
        if j in self.nodeId:
            in_node = [i for i in range(self.nodenum) if self.maps[i][j] != self.NOT_CONNECT]
            return in_node
        else:
            return []

if __name__ == '__main__':
    graph = Graph_matrix(directed = False)
    graph.addNode()
    graph.addNode()
    graph.addNode()
    graph.addEdge(0,1,1)
    graph.addEdge(1,2,3)
    graph.addEdge(2,0,2)
    graph.checkMaps()
