class Node:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,v):
        if self.root==None:
            self.root = Node(v)
        else:
            self._insert(self.root,v)
    def _insert(self,curr,v):
        if v<curr.val and curr.left==None:
            curr.left = Node(v)
        elif v>curr.val and curr.right==None:
            curr.right = Node(v)

        if v<curr.val and curr.left!=None:
            self._insert(curr.left,v)
        elif v>curr.val and curr.right!=None:
            self._insert(curr.right,v)

    def inorder(self):
        self._inorder(self.root)
        print("")
    def _inorder(self,curr):
        if curr == None:
            return
        self._inorder(curr.left)
        print(curr.val,end=" ")
        self._inorder(curr.right)

    def sum(self):
        return self._sum(self.root)
    def _sum(self,curr):
        if curr==None:
            return 0
        lsm = self._sum(curr.left)
        rsm = self._sum(curr.right)
        return lsm+rsm+curr.val

    def max(self):
        return self._max(self.root)
    def _max(self,curr):
        if curr==None:
            return -99999
        lmx = self._max(curr.left)
        rmx = self._max(curr.right)
        return max(curr.val,max(lmx,rmx))

    def size(self):
        return self._size(self.root)
    def _size(self,curr):
        if curr==None:
            return 0
        lsz = self._size(curr.left)
        rsz = self._size(curr.right)
        return lsz+rsz+1


t = Tree()
t.insert(50)
t.insert(10)
t.insert(20)
t.insert(60)
t.insert(80)
t.insert(70)
t.inorder()
print("Max : "+ str(t.max()))
print("Sum : "+ str(t.sum()))
print("Size : "+ str(t.size()))