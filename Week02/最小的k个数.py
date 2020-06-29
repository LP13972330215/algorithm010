class Solution:
    def getLeastNumbers(self, arr, k):
        if k == 0:
            return []
        heaplist = HeapList()
        heaplist.buildHeap(arr[:k])
        for i in arr[k:]:
            if i < heaplist.heaplist[1]:
                heaplist.delMax()
                heaplist.insert(i)
        return heaplist.heaplist[1:]

class HeapList():
    """
    大顶堆
    """
    def __init__(self):
        self.heaplist = [0]
        self.size = 0

    def buildHeap(self, alist):
         i = len(alist) // 2
         self.size = len(alist)
         self.heaplist += alist[:]
         print(i,self.heaplist)
         while i > 0:
             self.percDown(i)

             i -= 1

    def delMax(self):
        """删除堆顶最大元素"""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def insert(self, k):
        self.heaplist.append(k)
        self.size += 1
        self.percUP(self.size)

    def percUP(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]
            i //= 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.maxChild(i)
            print(i, mc)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc

    def maxChild(self, i):#获取它最大孩子的位置
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.heaplist[2 * i] > self.heaplist[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1


if __name__ == '__main__':
    # data = [3,2,1,4,5,6,7,22,33,111,3333,445]
    # t = Solution().getLeastNumbers(data ,6)
    # print(t)
    def Factorial(n):
        if n<=1:
            return 1
        return n * Factorial(n-1)
    print(Factorial(995))




