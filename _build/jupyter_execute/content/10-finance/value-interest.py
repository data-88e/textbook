#!/usr/bin/env python
# coding: utf-8

# # Present Value, Future Value, and Interest Rates

# ## The Time Value of Money
# 
# An important concept that is the basis for most of finance is the *time value of money*: money now is worth more than money in the future. This makes sense; you would rather have \$100 now than later. But what if I owed you money and I really wanted to postpone the payment? In order to compensate you for your bias toward having money as soon as possible, I would need to pay more than I owed. Otherwise, you might not tolerate a delayed payment. This idea of an extra payment to address time concerns is called *interest*. There is also a dimension of risk as well. If you had reason to doubt my ability to repay you in the future, you might charge me more interest to compensate for this risk.

# ```{admonition} Definition
# **Interest** is payment at a particular rate for the use of money or for delaying the repayment of money. Interest is typically set at a specific rate and that rate fluctuates based on the amount of time between borrowing and repayment, the risk of default, and other factors determined by the lender.
# ```

# ## Interest
# 
# Interest is at the heart of loans, fixed income securities (think bonds), and financial economics in general. We are familiar with the bank account: you give a certain amount of money to a financial institution, and they compensate you for allowing them to use your money to invest in other assets. What they pay you for keeping your money is interest, and is normally quantified as a percentage of what you deposit with them - an interest rate. Thus, for each \$1 deposited at the bank, you will receive $r$ dollars in interest, where $r$ is the interest rate quoted by the bank. Note that $r$ takes the form of a decimal value: 0.05, for instance, and not 5%.
# 
# Interest can be paid out in different time intervals - usually monthly, quarterly, yearly or continuously. Also, if you earn some interest in one year, in the next year you will not only earn interest on the initial amount you deposited, but also on the amount you earned the year before. This reflects the idea of *compounding interest*. We are able to determine how much \$1 will be worth in $t$ years, when compounding $n$ times per year at an interest rate of $r$.
# 
# $$\begin{aligned}
# \text{Value of 1 dollar in } t \text{ years} &= 1 \times \left(1 + \dfrac{r}{n} \right) \times \left(1 + \dfrac{r}{n} \right) \times \cdots \times \left(1 + \dfrac{r}{n} \right) \\
# &= 1 \left(1 + \dfrac{r}{n} \right)^{nt}
# \end{aligned}$$
# 
# Take a look at the table below for an example of the effects of compounding.
# 
# |                        | Bank 1: 5\% annual compounding | Bank 2: 5\% semi-annual compounding                       |
# |------------------------|--------------------------------|-----------------------------------------------------------|
# | January 2016           | \$100                          | \$100                                                     |
# | July 2016              |                                | $100 \left(1 + \dfrac{0.05}{2} \right) =$ \$102.50        |
# | January 2017           | $100 (1 + 0.05) =$ \$105       | $102.50 \left(1 + \dfrac{0.05}{2} \right) =$ \$105.0625   |
# | July 2017              |                                | $105.0625 \left(1 + \dfrac{0.05}{2} \right) =$ \$107.69   |
# | January 2018           | $105 (1 + 0.05) =$ \$110.25    | $107.69 \left(1 + \dfrac{0.05}{2} \right) =$ \$110.38     |
# | Total Percent Change   | 10.25%                         | 10.38%                                                    |
# 
# Notice that instead of a $5\% \cdot 2 = 10\%$ increase, you end up receiving a 10.25% or 10.38% increase depending on the rate of compounding. This is because the interest you received in the first compounding period (in bank 1’s case, a year, in bank 2’s case, half a year) is added onto your initial deposit, and this new deposit is used for calculating interest in the next period. Thus, even a small amount of money can grow quickly under interest rate compounding.

# ## Present Value, Future Value, and the Discount Factor
# 
# An important related concept is the idea of present and future value (which are effectively opposites). We have already discussed future value above. A \$100 deposit at bank 1 above has a future value of \$110.25 after 2 years. Conversely, an important question frequently asked in finance is the following:
# 
# > Given an amount of money in the future, what is its fair value today? 
# 
# In this example, what is the present value of \$110.25 at bank 1 two years in the future? Well, from the table above, \$100! This idea of present value is essential to the pricing of assets. In general, an asset's price is the present value of all expected future payments.
# 
# $$\begin{aligned}
# \text{FV of 1 dollar} &= 1 \times \left(1 + \dfrac{r}{n} \right)^{nt} \\
# \text{PV of 1 dollar} &= \dfrac{1}{\left(1 + \dfrac{r}{n} \right)^{nt}}
# \end{aligned}$$
# 
# We call $\dfrac{1}{(1 + \frac{r}{n})^{nt}}$ a *discount factor*. It discounts the value of \$1 from the future into today. This ties in with the time value of money. Since a dollar today is worth more than a dollar tomorrow, in order for you to be indifferent between receiving money today or tomorrow, the money you would receive tomorrow has to be discounted into the present by some amount that depends on the interest rate.
# 
# $$
# \text{PV} = \text{DF} \cdot \text{FV}
# $$

#  
