class Node:
    def __init__(self,v):
        self.v = v
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,v):
        if self.root == None:
            self.root = Node(v)
        else:
            self._insert(self.root,v)
    def _insert(self,curr,v):
        if curr == None:
            curr = Node(v)
            return

        if v<curr.v and curr.left!=None:
            self._insert(curr.left,v)
        elif v>curr.v and curr.right!=None:
            self._insert(curr.right,v)

        if v<curr.v and curr.left==None:
            curr.left = Node(v)
        elif v>curr.v and curr.right==None:
            curr.right = Node(v)


    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,curr):
        if curr == None:
            return 
        self._inorder(curr.left);
        print(curr.v)
        self._inorder(curr.right);

t = Tree()
t.insert(50)
t.insert(10)
t.insert(20)
t.insert(60)
t.insert(80)
t.insert(70)
t.inorder()