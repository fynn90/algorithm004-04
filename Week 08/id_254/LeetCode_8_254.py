class Solution:
    def myAtoi(self, str: str) -> int:
      if not str or not str.lstrip():
          return 0

      s = str.lstrip()
      i = 2 if s[0] == '-' or s[0] == '+' else 1
      last = 0
      while i <= len(s):
        try:
          last = int(s[:i])
          i += 1
        except:
          break

      if last <= -2147483648:
        return -2147483648
      elif last >= 2147483647:
        return 2147483647

      return last
