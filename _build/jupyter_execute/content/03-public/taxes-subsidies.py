#!/usr/bin/env python
# coding: utf-8

# # Taxes and Subsidies

# Now that we have discussed cases of market equilibrium with just demand and supply, also known as free market cases, we will examine what happens when the government intervenes. In all of these cases, the market is pushed from equilibrium to a state of disequilibrium. This causes the price to change and, as a result, the quantity transacted in the market. 

# Broadly, a tax is any type of financial charge imposed by the government, such as income tax, property tax, or excise tax. In this course, and for this section in particular, we will consider only taxes levied on consumption. These taxes are typically enforced on a state level in the US, and can take 2 forms:
# 
# - An *excise tax* levies a fixed dollar amount on a particular good or service. A flat \$1 tax per packet of cigarette sold is an example of an excise tax.
# - An *ad valorem tax* levies a percentage amount on the purchase of a particular good or service. For example the sales tax is an ad valorem tax.
# 
# Notably, consumption taxes can be levied on either the producer or the consumer. The side that pays for the tax *upfront* (when a transaction occurs) is known as the party that bears the **statutory incidence** of the tax. However, as you'll soon learn, this does not mean that the party paying for the tax upfront bears the entire **economic incidence** of the tax.
# 
# A subsidy is the opposite of a tax; it involves either a monetary benefit given by the government or a reduction in taxes granted to individual businesses or whole industries.

# ## Why Tax or Subsidize?
# 
# The supply and demand models that we've examined so far do not necessarily reflect the entire picture; often, there are additional social costs or benefits associated with producing or consuming a good that is not paid for by a firm or considered by consumers. 
# 
# For example, take a factory producing dyed color T-shirts that pollute a nearby river. In a world without government intervention, the firm would not have to clean up the river even though they should include factor that into their costs. This is an example of a **negative externality**, in which the *private cost* faced in production by a firm or consumption by a consumer is lower than the actual *social cost*.

# ```{figure} fig1-negative-externality.png
# ---
# width: 500px
# name: negative-externality
# ---
# A supply-side negative externality in which the marginal social cost is greater than the marginal private cost
# ```

# ![title](fig1-negative-externality.png)

# Take another example: vaccines. By consuming a vaccine shot, a consumer benefits their communities to overall reduce transmission of a disease. However, chances are the consumer probably did not consider the social benefits when making a decision on whether to vaccinate. This is an example of a **positive externality**, in which the *private benefit* faced in production by a firm or consumption by a consumer is lower than the actual *social benefit* (alternatively, in some cases it may be more intuitive to think about it as the *private cost* is greater than the *social cost*. Similarly, the opposite holds true for negative externalities).

# ```{figure} fig1-positive-externality.png
# ---
# width: 500px
# name: positive-externality
# ---
# A demand-side positive externality in which the marginal social benefit is greater than the marginal private benefit
# ```

# ![title](fig1-positive-externality.png)

# In this case, a **market failure** occurs, in which the true quantity demanded by society does not match what would occur in a free market without government intervention. This is where taxes and interventions come in: they can correct for externalities and thus resolve consequent market failures.

# ## Effects of Taxation
# 
# The primary method that governments use to intervene in markets to address negative externalities is taxation. 

# ```{figure} fig2-supply-tax.png
# ---
# width: 500px
# name: supply-tax
# ---
# A shift in supply due to a tax levied on producers
# ```

# ![title](fig2-supply-tax.png)

# If a tax is levied on producers, this decreases the quantity of goods they can supply at each price as the tax is effectively acting as an additional cost of production. This shifts the supply curve leftward. Compared to negative externality graph above, we can see that the tax essentially 'corrects' the supply curve based on the marginal private cost to instead mirror the supply curve based on the marginal social cost.
# 
# 

# ```{figure} fig3-demand-tax.png
# ---
# width: 500px
# name: demand-tax
# ---
# A shift in demand due to a tax levied on consumers
# ```

