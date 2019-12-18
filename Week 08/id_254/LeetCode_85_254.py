class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
      if not matrix:
          return 0
      m = len(matrix)
      n = len(matrix[0])

      height = [0]*n
      left = [0]*n
      right = [n]*n
      maxarea = 0

      for i in range(m):
        curr_left, curr_right = 0, n
        for j in range(n):
          if matrix[i][j] == '1':
            height[j] += 1
          else:
            height[j] = 0
        for j in range(n):
          if matrix[i][j] == '1':
            left[j] = max(left[j], curr_left)
          else:
            left[j] = 0
            curr_left = j+1
        for j in range(n-1, -1, -1):
          if matrix[i][j] == '1':
            right[j] = min(right[j], curr_right)
          else:
            right[j] = n
            curr_right = j
        for j in range(n):
          maxarea = max(maxarea, height[j]*(right[j]-left[j]))
      return maxarea
