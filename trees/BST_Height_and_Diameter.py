class TreeNode:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,v):
        if self.root == None:
            self.root = TreeNode(v)
        else:
            self._insert(self.root,v)
    def _insert(self,curr,v):
        if v<curr.val and curr.left==None:
            curr.left = TreeNode(v)
        elif v>curr.val and curr.right==None:
            curr.right = TreeNode(v)

        if v<curr.val and curr.left!=None:
            self._insert(curr.left,v)
        elif v>curr.val and curr.right!=None:
            self._insert(curr.right,v)

    def inorder(self):
        self._inorder(self.root)
        print("")
    def _inorder(self,curr):
        if curr==None:
            return
        self._inorder(curr.left)
        print(curr.val,end=" ")
        self._inorder(curr.right)

    def height(self):
        return self._height(self.root)
    def _height(self,curr,h=0):
        if curr == None:
            return 0
        else:
            lh = self._height(curr.left)
            rh = self._height(curr.right)
            return max(lh,rh)+1

    def diameter(self):
        return self._diameter(self.root)
    def _diameter(self,curr):
        if curr == None:    
            return 0

        lh = self._height(curr.left)
        rh = self._height(curr.right)

        ld = self._diameter(curr.left)
        rd = self._diameter(curr.right)

        return max(lh+rh+1,max(ld,rd))

t = Tree()
t.insert(50)
t.insert(10)
t.insert(20)
t.insert(5)
t.insert(80)
t.inorder()
print("height : "+str(t.height()))
print("diameter : "+str(t.diameter()))