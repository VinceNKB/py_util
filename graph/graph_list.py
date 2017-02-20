#!/usr/bin/env python3

class Graph_list(object):
    def __init__(self, adj_list = [], nodenum = 0, edgenum = 0, directed = True):
        self.adj_list = adj_list
        self.nodenum = nodenum
        self.edgenum = edgenum
        self.nodeId = set([id for id in range(nodenum)])
        self.directed = directed
        # self.getNodenum()
        # self.getEdgenum()

    def getNodenum(self):
        self.nodenum = len(self.adj_list)

    def getEdgenum(self):
        self.edgenum = sum([len(x) for x in self.adj_list])

    def addNode(self):
        self.adj_list.append([])
        self.nodenum += 1



