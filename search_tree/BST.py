#!/usr/bin/env python3

from search_tree import TreeNode

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, z):
        y = None
        x = self.root

        while not x:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z
        elif z.val < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u, v):
        '''
        用v替换u
        '''
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if not v:
            v.parent = u.parent

    def delete(self, z):
        if not z.left:
            self.transplant(z, z.left)
        elif not z.right:
            self.transplant(z, z.right)
        else:
            y = z.right
            while not y.left:
                y = y.left
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def search(self, root, val):
        if not root or root.val == val:
            return root

        if val < root.val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)

    

