from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
      if not str:
          return -1

      arr = Counter(s)
      for inx, val in enumerate(s):
        if arr[val] == 1:
          return inx

      return -1
