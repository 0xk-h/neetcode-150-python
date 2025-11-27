from sortedcontainers import SortedList
import heapq


class MedianFinder:

    def __init__(self):
        self.left = []           # max-heap
        self.right = []          # min-heap


    def addNum(self, num: int) -> None:
        x = -heapq.heappushpop(self.left, -num)
        heapq.heappush(self.right, x)
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        
        else:
            return -self.left[0]
        
#---------------------------------------------------------
#           Time Complexity:
#           addNum:           O(log n)
#           findmedian:       O(1)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------


class MedianFinder:

    def __init__(self):
        self.nums = SortedList()


    def addNum(self, num: int) -> None:
        self.nums.add(num)
        

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 0:
            return (self.nums[n//2 - 1] + self.nums[n//2]) / 2
        
        else:
            return self.nums[n//2]
        
#---------------------------------------------------------
#           Time Complexity:
#           addNum:           O(n)
#           findmedian:       O(1)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------


class MedianFinder:

    def __init__(self):
        self.left = []           # max-heap
        self.right = []          # min-heap


    def addNum(self, num: int) -> None:
        if not self.left:
            self.left.append(-num)
        elif not self.right:
            self.right.append(num)
            if -self.left[0] > num:
                self.left[0], self.right[0] = -self.right[0], -self.left[0]
        elif num > -self.left[0]:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left):
                x = heapq.heappop(self.right)
                heapq.heappush(self.left, -x)
        else:
            heapq.heappush(self.left, -num)
            if len(self.left) - 1 > len(self.right):
                x = -heapq.heappop(self.left)
                heapq.heappush(self.right, x)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        
        else:
            return -self.left[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#---------------------------------------------------------
#           Time Complexity:
#           addNum:           O(log n)
#           findmedian:       O(1)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------