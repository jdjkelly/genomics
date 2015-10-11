## Polymarese Chain Reaction

- Sequencing requires many identical copies of DNA
- DNA "hybridizes" 
  - "Sticks to itself"
  - Directional
  - The fact that DNA sticks to itself is an important property for PCR
- Primers
  - Short sequence - 15 to 20 bases long 
  - Complementary to the DNA we want to copy
- Process
  - Melt (heath up gently)
    - Two strands fall apart
    - Also known as Denaturation
  - Anneal (cool down gently)
    - Primers will stick to the DNA
  - Add copier molecule: DNA polymerase
    - What our cells use to copy our own DNA
    - DNA polymerase looks for a place where it's partly single/partly double and starts to copy
  - Add raw nucleotides
    - Used by the polymerase to complete the chain
  - Each round doubles the number of DNA strands you have
    - 30 cycles - 2^30 == 2 billion

## Next Generation Sequencing

- Process
  - Chop DNA up into single stranded fragments and attach to a slide
  - Use PCR to create copies "clustering"
  - Add color labeled nucleotides
    - Chemically modified with "terminators"
    - Polymerase can't continue 
    - Means a single base is only added with each sequence
  - Photograph the slide
  
## Next Generation Sequencing Applications

- Exome sequencing
  - Exome is a collection of Exones in your genome
  - Exon?
    - DNA gets transcribed to RNA
    - RNA gets chopped up into Exons and Introns
    - Exones get concatenated together, Intrones get thrown away
    - Exones get translated into proteins
    - If you want to know what the proteins are that are being turned on in a cell you need to know what the Exones are
  - When we're looking for genetic mutations, we're looking for mutations that effect proteins
  - Those mutations should occur in Exones, so we sequence just those (1.5% of genome)
  - We take the DNA molecule, fragment it
- RNA sequencing
  - Tries to capture the genes turned on in a cell
  - DNA gets transcribed to RNA then translated to proteins
  - If we can capture RNA we can tell which genes are being turned on
  - An important feature of RNA is after transcription, the cell attaches a long string of As to it
  - Anything that doesn't have As (poly-A-tail) we can ignore 
  - We can capture them by T-primers
  - Reverse transcribe into complementary DNA (cDNA)
    - Go from RNA to DNA (reverse)
    - Once we have DNA, we sequence
- ChipSeq
  - Tries to address the problem of where in the DNA certain proteins might bind
  - Some genes are inhibited in certain cell types via "transcription factors"
    - Proteins bind
  - "Cross-linking" proteins
    - Sticks protein in binding location
    - We can take the DNA where the protein is stuck, fragment it
    - Using "anti-body" pulldown, we'll pull out the fragments that are bound
    - Sequence the pulled-down fragments
- MethylSeq
  - Method of determining where the DNA is methylated 
  - Methylation is an epigenetic modification that effects which proteins are expressed
  - Methylation marks can be passed on as the cells divided
    - Attach only to Cs
  - Split your DNA into 2 identical samplse (aliquots)
  - Treat 1 of them in a special way
    - Converts all of the Cs that aren't methylated into Us
  - Sequence both, and compare
    - Us will match Cs
