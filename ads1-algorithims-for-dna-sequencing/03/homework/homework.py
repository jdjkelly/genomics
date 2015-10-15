#!/usr/bin/python
# vim: set fileencoding=utf-8

import bisect

def readGenome(filename):
  genome = ''
  with open(filename, 'r') as f:
    for line in f:
      # ignore header line with genome information
      if not line[0] == '>':
        genome += line.rstrip()
  return genome

def editDistance(p, t, debug=False):
    # Create distance matrix
    D = []
    for i in range(len(p)+1):
        D.append([0]*(len(t)+1))
    # Initialize first row and column of matrix
    for i in range(len(p)+1):
        D[i][0] = i 
    # Fill in the rest of the matrix
    for i in range(1, len(p)+1):
        for j in range(1, len(t)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if p[i-1] == t[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    # Edit distance is the value in the bottom right corner of the matrix
    for i in range(len(t)):
      D[len(p)-1][i]

    if debug:
      printEditDistanceMatrix(D, p, t)

    minimum = []
    for i in range(len(t)):
      minimum.append(D[len(p)][i])
    return min(minimum)
  
def printEditDistanceMatrix(matrix, p, t):
    p = "e" + p
    t = "e" + t
    print "  ",
    for i in range(len(t)):
      print '{0: <2}'.format(t[i]),
    print "\n"
    for i in range(len(p)):
      print '{0: <2}'.format(p[i]),
      for j in range(len(t)):
        print '{0: <2}'.format(matrix[i][j]),
      print "\n"

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def q1():
  genome = readGenome('chr1.GRCh38.excerpt.fasta')
  ed = editDistance('GCTGATCGATCGTACG', genome)  
  print(ed)

def q2():
  genome = readGenome('chr1.GRCh38.excerpt.fasta')
  ed = editDistance('GATTTACCAGATTGAG', genome)
  print(ed)

def q3():
  reads, _ = readFastq('ERR266411_1.for_asm.fastq')
  overlap_all_pairs(reads, 30)

def overlap_all_pairs(reads, min_length):
  index = {}
  for i in range(len(reads)):
    for j in range(len(reads[i]) - min_length + 1):
      key = reads[i][j:j+min_length]
      if (key in index):
        index[key].add(reads[i])
      else:
        index[key] = set([reads[i]])
  hits = []
  edged_nodes = set()
  for i in range(len(reads)):
    suffix = reads[i][len(reads[i])-min_length:]
    if (suffix in index):
      for indexed in index[suffix]:
        if overlap(reads[i], indexed, min_length) >= min_length and reads[i] != indexed:
          hits.append((reads[i], indexed))
          edged_nodes.add(reads[i])
  print("%d distinct pairs" % len(hits))
  print(hits[400])
  print("%d nodes with at least one outgoing edge" % len(edged_nodes))

q1()
q2()
q3()
