class MinStack:

    def __init__(self):
        self.stk = []
        self.m = float("inf")

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.m = val
        else:
            x = val - self.m
            self.stk.append(x)
            if x < 0:
                self.m = val
        

    def pop(self) -> None:
        val = self.stk.pop()
        if val < 0:
            self.m -= val

    def top(self) -> int:
        top = self.stk[-1]
        if top > 0: 
            return self.stk[-1] + self.m
        else:
            return self.m
        

    def getMin(self) -> int:
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#---------------------------------------------------------
#           Time Complexity:
#           push:    O(1)
#           pop:     O(1)
#           top:     O(1)
#           getMin:  O(n)
#           
#           Space Complexity:
#           O(1)
#---------------------------------------------------------


class MinStack:

    def __init__(self):
        self.stk = []
        self.m = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.m or self.m[-1] >= val:
            self.m.append(val)
        

    def pop(self) -> None:
        val = self.stk.pop()
        if self.m and self.m[-1] == val:
            self.m.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#---------------------------------------------------------
#           Time Complexity:
#           push:    O(1)
#           pop:     O(1)
#           top:     O(1)
#           getMin:  O(1)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------


# Brute Force Solution
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        

    def pop(self) -> None:
        self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return min(self.stk)
    
#---------------------------------------------------------
#           Time Complexity:
#           push:    O(1)
#           pop:     O(1)
#           top:     O(1)
#           getMin:  O(n)
#           
#           Space Complexity:
#           O(n)
#---------------------------------------------------------