- Shortest common superstring problem
  - NP-complete
  - Idea: pick order for strings in S and construct superstring
  - Try all possible orderings and pick shortest superstring
  -  If S contains n strings, n! possible orderings

- Greedy shortest common superstring
  - Use a process of graphs, and reduction/concatenation to find shortest common substring

- Third law of assembly
  - Because of the repetitive nature of the genome, finding the
    shortest superstring, will tend to take the repetitive parts
    and collapse them down to a shorter string than they really
    are
  - Repetitive sequences cause ambiguity
  - Repeats make assembly difficult

- De Bruijn Graphs and Eulerian walks
  - De Bruijn is a directed graph
  - "Tomorrow and tomorrow and tomorrow"
    - "Tomorrow" <-> "and"
    - Can have more than one edge between the nodes
  - "AAABBBBA"
    - 3-mers: AAA, AAB, ABB, BBB, BBB, BBA
    - Extract each k-1 mers from each mer:
      - AAA -> 'AA' and 'AA'
    - Create edges between pair of k-1 mer
    - One edge per k-mer
    - One node per distinct k-1-mer
    - Reconstruct the genome by:
      - Walk crossing each edge exactly once (Eulerian Walk)

- Eulerian walks
  - Problems:
    - Multiple walks are possible

- Assemblers in practice
  - Polypolidy 


