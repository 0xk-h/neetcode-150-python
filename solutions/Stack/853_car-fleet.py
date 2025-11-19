from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = [(target - pos) / s  for pos, s in zip(position, speed)]
        ind = sorted(range(len(temp)), key = lambda i: -position[i])
        time = [temp[i] for i in ind]

        res = 1
        curr = time[0]
        for i in time:
            if i > curr:
                res += 1
                curr = i

        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        res = 0
        curr = -1

        for pos, s in cars:
            time = (target - pos) / s
            if time > curr:
                res += 1
                curr = time

        return res
    
# Time Complexity: O(n log n)
# Space Complexity: O(n)

