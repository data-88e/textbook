#!/usr/bin/env python
# coding: utf-8

# # Reading Economics Papers

# In upper division economics courses, you'll often read economics papers that utilize ordinary least squares to conduct regression. Now that we have familiarized ourselves with multi-variate regression, let's familiarize ourselves with reading the results of economics papers!
# 
# Let's consider an existing empirical study conducted by David Card {cite}`11reading-econ-papers`, a Nobel Prize winning professor at UC Berkeley, that regresses income on education:
# 
# ![](https://i.imgur.com/FPLII4s.png)
# 
# Every column here is from a different regression: the first column predicts the log hourly earnings from years of education, the fifth column predicts the log annual earnings from years of education, and so on. For now, let's focus on the first column, which states the linear regression as follows: 
# 
# $$
# \ln{(\text{hourly earnings})_i} = \alpha + \beta \cdot (\text{years of schooling})_i + \varepsilon_i
# $$
# 
# From the table, the education coefficient is 0.100, with a (0.001) underneath it. This means that our $\beta$ value is equal to 0.100. What does the (0.001) mean? It is the standard error, which is essentially a measure of our uncertainty. From Data 8, the standard error is most similar to the standard deviation of sample means, which is a measure of the spread in the population mean. Similarly, the the standard error here is a measure of the spread in the population coefficient. We can use the standard error to construct a confidence interval of the actual coefficient: a 95% confidence interval is between 2 standard errors above and below the reported value.
# 
# The effects of schooling on income is captured by the education coefficient term: 0.100. This means that an increase in 1 unit (year) of education is correlated with a log hourly earnings by 0.1. This approximately corresponds to a 10% increase in wages per year of schooling.

#  
