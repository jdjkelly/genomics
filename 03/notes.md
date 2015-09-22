- Solving the edit distance problem
  ```
    def edDistRecursive(a, b):
      if len(a) == 0:
        return len(b)
      if len(b) == 0:
        return len(a)
      delt = 1 if a[-1] != b[-1] else 0
      return min(edDistRecursive(a[:-1], b[:-1]) + delt,
                 edDistRecursive(a[:-1], b) + 1,
                 edDistRecursive(a, b[:-1]) + 1)
  ```
- Dynamic program algorithims:
  - Reduce large problems into small ones
  - Optimize out repetition

