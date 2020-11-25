class Node:
    def __init__(self,val):
        self.val = val
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
        
        if v<curr.val and curr.left==None:
            curr.left = Node(v)
        elif v>curr.val and curr.right==None:
            curr.right = Node(v)

        if v<curr.val and curr.left!=None:
            self._insert(curr.left ,v)
        elif v>curr.val and curr.right!=None:
            self._insert(curr.right ,v)

    def inorder(self):
        self._inorder(self.root)
    def _inorder(self,curr):
        if curr==None:
            return
        self._inorder(curr.left)
        print(curr.val)
        self._inorder(curr.right)


    def path(self,v):
        l = []
        self.findPath(self.root,v,l)
        return l
    def findPath(self,curr,v,l):
        while(curr!=None):
            l.append(curr.val)
            if v<curr.val:
                curr = curr.left
            elif v>curr.val:
                curr = curr.right
            else:
                break

t = Tree()
t.insert(50)
t.insert(10)
t.insert(20)
t.insert(60)
t.insert(80)
t.insert(70)
t.insert(90)
# t.inorder()
print(t.path(90))