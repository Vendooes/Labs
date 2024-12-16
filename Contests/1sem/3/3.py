class Node:
    def __init__(self,base):
        self.base = base
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.impot = None
    
    def find(self,node,parent,value):
        if node is None:
            return None, parent, False
        if value == node.base:
            return node,parent,True

        if value<node.base:
            if node.left:
                return self.find(node.left,node,value)

        if value>node.base:
            if node.right:
                return self.find(node.right,node,value)

        return node,parent,False   

    def app(self,noun):
        if self.impot is None:
            self.impot = noun
            return noun
        
        s,p,fl_find = self.find(self.impot, None,noun.base)

        if not fl_find and s:
            if noun.base < s.base:
                s.left = noun
            else:
                s.right = noun

    def show(self,node):
        if node is None:
            return
        self.show(node.left)
        if node.left is None and node.right is None:
            print(node.base, end=' ')
        self.show(node.right)

    def delit_leaf(self,s,p):
        if p.left == s:
            p.left - None
        elif p.right == s:
            p.right = None

    def delit(self,key):
        s,p,fl_find = self.find(self.impot, None,key)
        if not fl_find:
            return None
        if s.left is None and s.right is None:
            self.delit_leaf(s,p)

n = list(map(int,input().split()))
seq = list(map(int, input().split()))

t = Tree()
for i in seq:
    t.app(Node(i))
t.show(t.impot)
