from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.h = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h:
            self.h[key] = [(timestamp, value)]
        else:
            self.h[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h:
            return ""
        arr = self.h[key]
        if timestamp >= arr[-1][0]:
            return arr[-1][1]
        l, r = 0, len(arr) -1

        while l < r:
            mid = l + (r-l) // 2

            if arr[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid

        if arr[l][0] == timestamp:
            return arr[l][1]
        return "" if l == 0 else arr[l - 1][1]     


# Time Complexity: O(log n) for get, O(1) for set
# Space Complexity: O(m)


class TimeMap:

    def __init__(self):
        self.h = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.h[key]
        l, r = 0, len(arr) -1
        res = ""

        while l <= r:
            mid = l + (r-l) // 2

            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res     


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Time Complexity: O(log n) for get, O(1) for set
# Space Complexity: O(m)