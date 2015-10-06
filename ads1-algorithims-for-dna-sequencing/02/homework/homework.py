# Problem
#
# implement versions of the naive exact matching and Boyer-Moore
# algorithms that additionally count and return (a) the number of
# character comparisons performed and (b) the number of alignments tried.
# Roughly speaking, these measure how much work the two different
# algorithms are doing.

import bm_preproc
import bisect

def boyer_moore_with_stats(p, p_bm, t):
    """ Do Boyer-Moore matching. p=pattern, t=text,
        p_bm=BoyerMoore object for p """
    i = 0
    occurrences = []
    char_comparisons = 0
    aligns_tried = 0
    while i < len(t) - len(p) + 1:
        shift = 1
        aligns_tried += 1
        mismatched = False
        for j in range(len(p)-1, -1, -1):
            char_comparisons += 1
            if p[j] != t[i+j]:
                skip_bc = p_bm.bad_character_rule(j, t[i+j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if not mismatched:
            occurrences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += shift

    return occurrences, aligns_tried, char_comparisons

def naive_with_stats(p, t):
    occurrences = []
    char_comparisons = 0
    aligns_tried = 0
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        aligns_tried += 1
        for j in range(len(p)):  # loop over characters
            char_comparisons += 1
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences, aligns_tried, char_comparisons

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

class Index(object):
    def __init__(self, t, k):
        ''' Create index from all substrings of size 'length' '''
        self.k = k  # k-mer length (k)
        self.index = []
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer

    def query(self, p):
        ''' Return index hits for first k-mer of P '''
        kmer = p[:self.k]  # query with first k-mer
        i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

class SubseqIndex(object):
    """ Holds a subsequence index for a text T """

    def __init__(self, t, k, ival):
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex("ATAT", 2, 2)
            extracts ("AA", 0) and ("TT", 1). """
        self.k = k  # num characters per subsequence extracted
        self.ival = ival  # space between them; 1=adjacent, 2=every other, etc
        self.index = []
        self.span = 1 + ival * (k - 1)
        for i in range(len(t) - self.span + 1):  # for each subseq
            self.index.append((t[i:i+self.span:ival], i))  # add (subseq, offset)
        self.index.sort()  # alphabetize by subseq

    def query(self, p):
        """ Return index hits for first subseq of p """
        subseq = p[:self.span:self.ival]  # query with first subseq
        i = bisect.bisect_left(self.index, (subseq, -1))  # binary search
        hits = []
        while i < len(self.index):  # collect matching index entries
            if self.index[i][0] != subseq:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits

def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        mismatch = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                mismatch += 1
                if mismatch > 2:
                    match = False
                    break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

def indexMatcher():
    p = 'GGCGCGGTGGCTCACGCCTGTAAT'
    genome = readGenome('chr1.GRCh38.excerpt.fasta')
    kmer_index = Index(genome, 8)

    hits = []
    partial_matches = []
    for i in range(len(p) - 8):
        seq = p[i:]
        matches = kmer_index.query(seq)
        partial_matches += matches

        for j in range(len(matches)):
            start = matches[i] - i
            end = start + len(p)
            if len(naive_2mm(p, genome[start:end])) > 0:
                hits.append(matches[i])
    return hits, partial_matches

def q1():
    print("Question 1")
    genome = readGenome('chr1.GRCh38.excerpt.fasta')
    occurrences, aligns_tried, char_comparisons = naive_with_stats('GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG', genome)
    print("Alignments: %d" % aligns_tried)

def q2():
    print("Question 2")
    genome = readGenome('chr1.GRCh38.excerpt.fasta')
    occurrences, aligns_tried, char_comparisons = naive_with_stats('GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG', genome)
    print("Character comparisons: %d" % char_comparisons)

def q3():
    print("Question 3")
    genome = readGenome('chr1.GRCh38.excerpt.fasta')
    p = 'GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG'
    alphabet = 'AGCT'
    p_bm = bm_preproc.BoyerMoore(p, alphabet)
    occurrences, aligns_tried, char_comparisons = boyer_moore_with_stats('GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG', p_bm, genome)
    print("Alignments: %d" % aligns_tried)

def q4():
    print("Question 4")
    hits, partial_matches = indexMatcher()
    print(len(hits))

def q5():
    print("Question 5")
    hits, partial_matches = indexMatcher()
    print(len(partial_matches))

def q6():
    print("Question 6")
    genome = readGenome('chr1.GRCh38.excerpt.fasta')

    kmer_index = SubseqIndex(genome, 8, 3)

    hits = []
    p = 'GGCGCGGTGGCTCACGCCTGTAAT'
    partial_matches = []
    for i in range(len(p) - 8):
        seq = p[i:]
        matches = kmer_index.query(seq)
        partial_matches += matches

        for j in range(len(matches)):
            start = matches[i] - i
            end = start + len(p)
            if len(naive_2mm(p, genome[start:end])) > 0:
                hits.append(matches[i])
    print(len(partial_matches))

q1()
q2()
q3()
q4()
q5()
q6()
