#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display, HTML
import warnings
warnings.filterwarnings('ignore')


# # Budget Constraints and Utility Maximization
# 
# In this section, we will assume that $\alpha = 0.5$ (i.e. the utility function is: $u(x_1, x_2) = x_1^{0.5}x_2^{0.5}$).
# 

# 
# Now we introduce the concept of money into our model. Consumers face a budget constraint when choosing to maximize their utility. Given an income $M$ and prices $p_1$ for good $x_1$ and $p_2$ for good $x_2$, the consumer can at most spend up to $M$ for both goods:
# 
# $$M \geq p_1x_1 + p_2x_2$$
# 
# Since goods will always bring non-negative marginal utility, consumers will try to consume as many goods as they can. Hence, we can rewrite the budget constraint as an equality instead (since if they have more income leftover, they will use it to buy more goods).
# 
# $$M = p_1x_1 + p_2x_2$$
# 
# This means that any bundle of goods $(x_1,x_2)$ that consumers choose to consume will adhere to the equality above. What does this mean on our graph? Let's examine the indifference curve plots, assuming that $M = 32$, and $p_1 =2$ and $p_2 = 4$. 
# 

# In[2]:


M = 32
p_1 = 2
p_2 = 4

# Plot default indifference curves
utilities = np.arange(1, 9)
x1_indiff_val = np.linspace(0,50,1000)
x2_indiff_vals = []
for u in utilities:
    x2_indiff_vals.append(((u/(x1_indiff_val ** (1/2))) ** (2)))
traces = []
colors = ['blue', 'red','green','purple'] + ['blue', 'red','green','purple']
for u,c,x2 in zip(utilities,colors,x2_indiff_vals):
    traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2,
    name = 'utility = ' + str(u),
    line = dict(color = c,width = 1)))
    
# for i in range(len(traces) - 4):
#     del traces[-1] # This is a hacky method to not continually append to TRACES upon an update from the slider.
x2_bc_val = (M - (p_1*x1_indiff_val))/p_2
traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2_bc_val,
    name = 'Budget Constraint',
    line = dict(color = 'black',width = 1,dash="dot")))
data = traces
layout = dict(title = 'Budget Constraint and Indifference Curves for the Cobb-Douglas Utility Function (alpha = 0.5)',
              xaxis = dict(title = 'X1', range = [0,18]),
              yaxis = dict(title = 'X2', range = [0,10]),)
fig = dict(data=data, layout=layout)

plot(fig, filename="fig3.html", auto_open=False)
display(HTML("fig3.html"))


# The budget constraint is like a possibilities curve: moving up or down the constraint means gaining more of one good while sacrificing the other.
# 
# Let's take a look at what this budget constraint means. Because of the budget constraint, any bundle of goods $(x_1,x_2)$ that consumers ultimately decide to consume will lie on the budget constraint line. Adhering to this constraint where $M=32, p_1 = 2, p_2 = 4$, we can see that consumers will be able to achieve 2 units of utility, and can also achieve 4 units of utility. But what is the maximum amount of utility that consumers can achieve? 
# 
# Notice an interesting property about indifference curves: **the utility level of the indifference curves gets larger as we move up and to the right.** Hence, the maximizing amount of utility in this budget constraint is the rightmost indifference curve that still touches the budget constraint line. In fact, it'll only 'touch' (and not intersect) the budget constraint and be tangential to it. 

# In[3]:


M = 32
p_1 = 2
p_2 = 4

# Plot default indifference curves
utilities = np.arange(1, 9)
x1_indiff_val = np.linspace(0,50,1000)
x2_indiff_vals = []
for u in utilities:
    x2_indiff_vals.append(((u/(x1_indiff_val ** (1/2))) ** (2)))
traces = []
colors = ['blue', 'red','green','purple'] + ['blue', 'red','green','purple']
for u,c,x2 in zip(utilities,colors,x2_indiff_vals):
    traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2,
    name = 'utility = ' + str(u),
    line = dict(color = c,width = 1)))

# PLOT BC
x2_bc_val = (M - (p_1*x1_indiff_val))/p_2
traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2_bc_val,
    name = 'Budget Constraint',
    line = dict(color = 'black',width = 1,dash="dot")))


# PLOT MAX UTIL INDIFF CURVE
max_utility = ((1/2*M/p_1) ** (1/2)) * ((1/2*M/p_2) ** (1/2))
x2_max_util = (max_utility/(x1_indiff_val ** (1/2))) ** 2
x2_max_util = (max_utility/(x1_indiff_val ** (1/2))) ** 2
traces.append(go.Scatter(
    x = x1_indiff_val,
    y = x2_max_util,
    name = 'Maximized Utility = ' + str(round(max_utility, 2)),
    line = dict(color = 'black',width = 2)))
data = traces

layout = dict(title = 'Budget Constraint and Indifference Curves for the Cobb-Douglas Utility Function (alpha = 0.5)',
              xaxis = dict(title = 'X1', range = [0,20]),
              yaxis = dict(title = 'X2', range = [0,15]),)
fig = dict(data=data, layout=layout)

plot(fig, filename="fig4.html", auto_open=False)
display(HTML("fig4.html"))


# Notice that as the price of one good increases, the indifference curve that represents the maximum attainable utility shifts towards the left (i.e. the max utility decreases). Intuitively, this makes sense. As the price of one good increases, consumers have to make adjustments to their consumption bundles and buy less of one, or both, goods. Hence, their maximum utility will decrease.
# 
# Let's visualize the budget constraint in 3D where $M=30, p_1=3, p_2=3$. Here, any point along the curve in which the 2 planes intersect represents an amount of utility in which the budget constraint holds true (i.e. where we've spent all our income). The utility maximizing quantity is a point on this intersecting curve at which the utility level is the highest.

# In[4]:


def cobb_douglas(x1, x2):
    return (x1 ** (1/2)) * (x2 ** (1/2))
x1 = np.linspace(0,10,10)
x2 = np.linspace(0,10,10)
X1,X2 = np.meshgrid(x1,x2)
z = cobb_douglas(X1,X2)

def budget_constraint(x1, x2):
    return 10000*(3*x1 + 3*x2 - 30) # We multiply this by 10000 to get a very steep plane, which should be similar to the actual BC, a vertical plane.

z2 = budget_constraint(X1, X2)

data = [go.Surface(
    z=z, contours=go.surface.Contours(z=go.surface.contours.Z(show=True,usecolormap=True,highlightcolor="#42f462",
                                                              project=dict(z=True))), name="Cobb-Douglas Utility Function"),
       go.Surface(
   z=z2, contours=go.surface.Contours(z=go.surface.contours.Z(show=True,usecolormap=False,
                              highlightcolor="#42f462",project=dict(z=True))),showscale=False, colorscale="balance", name="Budget Constraint")]
layout = go.Layout(
    title='Cobb-Douglas Utility Function with Budget Constraint', autosize=False,width=500, height=500, margin=dict(l=65,r=50,b=65,t=90),
    scene = dict(xaxis = dict(title='X1', range = [0,10]), yaxis = dict(title='X2'),
    zaxis = dict(title = 'Utility', nticks=4, range = [0,10],)))
fig = go.Figure(data=data, layout=layout)

plot(fig, filename="fig5.html", auto_open=False)
display(HTML("fig5.html"))


#  
