#!/usr/bin/env python
# coding: utf-8

# In[2]:


from textbook_utils import *


# # Analyzing Shifts in $A$ and $\alpha$

# ## Shifts in $A$ and their Effect on Output
# 
# First, let us plot a 3D surface of the Cobb-Douglas production function. Output, $Y$, will go on the vertical (or $z$) axis. Capital and labor will go on the $y$ and $x$ axes, resp. The plot below plots the Cobb-Douglas function with $A=2$, also showing $A=1$ for reference.

# In[3]:


change_A(2, filename="fig1.html")
display(HTML("fig1.html"))


# Supply or total factor productivity shocks could cause $A$ to change. These occur if there is a change in total output for a given level of capital and labor. Examples of these include financial crises, technology shocks, natural environment/distasters and energy prices.

# In[15]:


filename = "fig6.html"

L_s = np.arange(0, 10.11, 0.1)
K_s = np.arange(0, 10.11, 0.1)
alpha = 0.5
xx, yy = np.meshgrid(K_s, L_s)
# plot_cobb_douglas(curr_V, orig_cobb_douglas(), fr"A = {A}", r"A = 1", filename=filename)

layout = go.Layout(
    title = "Cobb-Douglas Production Function", autosize=False, width=500, height=500, margin = dict(l = 65, r = 50, b = 65, t = 90),
    scene = dict(xaxis = dict(title = 'K'), yaxis = dict(title = 'L'), zaxis = dict(title = 'Y'))
)

fig = go.Figure(layout = layout)

active = None
As = []
for i, A in enumerate(np.arange(0.5, 10.1, 0.5)):
    As.append(A)
    if A == 1:
        active = i
    V = cobb_douglas(A, xx, yy, alpha)
    fig.add_trace(go.Surface(
        z = V, contours = go.surface.Contours(
            z = go.surface.contours.Z(
                show = False, project = dict(z = True)
            )
        ), colorscale = "Electric", showscale = False, name=f"A = {A}", visible=False
    ))
    
fig.data[active].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update", args=[
            {"visible": [False] * len(fig.data) + [True]},
        ], label=f"A = {As[i]}"
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)
    
sliders = [dict(
    active=active,
    currentvalue={"prefix": ""},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(sliders=sliders, width=500, height=600)

orig_V = orig_cobb_douglas()
fig.add_trace(go.Surface(
    z = orig_V, contours = go.surface.Contours(
        z = go.surface.contours.Z(
            show = False, project = dict(z = True)
        )
    ), colorscale = "Viridis", showscale = False, name="A = 1"
))

plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')

display(HTML(filename))


# Favorable shocks rotate the production function upward through an increase in A. Thus, each unit of input from capital and labor now simulataneously produce more output. What does this mean for the rental rate of capital and the real wage? Recall the functions for both of them:
# 
# $$\begin{aligned}
# \text{MPL} &= A (1 - \alpha) \left ( \frac{K}{L} \right )^{\alpha} \\
# \text{MPK} &= \alpha A \left ( \frac{L}{K} \right )^{1 - \alpha} 
# \end{aligned}$$
# 
# Both MPK and MPL will increase by a factor of $A$. Thus, it would be more expensive to hire an additional unit of labor or rent an additional unit of capital. As they are both more productive than previously, they are both more valuable to a business and thus will cost more. Negative shocks do the opposite. They rotate the production function downward through a decrease in $A$. Each unit of input is now less productive, meaning that both the rental rate of capital and the real wage are lower.

# ## Shifts in $\alpha$ and their Effect on Output
# 
# We will now plot what happens to the Cobb-Douglas function as we vary $\alpha$, while holding all other variables constant. The plot below shows $\alpha = 0.8$ (the purple-yellow surface) with $\alpha=0.5$ for reference (the blue-yellow surface). Try and hypothesize what this will do to our production function.

# In[5]:


change_alpha(0.8, filename="fig2.html")
display(HTML("fig2.html"))


# 
# The next plot has $\alpha = 0.2$ (the purple-yellow surface) with $\alpha=0.5$ for reference (the blue-yellow surface). What is the difference between the plot above and the one below?

# In[6]:


change_alpha(0.3, filename="fig3.html")
display(HTML("fig3.html"))


# Below is an interactive plot with a slider to change $\alpha$. Try out different values and see how the shape of the production function changes.

# In[16]:


filename = "fig7.html"

L_s = np.arange(0, 10.11, 0.1)
K_s = np.arange(0, 10.11, 0.1)
A = 1
xx, yy = np.meshgrid(K_s, L_s)

layout = go.Layout(
    title = "Cobb-Douglas Production Function", autosize=False, width=500, height=500, margin = dict(l = 65, r = 50, b = 65, t = 90),
    scene = dict(xaxis = dict(title = 'K'), yaxis = dict(title = 'L'), zaxis = dict(title = 'Y'))
)

fig = go.Figure(layout = layout)

active = None
alphas = []
for i, alpha in enumerate(np.arange(0.1, 1.01, 0.1)):
    alphas.append(alpha)
    if alpha == 0.5:
        active = i
    V = cobb_douglas(A, xx, yy, alpha)
    fig.add_trace(go.Surface(
        z = V, contours = go.surface.Contours(
            z = go.surface.contours.Z(
                show = False, project = dict(z = True)
            )
        ), colorscale = "Electric", showscale = False, name=f"alpha = {alpha}", visible=False
    ))
    
fig.data[active].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update", args=[
            {"visible": [False] * len(fig.data) + [True]},
        ], label=f"alpha = {alphas[i]}"
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)
    
