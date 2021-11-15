#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sympy
import numpy as np
import warnings
from datascience import *
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import plotly.graph_objects as go
from plotly.offline import plot
from IPython.display import display, HTML
warnings.filterwarnings('ignore')
plt.style.use("seaborn-muted")
solve = lambda x,y: sympy.solve(x-y)[0] if len(sympy.solve(x-y)) == 1 else "Not Single Solution"
get_ipython().run_line_magic('matplotlib', 'inline')


# # Surplus

# ## Consumer Surplus
# Although all consumers face the same market price, consumers are different in how much they individually value a good. We say that consumers have a maximum price that they are willing to pay for a good, and any price marginally higher than this price will dissuade the consumer from participating in the market. This max willingness to pay (WTP) price varies among entities based on their desire for the good, which in turn can be based on how much of the good they already have.
# 
# Consider the market for electricity. Among consumers we have entities such as households, commercial buildings, factories, and so on. A factory would likely have a very high WTP for electricity because the opportunity costs for factories to not operate are very high. Capital is expensive, employees still have to be paid, and it is inconvenient to have to stop and start up machinery frequently. Thus, for a factory it is preferable to always have a reliable supply of electricity to continue operations and this need is reflected in the WTP. Contrast this with households, who certainly value having electricity, but should electricity become prohibitively expensive, probably would decide to cut back on usage as the drawbacks of not having electricity aren't as severe compared to the factory above.
# 
# ## Producer Surplus
# Producers experience a similar characteristic. A producer has a minimum price at which it is willing to produce a good based on its costs. Any market price less than this price would dissuade a producer from supplying its good. Again, in the electricity example, we have several power plants that produce electricity, but each inherently does so at different costs. Imagine and contrast the operating costs of a solar farm with a coal plant, or a newer, more efficient natural gas plant versus an older one.
# 
# Putting all of these concepts together we arrive at the idea of economic welfare. Suppose electricity costs 10 cents per kWh. On the demand side, imagine a factory who's WTP is 30 cents/kWh. This factory enjoys a consumer surplus of 20 cents/kWh, in other words, it's paying 20 cents less per kWh than what it would be willing to pay. A household might have a WTP of 15 cents/kWh. Here the household's surplus is only 5 cents/kWh. We can also imagine a consumer whose WTP is less than the market price and thus doesn't participate in the market. Imagine for some reason that cryptocurrency prices have dropped to the point that they aren't worth the electricity it takes to mine them. In this case, we might have an idle or non-existent crypto-farm (a place with a lot of computing power) due to electricity being too expensive. On the producer side, maybe we have a solar plant which is operating at the market price, but a natural gas plant that is idling because the price of supplying electricity isn't sufficient to make up for operating costs.
# 
# Combining the surpluses of all individual consumers and producers yields the market consumer surplus and producer surplus. As the market price fluctuates, certain comsumers and producers enter and exit the market, and the total surplus varies. Note from the above examples that a consumer is not always an individual, it can be a firm buying from another firm. We now explore further.

# ## Example
# 
# We create a consumer class with a WTP characteristic, and a list of consumers with WTP from 10 to 1. The binary function `demand` ```1``` if the consumer participates in the market at a given price and ```0``` if not.

# In[2]:


class Consumer:
    def __init__(self, WTP):
        self.WTP = WTP
        
    def demand(self, price):
        if price <= self.WTP:
            return 1
        else:
            return 0
        
    def surplus(self, price):
        if price <= self.WTP:
            return self.WTP - price
        else:
            return 0
        
consumers = [Consumer(x) for x in range(10,0,-1)]

[x.demand(6) for x in consumers]


# For a market price of 6, we have 5 consumers who participate and 5 who don't. Now let's make a table of the lists of participants for each market price between 1 and 10.

# In[3]:


per_consumer = np.array([[x.demand(i) for x in consumers] for i in range(10, 0, -1)]).T
Table().with_columns("Market Price", np.arange(10, 0, -1), 
                     "Consumer with WTP: 10", per_consumer[0],
                     "Consumer with WTP: 9", per_consumer[1],
                     "Consumer with WTP: 8", per_consumer[2],
                     "Consumer with WTP: 7", per_consumer[3],
                     "Consumer with WTP: 6", per_consumer[4],
                     "Consumer with WTP: 5", per_consumer[5],
                     "Consumer with WTP: 4", per_consumer[6],
                     "Consumer with WTP: 3", per_consumer[7],
                     "Consumer with WTP: 2", per_consumer[8],
                     "Consumer with WTP: 1", per_consumer[9])


# You can draw a downward-sloping diagonal line sepearating ```1```s from ```0```s - a vague resemblance of a downward-sloping demand curve. The left-most consumer, with a WTP of 10, always participates for the market prices we have listed. The right-most consumer only participates at a market price of 1. Now lets try and find the number of consumers who participate for each price point, starting at 10.

# In[4]:


market = Table().with_column("Market Price", np.arange(10, 0, -1))
market = market.with_column("Number of Participants", 
                   market.apply(lambda price : sum([x.demand(price) for x in consumers]), "Market Price"))
