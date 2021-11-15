#!/usr/bin/env python
# coding: utf-8

# In[2]:


from textbook_utils import *
get_ipython().run_line_magic('matplotlib', 'inline')


# # Production and Cobb-Douglas Functions

# ## Production in the Economy
# 
# At the core of macroeconomics is the study of how a nation's various resources are used as inputs in the production of goods and services. The aggregate value of what a nation produces is known as its Gross Domestic Product, which is calculated in many different ways. The focus of this lecture is on production and the functions that aim to model how much output a country can produce, when given a certain set of inputs. 
# 
# These set of inputs are known as factors of production:
# - $K$: Capital - a monetary value of the stock or value of productive assets.
# - $L$: Labor - the number of worker hours.
# - $A$: Total Factor Productivity - a measure of the effectiveness with which the two factors of production are used.
# 
# This model of production in an economy provides a simple yet effective way of modeling output. It would be way too complicated to account for every possible input to production, especially as we are operating at the country level. However, the key simplication is that we can classify all of these different inputs as either capital or labor: anything physical or tangible is capital and any work done by humans is labor. Taking the monetary value of either of these, while a rough approximation, still yields great insight into the different ways countries produce goods and services. Even if two countries have very similar GDPs, one maybe more capital intensive than the other. Having this knowledge would greatly inform policy and would help governments direct funding towards areas of concern.
# 
# We will see this in action during Project 2 where we will examine real life data from different countries and compare/contrast their usage of labor, capital and total factor productivity.
# 
# This simplication has allowed economists to derive the following key notion:
# A nation's output is a function of the amount of the factors of production that are utilized in its economy; that is to say output is a function of labor and capital.
# 
# Thus, the economy's production function is: 
# 
# $$Y = A \cdot f(K, L)$$
# 
# $f(K, L)$ refers to any specific mathematical model of output. One such example is the Cobb-Douglas production function that we will be examining in the next section.

# ### Total Factor Productivity
# 
# In modern economies, one way to think about total factor producivity (TFP) is technology or research and development. A country with a high TFP (or technology) can produce far more goods and services than another with a lower TFP but the exact same amount of capital and labor. Think about it: a country with 5 factories utilizing robotic arms to assemble cars will be able to produce more than another nation that also has 5 factories but utilizes workers working in 8-hour shifts. The former country would have a higher TFP than the latter. Thus, it can be said that technology increases the efficiency with which the factors of production are used.
# 
# There are three key differences between TFP and the other two factors of production:
# 1. TFP "scales" production by some factor A. The other two are raised to an exponent that is less than 1, reducing its value relative to the input. Thus, TFP is very powerful as it creates a proportional increase in output.
# 2. Technology is "non-rivalrous", meaning that more than one person can use it at any given time. For example, robotics technology is not limited to one person, but a specific robotic arm can only be used by a single person at a time.
# 3. Technology is "non-excludable", meaning that one person cannot block another from using that factor. Even with the patent system, after expiry, technologies that were once protected now becomes free to use or adapt.
# 
# Note that TFP has no intrinsic value by itself, but becomes informative when it is compared across nations. For example, a TFP of 1.4 means nothing. However, if one country has a TFP of 1.8 while the other is 1.4, then we can say that the first country is more effective at utilizing its resources to produce output.

# ## The Cobb-Douglas Production Function
# 
# The Cobb-Douglas Production Function is
# 
# $$\begin{aligned}
# f(K, L) &= K^\alpha L^\beta \\
#  Y &= A \cdot f(K, L) \\
#  &= A K^\alpha L^\beta
# \end{aligned}$$
# 
# where $\alpha$ and $\beta$ are exponents.
# 
# A common simplification is that $\beta = 1 - \alpha$. We will later explore the implications of this statement. For now, let us rewrite the above function:
# 
# $$
# Y = A K^\alpha L^{1 - \alpha}
# $$
# 
# Note that this is a function of two variables, $K$ and $L$. If we were to plot this function utilizing both variables, we would need a 3D plot with $K$, $L$ and $Y$ each having their own axis. For now, let us gain greater insight of what this function will look like by holding one variable constant and plot the other versus output.

# ### Capital
# 
# For the first case, let us visualize the Cobb-Douglas Production Function with output as a function of capital, holding the amount of labor constant at $\bar L$.

# In[7]:


plt.figure(figsize=[11,7])
cobb_douglas_plotter_K(1, 0.5, 0.4, cobb_douglas(1, np.arange(0, 1.01, .01), 0.5, 0.4))


# Notice some of the properties of the function above:
# 
# 1. It is increasing. This is called increasing returns to capital wherein any increase in capital will lead to an increase in output, assuming that labor is held constant.
# 2. It is concave (increasing at a decreasing rate). This is called diminishing marginal returns to capital wherein any additional unit of capital will lead to smaller and smaller increases in capital. For a better idea of this, let us take the partial derivative of the Cobb-Douglas function with respect to capital.
# 
# $$\begin{aligned}
# Y &= A K^\alpha L^{1 - \alpha} \\
# \dfrac{\partial Y}{\partial K} &= \alpha A \left ( \dfrac{L}{K} \right )^{1 - \alpha} 
# \end{aligned}$$
# 
# $\dfrac{\partial Y}{\partial K}$ is called the **marginal product of capital (MPK)**. Let us plot this function, once again holding labor constant at $\bar L$.

