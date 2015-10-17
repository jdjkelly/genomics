# Why Care About Stats?
- Potential for personalized medical care
- Prominent case of "Genomic signatures guide the use of chemotherapeutics"
  where chemotherapy trials were started with faulty stats

# What Went Wrong?
- What went wrong with the Duke analysis?
  - Lack of transparency. Data/code weren't reproducible
  - There was a lack of cooperation
  - Silly prediction rules 
  - Study design problems
    - Batch effects (confounder)
  - Their predictions weren't locked down

# Central Dogma of Statistics
- We have a poplation, we want to take a smaller sample of that population, and
  use statistical interference to say something about the population, and in
  particular the variability of our estimate for that population

# Data Sharing Plans
- Data set consists of:
  1. The raw data
  2. A tidy data set
  3. A code book describing each variable and its values
  4. An explicit and exact recipe you used to go from 1 -> 2,3

# Getting Help with Statistics
- CrossValidated = StackOverflow for stats

# Sample Size and Variability
- Power
  - Statistical method of resolving n, delta, sd (sample size, effect, variability)
  - In R: `power.t.test`

# Statistical Significance
- We want to know if observed differences we have in the sample are replicable or "real"
- T-Statistic
  - T = avg(y) - avg(x) / measure_of_variability
- P-value
  - Suppose we've calculated the difference between 2 curves
  - Suppose that difference is equal to 2, is that big or small?
  - Permutation test:
    - Scramble values on axis', recalculate the statistic
    - Make a histogram of random samplings
    - P-Value = average number of times the histogramed values are bigger than the calculated stats)
  ^ This seems like a terrible explanation
  - Def'n: the probability of observing a statistic as extreme if the null hypothesis is true
    - P-Value is *not* 
      - Probability the null is true
      - Probability the alternative is true
      - A measure of statistical evidence

# Multiple Testing
- Uniform distribution:
  - Flat P-value distribution (20% less than 0.2 etc)
- Error rates:
  - Family wise error rate
    - If we're going to do many hypothesis' tests, we want to control the probability there will be even one false positive
  - False discovery rate:
    - Expected number of false positives / total discoveries
- Suppose 550 out of 10000 genes are significant at 0.05 level
  - P-value < 0.05
    - Expect 0.05 * 10k = 500 false positives
  - False Discovery Rate < 0.05
    - Expect 0.05 * 550 = 27.5 false positives
  - Family Wise Error Rate < 0.05
    - The probability of at least 1 false positive < 0.05

# Study size, batch effects, confounding
- Balanced
- Replicated
- Has controls