# ![title](fig3-demand-tax.png)

# If the tax is levied on consumers, this increases the price per unit they must pay, thereby reducing quantity demanded at every price. This shifts the demand curve leftward.

# ## Effects of Subsidies
# 
# To account for positive externalities, a popular form of government intervention is a subsidy. They intend to lower production or consumption costs, and thus increase the quantity supplied of goods and services at equilibrium.

# ```{figure} fig5-subsidy.png
# ---
# width: 500px
# name: subsidy
# ---
# A shift in supply due to a new subsidy
# ```

# ![title](fig5-subsidy.png)

# We represent this visually as a rightward shift in the supply curve. As costs are lower, producers are now willing to supply more goods and services at every price. The demand curve remains unchanged as a subsidy goes directly to producers. The resulting equilibrium has a lower price $P^*$ and higher quantity $Q^*$. It is assumed that the lower production costs would be passed onto consumers through lower market prices. $P^*$ is what consumers pay, but producers receive $P_P = P^* + \text{subsidy}$. This is depicted visually by the price along the new supply curve at quantity $Q^*$.
# 
# Consumer surplus increases as more individuals are able to purchase the good than before. Similarly, producer surplus has increased as the subsidy takes care of part (if not all) of their costs. Overall market surplus has increased.
# 
# The welfare gain is depicted in a similar way to that of a tax: a triangle with a vertex at the original market equilibrium and a base along $Q^*$. The cost of the subsidy to the government is $\text{per-unit subsidy} \cdot Q^*$.

# ## Examining the Effects of Taxes
# 
# For the rest of this section, we will examine the effects of taxes in more detail. 

# ```{figure} fig4-dwl-tax-wedge.png
# ---
# width: 500px
# name: dwl-tax-wedge
# ---
# Deadweight loss due to a tax levied on consumers
# ```

# ![title](fig4-dwl-tax-wedge.png)

# The resulting equilibrium - both price and quantity - is the same in both cases. However, the prices paid by producers and consumers are different. Let us denote the equilibrium quantity to be $Q^*$. The price that producers pay $P_p$ occurs where $Q^*$ intersects with the supply curve. At the same time, the price that consumers pay $P_c$ occurs where $Q^*$ intersects  the demand curve.
# 
# You will notice that the vertical distance between $P_p$ and $P_c$ will be the value of the tax. That is to say, $P_c = P_p + \text{tax}$. We call the vertical distance between $P_p$ and $P_c$ at quantity $Q^*$ the tax wedge.

# ### Incidence
#     
# Determining who bears the greater burden, or economic incidence, of the tax depends on the relative producer and consumer price elasticities. A good that consumers are relatively more inelastic towards (such that producers are more elastic) would mean that the burden of paying the tax will fall on consumers moreso than producers. Intuitively, this is because consumers are less sensitive to price changes and thus are 'more willing' to pay more to adjust to the tax. The opposite is true if the consumers are relatively more elastic (i.e. the producers are relatively more inelastic). See the figure below for more details.
# 
# One can calculate the burden share, or the proportion of the tax paid by consumers or producers:
# 
# Consumer's burden share: 
# 
# $$\dfrac{\text{Increase in unit price after the tax paid by consumers} + \text{Increase in price paid per unit by consumers to producers}}{\text{Tax per unit}}$$
# 
# Producer's burden share: 
# 
# $$\dfrac{\text{Increase in unit price after the tax paid by producers} - \text{Increase in price paid per unit by consumers to producers}}{\text{Tax per unit}}$$
# 
# Graphically, the total tax burden is the rectangle formed by the tax wedge and the horizontal distance between 0 and $Q^*$: $Q^* \cdot \text{tax}$ This is also how you calculate the revenue from the tax earned by the government.

# ```{figure} fig6-elasticity-of-taxes.png
# ---
# width: 900px
# name: elasticity-of-taxes
# ---
# Differences in economic incidences of a tax due to elastic and inelastic demand.
# ```