market


# Instead of printing a binary 1 or 0 indicating market participation, we've displayed each participant's actual surplus value. Similarly, let's find total surplus per price point.

# In[5]:


surplus = Table().with_column("Market Price", np.arange(10, 0, -1))
surplus = surplus.with_column("Total Surplus", 
                   surplus.apply(lambda price : sum([x.surplus(price) for x in consumers]), "Market Price"))
surplus


# Clearly there must be an opposite "force" at play here, otherwise all prices would converge to 0 as consumers maximize their surplus (more on maximization later). Naturally, we must also consider the producers who sell their product to the consumers. We essentially repeat the exercise above, but now instead of a consumer class with individual willingness to pay, we have a producer class with some minimal market price at which production can occur.

# In[6]:


class Producer:
    def __init__(self, WTA):
        self.WTA = WTA
        
    def supply(self, price):
        if price >= self.WTA:
            return 1
        else:
            return 0
        
    def surplus(self, price):
        if price >= self.WTA:
            return price - self.WTA
        else:
            return 0
        
producers = [Producer(x) for x in range(1,11)]


# In[7]:


per_producer = np.array([[x.surplus(i) for x in producers] for i in np.arange(10, 0, -1)]).T

Table().with_columns("Market Price", np.arange(10, 0, -1), 
                     "Producer with WTP: 10", per_producer[0],
                     "Producer with WTP: 9", per_producer[1],
                     "Producer with WTP: 8", per_producer[2],
                     "Producer with WTP: 7", per_producer[3],
                     "Producer with WTP: 6", per_producer[4],
                     "Producer with WTP: 5", per_producer[5],
                     "Producer with WTP: 4", per_producer[6],
                     "Producer with WTP: 3", per_producer[7],
                     "Producer with WTP: 2", per_producer[8],
                     "Producer with WTP: 1", per_producer[9])


# Looks familiar, but with an opposite slope! Here we've captured the idea of producer surplus. At a market price of 10, the leftmost producer is very happy with a surplus of 9, as in this case that producer is actually able to produce and sell at a price of 1 but is able to operate at a price of 10.
# 
# Before we continue, let's take a moment to think about the meaning and significance of our findings. Firms that can produce at lower market prices than their peers seem to be better off in the sense that they enjoy higher surplus. This minimum production price is based on the costs of operation the firm experiences, so naturally it seems that firms that can operate at lower costs do better. Certainly, if market prices decrease, more inefficent firms would be the first to shut down while these low operating cost firms continue to do business. This idea is very important in economics: Firms that can reduce their costs are rewarded with higher surplus. This is pretty much how society advances, at least in an economics context. Production methods continually to improve, and less efficient firms must either follow suit or shut down as prices decrease, to the benefit of consumers.
# 
# However, what would the equivalent be for the consumer side of things? We've discussed the idea of willingness to pay, and initially it might seem that in our perfectly-competitive market environment, only the consumers who most need a good or service will be the first to get it, as their WTP is the highest. We might think that resources are efficiently allocated in this way. Most of the time this is likely the case, but we've made an assumption while reaching this conclusion; an assumption that doesn't necessarily hold. We have assumed that a person with high willingness to pay also has at least an equally high *ability* to pay. In reality, this might not be the case. A hungry person might have high WTP for a serving of food, but if this person lacks the means to pay for this food, his willingness to pay won't do him much good. In this scenario, our earlier exercise reflects willingness to pay with a simultaneous ability to pay as well. While this week isn't about the ethics of certain types of markets and whether they achieve their goals, it's important to keep in mind that in these ideal exercises, an efficient economy with rational pricing should reflect consumers' willingness to pay, whereas in reality this might not actually be the case.

# ## Note on the Demand and Supply Curves
# 
# As pointed out above, the matrix we saw with rows of surpluses and columns of prices resembles the demand curve in the sense that we can see a diagonal line separating participants from non-participants. This is no coincidence. This idea is essentially what the demand and supply curves depict, except that due to there usually being many participants in a market, we simplify the concept to a continuous curve as opposed to a set of discrete values. This is helpful not only for visualization, but as we will soon see we can use these curves to find rates of change, which will prove to be useful as well.
# 
# 
# Earlier we had a matrix of each individual's surplus at each price point, and the overall surplus at each price point. Notice how as the price decreased, surplus increased. Let's see this exact same concept illustrated on a familiar demand curve. Take a few moments to adjust the slider controlling the market price to see how consumer surplus behaves.

# In[8]:


filename="fig1.html"

p = sympy.Symbol("p")
consumers = [Consumer(x) for x in range(0,11)]
demand_equation = 10 - p
prices = [x for x in range(0,11)]
demand_Q = [float(demand_equation.subs(p,x)) for x in prices]

fig = go.Figure()

