import sys

class MinHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0 for i in range(self.maxsize+1)]
        self.Heap[0] = -1*sys.maxsize

    # position functions
    def isLeaf(self,pos):
        if pos>=self.size//2 and pos<=self.size:
            return True
        return False

    # swap function
    def swap(self,fpos,spos):
        self.Heap[fpos],self.Heap[spos] = self.Heap[spos],self.Heap[fpos]

    # insert function
    def insert(self,v):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.Heap[self.size] = v

        curr = self.size

        while self.Heap[curr] < self.Heap[curr//2]:
            self.swap(curr,curr//2)
            curr = curr // 2

    # print function
    def Print(self):
        for i in range(1,self.size//2+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 

    def minHeapify(self,pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[2*pos] or self.Heap[pos] > self.Heap[2*pos+1]:
                if self.Heap[2*pos] < self.Heap[2*pos+1]:
                    self.swap(pos,2*pos)
                    self.minHeapify(2*pos)
                else:
                    self.swap(pos,2*pos+1)
                    self.minHeapify(2*pos+1)    
    def minHeap(self):
        for i in range(self.size//2,0,-1):
            self.minHeapify(i)

    def remove(self):
        popped = self.Heap[1]
        self.Heap[1] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(1)
        return popped

if __name__ == "__main__": 
    
    minHeap = MinHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove())) 
    print("The Min val is " + str(minHeap.remove())) 
    print("The Min val is " + str(minHeap.remove())) 