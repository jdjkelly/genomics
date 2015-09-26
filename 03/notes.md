- Solving the edit distance problem

    def edDistRecursive(a, b):
      if len(a) == 0:
        return len(b)
      if len(b) == 0:
        return len(a)
      delt = 1 if a[-1] != b[-1] else 0
      return min(edDistRecursive(a[:-1], b[:-1]) + delt,
                 edDistRecursive(a[:-1], b) + 1,
                 edDistRecursive(a, b[:-1]) + 1)

- Dynamic program algorithims:
  - Reduce large problems into small ones
  - Optimize out repetition

- Approximate matching
  - Imagine different lengths (p and t) in a matrix
  - Initialize row with 0s
    - We don't know ahead of time where P is going to occur within T
    - P's offset  could be anywhere in T
  - Initialize columns with ascending integers
  - Find the lowest value in the final row, and trace back to the starting co-ordinate (by reversing the rules)

- Global and local alignment
  - Purines
    - Adenine & guanine (AG)
      - Substitutions of this kind are called transitions
  - Pyrimidines 
    - Cytosine and Thymine (CT)
      - Substitutions of this kind are called transitions
  - Subsitutions between Purines and Pyrimidines are called transverions
  - Human transition to transversion ratio is ~ 2.1

- Assembly problem:
  - Reconsturct genome from sequencing reads
  - Coverage: amount of redunant info we have about the genome

- Two laws of assembly
  - If a suffix of read A is similar to a prefix of read B then A and B might overlap in the genome
  - More coverage leads to more and longer overlaps

- Overlap graphs
  - Each node is a read
  - Draw directed edge A->B when suffix of A overlaps prefix of B
