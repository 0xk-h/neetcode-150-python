from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x = []
        for val in p:
            if val == "*":
                x[-1] += val
            else:
                x.append(val)
        p = x
        m, n = len(s), len(p)

        memo = {}
        def back(i, j):
            if i == m:
                while j < n and len(p[j]) == 2:
                    j += 1
                
                return j == n

            if j >= n or i >= m:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            if len(p[j]) == 1:
                res = False
                if p[j] == "." or s[i] == p[j]:
                    res = back(i + 1, j + 1)

                memo[(i, j)] = res
                return res

            res = False
            if p[j][0] == "." or s[i] == p[j][0]:
                res = back(i + 1, j)

            memo[(i, j)] = res or back(i, j + 1)
            return memo[(i, j)]

        return back(0, 0)
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

#----------------------------------------------------------
#    All wrong ways to understand the question
#----------------------------------------------------------

# 1. u can't skip any character in p and * can be anything (eg. "si")
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @cache
        def back(i, j):
            if i == m and (j == n or (j == n - 1 and p[j] == "*")):
                return True

            if i >= m or j >= n:
                return False

            if p[j] == "." or s[i] == p[j]:
                return back(i + 1, j + 1)

            if p[j] == "*":
                return back(i + 1, j) or back(i, j + 1)

            return False

        return back(0, 0)
    
# 2. Assuming can skip any character in p and * can be anything (eg. "si")
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @cache
        def back(i, j):
            if i == m and (j == n or (j == n - 1 and p[j] == "*")):
                return True

            if i >= m or j >= n:
                return False

            if p[j] == "." or s[i] == p[j]:
                return back(i + 1, j + 1)

            if p[j] == "*":
                return back(i + 1, j) or back(i, j + 1)

            return back(i, j + 1)

        return back(0, 0)
    
# 3. Assuming can skip any character in p and * can be anylength of a same character (eg. "ssss")
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        @cache
        def back(i, j, c):
            if i == m and (j == n or (j == n - 1 and c)):
                return True

            if i >= m or j >= n:
                return False

            if p[j] == "." or s[i] == p[j]:
                return back(i + 1, j + 1, c)

            if c and s[i] != c:
                return back(i, j + 1, "")

            if p[j] == "*":
                c = c if c else s[i]
                return back(i + 1, j, c) or back(i, j + 1, "")

            return back(i, j + 1, "")

        return back(0, 0, "")
    
# 4. didnt handle ".*" case and assumes "a****" is valid
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i = 0
        nextJ = {}
        while i < n:
            if p[i] == "*":
                x = i + 1
                while x < n and p[x] == "*":
                    x += 1
                nextJ[i] = x
                i = x - 1
            i += 1

        @cache
        def back(i, j, c):
            if i == m:
                return True

            if j >= n:
                return False

            if p[j] == "." or s[i] == p[j]:
                return back(i + 1, j + 1, "")

            # The real headache starts here

            if p[j] == "*":
                c = c if c else p[j - 1]
                if c == ".":
                    c = s[i]

            if c:
                res = False
                if s[i] == c:
                    res = back(i + 1, j, c)
                
                return res or back(i, nextJ[j], "")

            return back(i, j + 1, "")

        return back(0, 0, "")
    
# 5. finds "a****" invalid but still assumes can skip any character in p
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def back(i, j, c):
            if i == m:
                return True

            if j >= n:
                return False

            if p[j] == "." or s[i] == p[j]:
                return back(i + 1, j + 1, "")

            # The real headache starts here

            if p[j] == "*":
                c = c if c else p[j - 1]
                if c == ".":
                    c = s[i]

            if c:
                res = False
                if s[i] == c:
                    res = back(i + 1, j, c)
                
                return res or back(i, j + 1, "")

            return back(i, j + 1, "")

        return back(0, 0, "")