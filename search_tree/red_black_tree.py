#!/usr/bin/env python3

from search_tree import TreeNode

class RBT(object):
    def __init__(self):
        self.NIL = TreeNode()
        self.NIL.color = 'B'
        self.root = TreeNode()
        self.root.color = 'B'
        self.root.parent = self.NIL

        