sliders = [dict(
    active=active,
    currentvalue={"prefix": ""},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(sliders=sliders, width=500, height=600)

orig_V = orig_cobb_douglas()
fig.add_trace(go.Surface(
    z = orig_V, contours = go.surface.Contours(
        z = go.surface.contours.Z(
            show = False, project = dict(z = True)
        )
    ), colorscale = "Viridis", showscale = False, name="alpha = 0.5"
))

plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')

display(HTML(filename))


# $\alpha$ and $\beta$ are called the output elasticities of capital and labor, respectively. They measure the responsiveness of output to a change in the levels of either labor or capital, holding all else constant. This means that if $\alpha$ or $\beta$ were high, then any small increase in their respective input would lead to a relatively large increase in output. As an example, if $\alpha$ was 0.4, then a 1% increase in capital would lead to a 0.4% increase in output.
# 
# Note, we assume that there are constant returns to scale. Thus, an increase in $\alpha$ necessarily means $\beta$ decreases. This reveals something important when comparing countries: the higher the $\alpha$, the more capital-intensive the country's production is. This means that $\alpha$ and $\beta$ give economists and policymakers insight as to how resources are allocated across nations.

# ## Returns to Scale
# 
# The significance of the exponents adding up to 1 ($\alpha + \beta = 1$) is that this implies constant returns to scale. If all inputs are scaled by a common non-zero factor, the output will be scaled by that same factor. Below is a generalization of this:
# 
# $$\begin{aligned}
# Y &= A (c \cdot K)^\alpha (c \cdot L)^{1 - \alpha} \\
# &= A c^\alpha K ^ \alpha c^{1 - \alpha}L^{1 - \alpha} \\
# &= A c^{\alpha + 1 - \alpha}K^\alpha L^{1 - \alpha} \\
# &= c \cdot A K^\alpha L^{1 - \alpha}
# \end{aligned}$$
# 
# Thus, any increase in either of the inputs will lead to a 1-1 increase in output. This is a significant assumption to make, as it essentially incentivizes companies to continue to "scale" their production inputs. They are not losing out on how much return is produced - they are getting output that matches exactly what they put into production.
# 
# The alternative case is when $\alpha + \beta < 1$. This is called decreasing returns to scale, and occurs when a company scales their production inputs by a factor of c, but gets a scaling in output that is less than c.
# 
# The last case is the most profitable one, when $\alpha + \beta > 1$. This is called increasing returns to scale, and occurs when a company increases their production inputs by c, but gets an increase in output that is greater than c.
# 
# Let us visually examine how values of $\alpha$ and $\beta$ affect output.

# In[8]:


change_alpha_beta(2, filename="fig4.html")
display(HTML("fig4.html"))


# The above graph shows increasing returns to scale with $\alpha + \beta = 2$ (the purble-yellow surface) with constant returns to scale for comparison (the blue-yellow surface). Notice how the orange function no longer increases at a decreasing rate, but seems to mimic exponential growth. This is once again because of the definition of increasing returns to scale. As companies continue to increase their inputs by a factor of $c$, they see their output increase by more than that factor. Thus, as inputs $(K, L)$ increase, output will increase at an even faster rate than that - in this case by the square.

# In[9]:


change_alpha_beta(0.5, filename="fig5.html")
display(HTML("fig5.html"))


# The above graph exhibits decreasing returns to scale as $\alpha + \beta = 0.5$ (the purple-yellow surface) with constant returns to scale for comparison (the blue-yellow surface). This time, the orange production function flattens out far faster than the regular constant returns to scale function. You can prove this to yourself using the slider below, which adjusts the value of $\alpha + \beta$.

# In[18]:


filename = "fig8.html"

L_s = np.arange(0, 10.11, 0.1)
K_s = np.arange(0, 10.11, 0.1)
A = 1
xx, yy = np.meshgrid(K_s, L_s)

layout = go.Layout(
    title = "Cobb-Douglas Production Function", autosize=False, width=500, height=500, margin = dict(l = 65, r = 50, b = 65, t = 90),
    scene = dict(xaxis = dict(title = 'K'), yaxis = dict(title = 'L'), zaxis = dict(title = 'Y'))
)

fig = go.Figure(layout = layout)

active = None
default = 1
ab_sums = []
for i, ab_sum in enumerate(np.arange(0.1, 3.01, 0.1)):
    ab_sums.append(ab_sum)
    if ab_sum == default:
        active = i
    alpha, beta = ab_sum / 2, ab_sum / 2
    V = cobb_douglas(A, xx, yy, alpha, beta)
    fig.add_trace(go.Surface(
        z = V, contours = go.surface.Contours(
            z = go.surface.contours.Z(
                show = False, project = dict(z = True)
            )
        ), colorscale = "Electric", showscale = False, name=f"alpha + beta = {ab_sum}", visible=False
    ))
    
fig.data[active].visible = True

steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update", args=[
            {"visible": [False] * len(fig.data) + [True]},
        ], label=f"alpha + beta = {ab_sums[i]}"
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)
    
sliders = [dict(
    active=active,
    currentvalue={"prefix": ""},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(sliders=sliders, width=500, height=600)

orig_V = orig_cobb_douglas()
fig.add_trace(go.Surface(
    z = orig_V, contours = go.surface.Contours(
        z = go.surface.contours.Z(
            show = False, project = dict(z = True)
        )
    ), colorscale = "Viridis", showscale = False, name=f"alpha + beta = {default}"
))

plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')

display(HTML(filename))


#  