active_idx = None
active_val = 5
vals = []
for i, val in enumerate(np.arange(1, 11)):
    vals.append(val)
    if val == active_val:
        active_idx = 3 * i
        step_idx = i
        
    demand_subbed = float(demand_equation.subs(p, val))
    fig.add_trace(go.Scatter(
        x = demand_Q,
        y = prices,
        mode = "lines",
        name = f"Demand",
        visible = False
    ))
    fig.add_trace(go.Scatter(
        x = [demand_subbed, 0, 0, demand_subbed],
        y = [val, val, 10, val],
        name = "Consumer Surplus",
        fill = "toself",
        visible = False,
        marker_color = "green"
    ))
    fig.add_trace(go.Scatter(
        x = [demand_subbed],
        y = [val],
        mode = "markers",
        name = "Equilibrium",
        visible = False,
        marker = dict(color = "red", size = 10)
    ))
    
fig.data[active_idx].visible = True
fig.data[active_idx + 1].visible = True
fig.data[active_idx + 2].visible = True

steps = []
for i in range(len(fig.data)):
    if i % 3 != 0:
        continue
    val = vals[i // 3]
    step = dict(
        method = "update",
        args = [
            {"visible": [False] * len(fig.data) + [True]},
            {"annotations": [
                dict(xref="paper", yref="paper", x=-0.003, y=-0.2, showarrow=False, xanchor="left",
                     text=f"Consumer Surplus: {sum([person.surplus(val) for person in producers])}")
            ]}
        ],
        label = f"{val}"
    )
    step["args"][0]["visible"][i] = True
    step["args"][0]["visible"][i + 1] = True
    step["args"][0]["visible"][i + 2] = True
    steps.append(step)
    
sliders = [
    dict(
        active = step_idx,
        currentvalue = {"prefix": "Market Price: $"},
        pad = {"t": 75},
        steps = steps
    )
]

fig.update_layout(
    xaxis = dict(title = "Demand Quantity"),
    yaxis = dict(title = "Price"),
    title = "Demand Curve with Consumer Surplus Shaded",
    sliders = sliders,
    width = 800, 
    height = 600,
    showlegend = False,
    annotations = [dict(xref="paper", yref="paper", x=-0.003, y=-0.2, showarrow=False, xanchor="left",
                     text=f"Consumer Surplus: {sum([person.surplus(active_val) for person in consumers])}")]
)

plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')
    
display(HTML(filename))


# Producer surplus with the supply curve works exactly the same way but mirrored to reflect the fact that producers gain surplus from higher prices instead of lower.

# In[9]:


filename="fig2.html"

p = sympy.Symbol("p")
producers = [Producer(x) for x in range(1,11)]
supply_equation = p
prices = [x for x in range(0,11)]
supply_Q = [float(supply_equation.subs(p, x)) for x in prices]

fig = go.Figure()

active_idx = None
active_val = 5
vals = []
for i, val in enumerate(np.arange(1, 11)):
    vals.append(val)
    if val == active_val:
        active_idx = 3 * i
        step_idx = i
        
    supply_subbed = float(supply_equation.subs(p, val))
    fig.add_trace(go.Scatter(
        x = supply_Q,
        y = prices,
        mode = "lines",
        name = f"Supply",
        visible = False
    ))
    fig.add_trace(go.Scatter(
        x = [supply_subbed, 0, 0, supply_subbed],
        y = [val, val, 0, val],
        name = "Producer Surplus",
        fill = "toself",
        visible = False,
        marker_color = "green"
    ))
    fig.add_trace(go.Scatter(
        x = [supply_subbed],
        y = [val],
        mode = "markers",
        name = "Equilibrium",
        visible = False,
        marker = dict(color = "red", size = 10)
    ))
    
fig.data[active_idx].visible = True
fig.data[active_idx + 1].visible = True
fig.data[active_idx + 2].visible = True

steps = []
for i in range(len(fig.data)):
    if i % 3 != 0:
        continue
    val = vals[i // 3]
    step = dict(
        method = "update",
        args = [
            {"visible": [False] * len(fig.data) + [True]},
            {"annotations": [
                dict(xref="paper", yref="paper", x=-0.003, y=-0.2, showarrow=False, xanchor="left",
                     text=f"Producer Surplus: {sum([person.surplus(val) for person in producers])}")
            ]}
        ],
        label = f"{val}"
    )
    step["args"][0]["visible"][i] = True
    step["args"][0]["visible"][i + 1] = True
    step["args"][0]["visible"][i + 2] = True
    steps.append(step)
    
sliders = [
    dict(
        active = step_idx,
        currentvalue = {"prefix": "Market Price: $"},
        pad = {"t": 75},
        steps = steps
    )
]

fig.update_layout(
    xaxis = dict(title = "Supply Quantity"),
    yaxis = dict(title = "Price"),
    title = "Supply Curve with Producer Surplus Shaded",
    sliders = sliders,
    width = 800, 
    height = 600,
    showlegend = False,
    annotations = [dict(xref="paper", yref="paper", x=-0.003, y=-0.2, showarrow=False, xanchor="left",
                     text=f"Producer Surplus: {sum([person.surplus(active_val) for person in producers])}")]
)

plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')
    
display(HTML(filename))


# Here we used a demand curve of $10-P$ and a supply curve of $P$.

#  
