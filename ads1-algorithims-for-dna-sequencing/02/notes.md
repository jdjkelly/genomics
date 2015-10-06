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
  - Tables are reusable-
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

- Suffix index
  - Sort all suffixes in alphabetical order
  - Query via binary search
  - n(n+1)/2 or N^2+1/2
  - Suffix arry
    - organizes via ordering
  - Suffix tree
    - Unlike suffix array organizes via grouping vs ordering
  - FM Index
    - Very compact

- k-mer index size variablility:
  - use offsets strategy to reduce size of index - trade off requires increasing # of queries needed to determine if there's a m - use offsets strategy to reduce size of index - trade off requires increasing # of queries needed to determine if there's a match
- subsequence of s: string of chars also occuring in s in the same order
  - all substrings are sequences, not all sequences are substrings

- Approximate matching, Hamming and edit distance
  - Algos for exact matches are not going to be sufficient for DNA analysis because of sequencing
    errors etc
  - Haming distance is the minimum # substituions needed to turn one into the other
  - Levenshtein idstance is the minimum # edits (subs, inserts, dels) needed to turn one into the other
    - X/Y are not required to be the same length
