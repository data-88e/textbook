#!/usr/bin/env python
# coding: utf-8

# In[6]:


from datascience import *

import sympy
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as patches
plt.style.use('seaborn-muted')
mpl.rcParams['figure.dpi'] = 200
get_ipython().run_line_magic('matplotlib', 'inline')

from IPython.display import display
import numpy as np
import pandas as pd
solve = lambda x,y: sympy.solve(x-y)[0] if len(sympy.solve(x-y))==1 else "Not Single Solution"

import warnings
warnings.filterwarnings('ignore')


# # Market Equilibria
# 
# We will now explore the relationship between price and quantity of oranges produced between 1924 and 1938. Since the data {cite}`01demand-fruits` is from the 1920s and 1930s, it is important to remember that the prices are much lower than what they would be today because of inflation, competition, innovations, and other factors. For example, in 1924, a ton of oranges would have costed \$6.63; that same amount in 2019 is \$100.78. 

# In[7]:


fruitprice = Table.read_table('fruitprice.csv')
fruitprice


# ## Finding the Equilibrium
# 
# An important concept in econmics is the market equilibrium. This is the point at which the demand and supply curves meet and represents the "optimal" level of production and price in that market.

# ```{admonition} Definition
# The **market equilibrium** is the price and quantity at which the demand and supply curves intersect. The price and resulting transaction quantity at the equilibrium is what we would predict to observe in the market.
# ```

# Let's walk through how to the market equilibrium using the market for oranges as an example.

# ### Data Preprocessing
# 
# Because we are only examining the relationship between prices and quantity for oranges, we can create a new table with the relevant columns: `Year`, `Orange Price`, and `Orange Unloads`. Here, `Orange Price` is measured in dollars, while `Orange Unloads` is measured in tons.

# In[52]:


oranges_raw = fruitprice.select("Year", "Orange Price", "Orange Unloads")
oranges_raw


# Next, we will rename our columns. In this case, let's rename `Orange Unloads` to `Quantity` and `Orange Price` to `Price` for brevity and understandability. 

# In[53]:


oranges = oranges_raw.relabel("Orange Unloads", "Quantity").relabel("Orange Price", "Price")
oranges


# ### Visualize the  Relationship
# 
# Let's first take a look to see what the relationship between price and quantity is. We would expect to see a downward-sloping relationship between price and quantity; if a product's price increases, consumers will purchase less, and if a product's price decreases, then consumers will purchase more. 
# 
# We will create a scatterplot between the points.

# In[50]:


oranges.scatter("Quantity", "Price", width=5, height=5)
plt.title("Demand Curve for Oranges", fontsize = 16);


# The visualization shows a negative relationship between quantity and price, which is in line with our expectations: as the price increases, fewer consumers will purchase oranges, so the quantity demanded will decrease. This corresponds to a leftward movement along the demand curve. Alternatively, as the price decreases, the quantity sold will increase because consumers want to maximize their purchasing power and buy more oranges; this is shown by a rightward movement along the curve.

# ### Fit a Polynomial
# 
# We will now quantify our demand curve using NumPy's [`np.polyfit` function](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html). Recall that `np.polyfit` returns an array of size 2, where the first element is the slope and the second is the $y$-intercept.
# 
# For this exercise, we will be expressing demand and supply as quantities in terms of price. 

# In[34]:


np.polyfit(oranges.column("Price"), oranges.column("Quantity"), 1)


# This shows that the demand curve is $D(P) = -3433 P+ 53626$. The slope is -3433 and $y$-intercept is 53626. That means that as price increases by 1 unit (in this case, \$1), quantity decreases by 3433 units (in this case, 3433 tons). 
# 

# ### Create the Demand Curve
# 
# We will now use SymPy to write out this demand curve. To do so, we start by creating a symbol `P` that we can use to create the equation.

# In[35]:


P = sympy.Symbol("P")
demand = -3432.846 * P + 53625.87
demand


# ### Create the Supply Curve
# 
# As you've learned, the supply curve is the relationship between the price of a good or service and the quantity of that good or service that the seller is willing to supply. It shows how much of a good suppliers are willing and able to supply at different prices. In this case, as the price of the oranges increases, the quantity of oranges that orange manufacturers are willing to supply increases. They capture the producer's side of market decisions and are upward-sloping.
# 
# Let's now assume that the supply curve is given by $S(P) = 4348P$. (Note that this supply curve is not based on data.)

# In[36]:


supply = 4348 * P
supply


#  This means that as the price of oranges increases by 1, the quantity supplied increases by 4348. At a price of 0, no oranges are supplied.

