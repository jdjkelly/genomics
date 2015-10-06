AT, Adenine/Thymine
GC, Guanine/Cytosine

- We can sequence them as strings
- Sequencer works by randomly selecting subsequences and re-rereading
	- "Reads"
	- 100 nt vs 100M nt 
	- Lots and lots of short snippets
	- Redundant information of any given base

- String definitions
	- Σ = { A, C, G, T }
	- S = number of characters in S
        - ɛ = empty string

- Python string tips:
	- s[2:6] = substring from 2 to 6
        - s[0:6] or s[:6] = first 7 starting from beginning ("Prefix")
	- s[-4:] = sufix, last 4

- DNY polymerase
	- Given a single strand + a base, the polymerase will build the complement piece by piece
	- 2nd gen sequencers watch the polymerase build

- Sequencing mistakes
	- template strands are amplified, clustered around the original strand ( many copies )
	- cluster so that light is bright enough
	- part of the cluster can get ahead of the others, if one of the bases is not terminated - so it will not block the polymerase
	- "Base Caller" - software analysis of base photographs (confidence interval)
	- "Base Quality" Q = -10 log10 p
		- Q = 10 -> 1 in 10 chance 
		- Q = 20 -> 1 in 100 chance
		- Q = 30 -> 1 in 1000 chance

- FASTQ format
	- Phred33 -> round + 33 == ascii value



