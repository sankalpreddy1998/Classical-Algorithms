class Node:
    def __init__(self,v):
        self.left = None
        self.val = v
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
        if v>curr.val and curr.right==None:
            curr.right = Node(v)
        if v<curr.val and curr.left!=None:
            self._insert(curr.left,v)
        if v>curr.val and curr.right!=None:
            self._insert(curr.right,v)

    def inorder(self):
        st = []
        curr = self.root

        while True:
            if curr!=None:
                st.append(curr)
                curr = curr.left
            else:
                if len(st)==0: break
                curr = st.pop()
                print(curr.val)
                curr = curr.right

    def preorder(self):
        st = []
        st.append(self.root)

        while len(st):
            x = st.pop()
            print(x.val)
            if x.right!=None:
                st.append(x.right)
            if x.left!=None:
                st.append(x.left)

    # def postorder(self):
    #     st = []
    #     curr = self.root

    #     while true:
    #         if curr!=None:
    #             st.append(curr)
    #             curr = curr.left
    #         if st[-1].right==None:
    #             print(st[-1].val)
    #             prev = st.pop()
    #             if st[-1].right == prev:


            

t = Tree()
t.insert(50)
t.insert(10)
t.insert(20)
t.insert(60)
t.insert(80)
t.insert(70)
t.preorder()