# ### Find the Price Equilibrium
# 
# With the supply and demand curves known, we can solve the for equilibrium. 
# The equilibrium is the point where the supply curve and demand curve intersect, and denotes the price and quantity of the good transacted in the market.
# 
# The equilbrium consists of 2 components: the quantity equilbrium and price equilbrium. 
# The price equilibrium is the price at which the supply curve and demand curve intersect: the price of the good that consumers desire to purchase at is equivalent to the price of the good that producers want to sell at. There is no shortage of surplus of the product at this price.
# 
# 
# Let's find the price equilibrium. To do this, we will use the provided `solve` function. This is a custom function that leverages some SymPy magic and will be provided to you in assignments.

# In[37]:


P_star = solve(demand, supply)
P_star


# This means that the price of oranges that consumers want to purchase at and producers want to provide is about \$6.89. 

# ### Find the Quantity Equilibrium
# 
# Similarly, the quantity equilibrium is the quantity of the good that consumers desire to purchase is equivalent to the quantity of the good that producers supply; there is no shortage or surplus of the good at this quantity. 
# 
# 

# In[38]:


demand.subs(P, P_star)
supply.subs(P, P_star)


# This means that the number of tons of oranges that consumers want to purchase and producers want to provide in this market is about 29,967 tons of oranges. 

# ### Visualize the Market Equilibrium 
# 
# Now that we have our demand and supply curves and price and quantity equilibria, we can visualize them on a graph to see what they look like. 
# 
# There are 2 pre-made functions we will use: `plot_equation` and `plot_intercept`.
# - `plot_equation`: It takes in the equation we made previously (either demand or supply) and visualizes the equations between the different prices we give it
# - `plot_intercept`: It takes in two different equations (demand and supply), finds the point at which the two intersect, and creates a scatter plot of the result

# In[49]:


def plot_equation(equation, price_start, price_end, label=None):
    plot_prices = [price_start, price_end]
    plot_quantities = [equation.subs(list(equation.free_symbols)[0], c) for c in plot_prices]
    plt.plot(plot_quantities, plot_prices, label=label)
    
def plot_intercept(eq1, eq2):
    ex = sympy.solve(eq1-eq2)[0]
    why = eq1.subs(list(eq1.free_symbols)[0], ex)
    plt.scatter([why], [ex], zorder=10, color="tab:orange")
    return (ex, why)


# We can leverage these functions and the equations we made earlier to create a graph that shows the market equilibrium.

# In[48]:


mpl.rcParams['figure.dpi'] = 150
plot_equation(demand, 2, 10, label = "Demand")
plot_equation(supply, 2, 10, label = "Supply")
plt.ylim(0,13)
plt.title("Orange Supply and Demand in 1920's and 1930's", fontsize = 15)
plt.xlabel("Quantity (Tons)", fontsize = 14)
plt.ylabel("Price ($)", fontsize = 14)
plot_intercept(supply, demand)
plt.legend(loc = "upper right", fontsize = 12)
plt.show()


# You can also practice on your own and download additional data sets [here](http://users.stat.ufl.edu/~winner/datasets.html), courtesy of the University of Flordia's Statistics Department. 

# ## Movements Away from Equilibrium
# 
# What happens to market equilibrium when either supply or demand shifts due to an exogenous shock?
# 
# Let's assume that consumers now prefer Green Tea as their hot beverage of choice moreso than before. We have an outward shift of the demand curve - quantity demanded is greater at every price. The market is no longer in equilibrium.

# ```{figure} fig1-demand.png
# ---
# width: 500px
# name: demand-shift
# ---
# A shift in the demand curve
# ```

# ![title](fig1-demand.png)

# At the same price level (the former equilibrium price), there is a shortage of Green Tea. The amount demanded by consumers exceeds that supplied by producers: $Q_D > Q_S$. This is a seller's market, as the excess quantity demanded gives producers leverage (or market power) over consumers. They are able to increase the price of Green Tea to clear the shortage. As prices increase, consumers who were willing and able to purchase tea at the previous equilibrium price would leave the market, reducing quantity demanded. $Q_S$ and $Q_D$ move up along their respective curves until the new equilibrium is achieved where $Q_S = Q_D$. 
# 
# This dual effect of increasing $Q_S$ and $Q_D$ is sometimes referred to as the "invisible hand". Sans government intervention, it clears out the shortage or surplus in the market, resulting in the eventual convergence to a new equilibrium level of quantity $Q^*$ and price $P^*$.

#  