# ![title](fig6-elasticity-of-taxes.png)

# ### Deadweight Loss
# 
# Naturally, the introduction of the tax disrupts the economy and pushes it away from equilibrium. For consumers, the higher price they must pay essentially "prices" out some individuals - they are now unwilling to pay more for the good. This leads them to leave the market that they previously participated in. At the same time, for producers, the introduction of the tax increases production costs and cuts into their revenues. Some of the businesses that were willing to produce at moderately high costs now find themselves unable to make a profit with the introduction of the tax. They too leave the market. There are market actors who are no longer able to purchase or sell the good.
# 
# We call this loss of transactions: deadweight welfare loss. It is represented by the triangle with a vertex at the original market equilibrium and a base at the tax wedge. The area of the deadweight loss triangle, also known as Harberger's triangle, is the size of the welfare loss - the total value of transactions lost as a result of the tax.
# 
# Another way to think about deadweight loss is the change (decrease) in total surplus. Consumer and producer surplus decrease significantly, but this is slightly offset by the revenue earned by the government from the tax. 
# 
# We can calculate the size of Harberger's triangle using the following formula: $\dfrac{1}{2} \cdot \dfrac{\epsilon_s \cdot \epsilon_d}{\epsilon_s - \epsilon_d} \cdot \dfrac{Q^*}{P_p} (\text{tax})^2$ where $\epsilon_s$ is the price elasticity of supply and  $\epsilon_d$ is the price elasticity of demand.

# ### Salience
# 
# We noted in our discussion about taxes that the equilibrium quantity and price is the same regardless of whether the tax is levied on producers or consumers. This is the traditional theory's assumption: that individuals, whether they be producers or consumers, are fully aware of the taxes they pay. They decide how much to produce or consume with this in mind.
# 
# We call the visibility at which taxes are displayed their salience. As an example, the final price of a food item in a restaurant is not inclusive of sales tax. Traditional economic theory would say that this difference between advertized or poster price and the actual price paid by a consumer has no bearing on the quantity they demand. That is to say taxes are fully salient. However, recent research has suggested that this is not the case. 
# 
# A number of recent studies, including by Chetty, Looney and Kroft in 2009, found that posting prices that included sales tax actually reduces demand for those goods. Individuals are not fully informed or rational, implying that tax salience does matter.

# ## Calculating Taxes Algebraically

# ### Expressing Quantity as a Function of Price
# 
# So far, we have expressed our demand and supply curves using prices as a function of quantity, e.g. $D(Q) = 100 - Q$. This format aligns with the axes of our plots, since quantity is on the x-axis and price is on the y-axis. However, it perhaps makes more sense to switch this around, expressing quantity demanded or supplied as a function of price. Intuitively, the price of a good or service causes the quantity supplied or demanded to alter; at high prices, producers would be willing to supply a great deal of units while few consumers would enter the market, while the opposite is true at low prices.
# 
# To switch in between the different formats, we simply have to solve for the independent variable and express it in terms of our dependent variable. For 
# example, if demand is expressed as $D(Q) = 100 - Q$, then:
# 
# $$
# \begin{align*}
# P &= 100 - Q \\
# P - 100 &= -Q \\
# Q &= 100 - P = D(P)
# \end{align*}
# $$
# 

