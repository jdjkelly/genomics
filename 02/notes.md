- Boyer-Moore
  - Similar to naive exact matching
  - Still checks alignments, but clever
  - Benchmark exact matching algo
  - Learn from character comparisons to skip pointless alignment
  - Try alignments in left-to-righ, try character comparisons in right-to-left
  - Bad character rule: skip alignments until:
    - Mismatch becomes a match
    - P moves past mismatched character
  - Good suffix rule:
    - Find a substring in P that matches the existing match
  - Use bad character or good suffix rule, whichever skips more
    - implements lookup table for skips

- Preprocessing		 
  - Make lookup tables for bad character * good suffix rules
  - Tables are reusable
  - Cost of preprocessing is ammortized over many problems
  - Algorithim that preprocesses T (the text) is offline. Otherwise, algo is online

- K-Mer Index
  - k-mer is a "pieced" or "split" index of a text
  - Not all index hits lead to matches
  - Data structures for k-mer indicies
    - Key/value pair of k-mer -> offset, ordered (alphabetically)
      - Queried via binary search
      - Python 'bisect' implements binary search functions
        - bisect_left(a, x): leftmost offset where x can be inserted in to a to maintain order
    - Hash table