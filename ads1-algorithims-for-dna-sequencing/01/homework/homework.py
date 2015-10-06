import sys

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences

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


def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

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

def question1():
    numMatches = 0
    genome = readGenome('lambda_virus.fa')

    numMatches += len(naive('AGGT', genome))
    numMatches += len(naive(reverseComplement('AGGT'), genome))

    print("Question 1: %d" % numMatches)

def question2():
    numMatches = 0
    genome = readGenome('lambda_virus.fa')

    numMatches += len(naive('TTAA', genome))

    print("Question 2: %d" % numMatches)

def question3():
    genome = readGenome('lambda_virus.fa')

    matches = naive('ACTAAGT', genome)
    reverseMatches = naive(reverseComplement('ACTAAGT'), genome)

    leftMost = min(matches + reverseMatches)

    print("Question 3: %d" % leftMost)

def question4():
    genome = readGenome('lambda_virus.fa')

    matches = naive('AGTCGA', genome)
    reverseMatches = naive(reverseComplement('AGTCGA'), genome)

    leftMost = min(matches + reverseMatches)

    print("Question 4: %d" % leftMost)

def question5():
    genome = readGenome('lambda_virus.fa')

    matches = naive_2mm('TTCAAGCC', genome)

    print("Question 5: %d" % len(matches))

def question6():
    genome = readGenome('lambda_virus.fa')

    matches = naive_2mm('AGGAGGTT', genome)

    print("Question 6: %d" % matches[0])

def question7():
    sequences, qualities = readFastq('ERR037900_1.first1000.fastq')

    qualitySums = [0] * len(qualities[0])

    for quality in qualities:
        for i in range(len(quality)):
            qualitySums[i] += ord(quality[i]) - 33

    print("Question 7: %d" % qualitySums.index(min(qualitySums)))

question1()
question2()
question3()
question4()
question5()
question6()
question7()