# In[4]:


A = 1
alpha = 0.4
L_bar = 0.5

K_s = np.linspace(0.001, 1, 100)
V_2 = MPK(A, K_s, L_bar, alpha)

plt.figure(figsize=[11,7])
plt.plot(K_s, V_2)
plt.title(fr"MPK with $\bar L$ = {L_bar}, $A$ = {A} and $\alpha$ = {alpha}", size=16)
plt.xlabel("Capital Stock", size=16)
plt.ylabel("MPK or Rental Rate of Capital", size=16);


# Note that $\text{MPK} \cdot P = R$ is the rental rate of capital less the cost of purchasing or renting an additional unit of capital.
# 
# The MPK is monotonically decreasing, converging towards an asymptote at $\text{MPK} = 0$. This means that the rate of increase of output due to an increase in capital will become 0, meaning that the amount of output added per unit of additional capital will become constant. What would be the intuition behind this?
# 
# Say a company making pizzas has 1 oven and 10 employees. There is a hard limit on how many pizzas can be baked in a given period of time. However, if the company purchases a second oven, suddenly the employees can bake more pizzas at the same time, thereby increasing the number that can be baked in the same amount of time. In this case, the MPK would be very high as output has greatly increased just by addding slightly to the company's capital stock. 
# 
# Let us move to the case when the company has 100 ovens and 10 employees. Adding another oven would do little to increase output as the 10 employees can only do so much - the extra capacity would not be helpful. In this case, the MPK would be very low as output has not increased by much (if at all) even when the company's capital stock increased.

# ### Labor
# 
# We will now move to using the Cobb-Douglas function for output as a function of labor, holding the amount of capital constant at $\bar K$.

# In[8]:


plt.figure(figsize=[11,7])
cobb_douglas_plotter_L(1, 0.5, 0.4)


# The properties of the Labor function are similar to that of the capital function. Let us take the partial derivative of the Cobb-Douglas function with respect to labor.
# 
# $$\begin{aligned}
# Y &= A K^\alpha L^{1 - \alpha} \\
# \dfrac{\partial Y}{\partial L} &= A (1 - \alpha) \left ( \dfrac{K}{L} \right )^{\alpha}
# \end{aligned}$$
# 
# $\dfrac{\partial Y}{\partial L}$ is called the **marginal product of labor (MPL)**. Let us plot this function, once again holding capital constant at $\bar K$.

# In[9]:


A = 1
K_bar = 0.5
L_s = np.linspace(0.001, 1, 100)
alpha = 0.4
V_4 = MPL(A, K_bar, L_s, alpha)

plt.figure(figsize=[11,7])
plt.plot(L_s, V_4)
plt.title(fr"MPL with $\bar K$ = {K_bar}, $A$ = {A} and $\alpha$ = {alpha}", size=16)
plt.xlabel("Labor", size=16)
plt.ylabel("MPL or Wage", size=16);


# Note that $\text{MPL} \cdot P = W$, the real wage rate less the cost of hiring an additional unit of labor.
# 
# Similar to the MPK, the MPL is monotonically decreasing, converging towards an asymptote at $\text{MPL} = 0$. This means that the rate of increase of output due to an increase in labor will become 0.
# 
# Say the same company making pizzas has 5 ovens and 5 employees. One oven per employee seems like overkill but provides significant extra capacity in terms of capital that would give great flexibility for the company when producing pizzas. However, if the company hires 1 more worker, each oven can be utilized more effectively, as another employee can go to prepping pizzas before baking. This greatly increasies the number of pizzas baked in a given unit of time. The MPL would be very high as output increases significantly with the addition of one more worker. On the above graph, we would be on the steep part of the function.
# 
# If the company has 5 ovens but 20 employees, hiring an additional worker would do little to increase output. The kitchen would probably be too crowded and there are only so many servers needed. The MPL would be very low as output has not increased by much even when the company's amount of labor has increased. We would be near the flat part of the graph, as the MPL approaches 0.

# ### Implication for Cross-Country Comparisons
# 
# Work by Professors C.W. Cobb and P.H. Douglas found that production or output was a weighted average of the log of capital and labor. The equation for Cobb-Douglas production functions were the result of their research, especially when a log transformation was applied to the equation:
# 
# $$\begin{aligned}
# Y &= A K^\alpha L^{1 - \alpha} \\
# \ln Y &= \ln A + \alpha \ln K + (1 - \alpha) \ln L
# \end{aligned}$$
# 
# Note that this is exactly the weighted average that Cobb & Douglas found in their empirical findings: capital and labor are weighted by $\alpha$ and $1 - \alpha$ respectively. However, this is still showing production as a function of two variables, $K$ and $L$. Rearranging the equation yields something interesting:
# 
# $$\begin{aligned}
# \ln Y &= \ln A + \alpha \ln K + \ln L - \alpha \ln L \\
# \ln Y- \ln L &= \ln A + \alpha \left ( \ln K - \ln L \right ) \\
# \ln \frac{Y}{L} &= \ln A + \alpha \ln \frac{K}{L}
# \end{aligned}$$
# 
# The Cobb-Douglas function is now an equation in 1 variable: $\ln \frac{K}{L}$. This provides a pathway for comparing values of $A$ and $\alpha$ across countries, and by extension how capital and labor are deployed in different ways between nations. We will explore this idea further in the next section.

#  