# ### Solving for the new quantity and price equilibria
# 
# In previous weeks where there was no tax in the market, we could equate demand and supply to solve for the market price/quantity:
# 
# $$D(P) = S(P)$$
# 
# In reality, the demand function is based on the price consumers pay (which we'll denote $P_c$), and the supply function is based on the price producers receive (which we'll denote $P_p$). Hence, the actual demand and supply functions are $D(P_c)$ and $S(P_p)$, so we should be equating:
# 
# $$D(P_c) = S(P_p)$$
# 
# In the no-tax scenario, the price received by producers is the same as the price paid by consumers. Hence, we are able to get away by expressing them both as $P$ above, where $P=P_p=P_c$. 
# 
# However, in the case of tax, $P_p$ is no longer equal to $P_c$. Specifically, $P_p+\text{tax}=P_c$. As a result, to solve for equilibrium with taxes, we can use substitution to express $P_c$ as $P_p+\text{tax}$, or $P_p$ as $P_c−\text{tax}$. Hence we actually aim to equate:
# 
# $$D(P_c)=S(P_p)\implies D(P_p+\text{tax})=S(P_p)\quad \text{or} \quad D(P_c)=S(P_c−\text{tax})$$
# 
# Because there are now 3 unknowns ($P_c,P_p,Q$) and 3 equations ($P_p+\text{tax}=P_c$, supply equation, and demand equation), we conduct this substitution to reduce it to 2 equations and 2 unknowns. Essentially, you'll find that the tax simply was just a shift in the intercepts, which matches our graphical intuition from the diagrams above!
# 
# Once we are able to solve for $P_p$ or $P_c$, we can add/subtract the tax to get the other. We can also plug $P_c$ into $D(P_c)$ to get the equilibrium quantity, which should be the same as plugging in $P_p$ into $S(P_p)$. 
# 
# Lastly, to calculate the consumer burden, we seek to measure how much more the consumers are now paying due to the tax. Hence, this value is $P_c−P$, where $P$ is the original price when there is no tax. Similarly, to calculate the producer burden, we seek to measure how much less the producers are now receiving due to the tax; this value is $P−P_p$. 

# ## An Example

# **Part 1:** Suppose the demand for rutabagas is $D(P_c) = 2000 − 100P_c$. The supply of rutabagas is: $S(P_p) = −100 + 200P_p$. What is the equilibrium price without the tax?

# ```{admonition} Solution
# :class: dropdown
# 
# Since there is no tax, $P_p = P_c = P$. Thus:
# 
# $$
# \begin{align*}
# 2000 - 100P &= -100 + 200 P \\
# 2100 - 100P &= 200 P \\
# 2100 &= 300 P \\
# P &= 7 \\
# \end{align*}
# $$
# 
# ```

# **Part 2:**
# What is the equilibrium price with a per unit \$2 sales tax?

# ```{admonition} Solution
# :class: dropdown
# 
# With a \$2 sales tax, we know that $P_c = P_p + 2$. Thus:
# 
# $$
# \begin{align*}
# 2000 - 100P_c &= -100 + 200 P_p\\
# 2000 - 100(P_p+2) &= -100 + 200P_p \\
# 2000 - 100P_p - 200 &= -100 + 200P_p \\
# 1900 - 100P_p &= + 200P_p \\
# 1900 &= 300P_p \\
# P_p &= 6.33 \\ 
# P_c &= 6.33 + 2 = 8.33
# \end{align*}
# $$
# ```

# **Part 3:**
# What are the tax burdens on the consumer and producer?

# ```{admonition} Solution
# :class: dropdown
# 
# Consumer burden: $\text{New price paid} - \text{Old price paid} = 8.33 - 7 = 1.33$
# 
# Producer burden: $\text{Old price received} - \text{New price received} = 7 - 6.33 = 0.67$
# 
# This means that the consumer bears $\frac{2}{3}$ of the total burden of the tax.
# ```

# **Part 4:**
# What is change in quantity transacted due to the tax?

# ```{admonition} Solution
# :class: dropdown
# 
# Originally, $Q = 2000 - 100P_c = 2000 - 100\times 7 = 1300$. 
# 
# Now, $Q = 2000 - 100P_c = 2000 - 100\times 8.33 = 1167$.
# The difference in quantity transacted is thus $1300 - 1167 = 133$ units.
# 
# Note that we can also plug in $P_p$ into the supply equation and get the same results!
# 
# ```

#  
