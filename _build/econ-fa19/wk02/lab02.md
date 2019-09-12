---
interact_link: content/econ-fa19/wk02/lab02.ipynb
kernel_name: python3
title: 'Lab 2'
prev_page:
  url: /econ-fa19/wk02/Intro_to_Production
  title: 'Intro to Production'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

<table style="width: 100%;" id="nb-header">
    <tr style="background-color: transparent;"><td>
        <img src="https://d8a-88.github.io/econ-fa19/assets/images/blue_text.png" width="250px" style="margin-left: 0;" />
    </td><td>
        <p style="text-align: right; font-size: 12pt;"><strong>Economic Models</strong>, Fall 2019<br>
            Dr. Eric Van Dusen</p></td></tr>
</table>



{:.input_area}
```python
from datascience import *
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import pandas as pd
from utils import *
plt.style.use('seaborn-muted')
```




{:.input_area}
```python
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from matplotlib import patches
import csaps
```


# Welcome to Week 2 of Data 88. This week is about the **Supply Curve and Firm Behaviour**.

Supply of a commodity refers to the quantity of a commodity which producers or sellers are willing produce and offer for sale at a particular price in some given period of time.

Individual supply refers to supply offered by a single firm/producer. Market supply refers to supply offered by all the firms/producers in a market.

## Firms and Supply

To answer questions like at a given price, what will be the supply of a good in the market, we need to know the market supply curve. A supply curve is simply a curve (or graph) which shows the different quantites of a good that can be produced and the prices they will be produced at.

The individual supply curve shows the prices and quantities produced at those prices for a single firm. Market supply curve is the horizontal summation of the individual supply curves in the market.

The following table and graph will give an example of a market with two firm: A and B.



{:.input_area}
```python
market_supply = Table().with_columns("Price", make_array(2, 3, 4),
                                     "Quantity supplied by A", make_array(20, 30, 40),
                                     "Quantity supplied by B", make_array(30, 40, 50),
                                     "Market Supply", make_array(50, 70, 90))
market_supply
```




{:.input_area}
```python
plt.plot(market_supply.column(1), market_supply.column(0), marker='o')
plt.plot(market_supply.column(2), market_supply.column(0), marker='o')
plt.plot(market_supply.column(3), market_supply.column(0), marker='o')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(make_array("Quantity supplied by A","Quantity supplied by B","Market Supply"), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()
```


Market behaviour relating to supply is based on the behaviour of the individual firms that comprise it. Now, how does an individual firm make its decision about production?

It does so based on the costs associated with production. If the price of a good is enough to recover the costs, the firm produces. Generally, costs increase with the quantity of production. So, to induce producers to increase the quantity supplied, the prices need to increase to compensate for the increased costs.

We will split costs into two categories: Fixed costs and Variable costs.

Fixed Costs are costs associated with fixed factors (or inputs) of production. For example, land for a factory, capital equipment like machinery, etc. The quantity of these inputs cannot be changed quickly in the short term. A factory owner cannot purchase land quickly enough to ramp up production in a week. A key point to note is that fixed costs are irrespective of the quantity, i.e., they do not change with the quantity produced.

Variable Costs are costs associated with variable factors (or inputs) of production. For example, labor, raw materials, etc. The quantity of these inputs can be changed quickly in the short term to adjust supply. A factory owner can hire more laborers or purchase more raw material to increase output. Variable costs change as the supply changes.

The following table will give an example of a firms costs. The columns are:

* **Output:** Units produced and supplied
* **Total Fixed Cost (TFC):** Cost incurred by firm on usage of all fixed factors.
* **Total Variable Cost (TVC):** Cost incurred by firm on usage of all variable factors.
* **Total Cost (TC):** Sum of the total fixed and variable costs
* **Marginal Cost (MC):** Addition to total cost as one more unit of output is produced
* **Average Fixed Cost (AFC):** Cost per unit of fixed factors
* **Average Variable Cost (AVC):** Cost per unit of variable factors
* **Average Total Cost (ATC):** Total cost per unit



{:.input_area}
```python
individual_firm_costs = Table.read_table('individual_firm_costs.csv')
individual_firm_costs
```


We are going to calculate all of the above mentioned curves using the data above.

First, lets calculate Total cost, which is the sum of total fixed cost and total variable cost.




{:.input_area}
```python
total_cost = individual_firm_costs.column("Total Fixed Cost") + individual_firm_costs.column("Total Variable Cost")
total_cost
```




{:.input_area}
```python
# adding the array to the table
individual_firm_costs = individual_firm_costs.with_column("Total Cost", total_cost)
individual_firm_costs
```


AFC can be calculated as the TFC divided by the output.



{:.input_area}
```python
# At zero level of output, we would by dividing by zero, which is invalid.
# So, we will calcuate for all other output levels and add the value for AFC manually at zero.
# While there should be no value for Average Fixed Cost at output zero, we will put a zero there for coding reasons.
# We will remove the first row by using .take() to select only rows in the range of indices from 1 to num_rows
# np.append(array1, array2) merges the two arrays, with array1 being the first array
individual_firm_costs_no_first = individual_firm_costs.take(np.arange(1, individual_firm_costs.num_rows))
average_fixed_cost = individual_firm_costs_no_first.column("Total Fixed Cost") / individual_firm_costs_no_first.column("Output")
average_fixed_cost = np.append(make_array(0), average_fixed_cost)
average_fixed_cost
```




{:.input_area}
```python
individual_firm_costs = individual_firm_costs.with_column("Average Fixed Cost", average_fixed_cost)
individual_firm_costs
```


Similarly, AVC can be calculated as the TVC divided by the output.



{:.input_area}
```python
average_variable_cost = individual_firm_costs_no_first.column("Total Variable Cost")/individual_firm_costs_no_first.column("Output")
average_variable_cost = np.append(make_array(0), average_variable_cost)
average_variable_cost
```




{:.input_area}
```python
individual_firm_costs = individual_firm_costs.with_column("Average Variable Cost", average_variable_cost)
individual_firm_costs
```


Similarly, ATC can be calculated as the TC divided by the output.



{:.input_area}
```python
average_total_cost = individual_firm_costs_no_first.column("Total Cost")/individual_firm_costs_no_first.column("Output")
average_total_cost = np.append(make_array(0), average_total_cost)
average_total_cost
```




{:.input_area}
```python
individual_firm_costs = individual_firm_costs.with_column("Average Total Cost", average_total_cost)
individual_firm_costs
```


MC can be calculated as the difference between TC at current output level and TC at previous output level (or TVC, as TFC is fixed).

For this we are going to use the function `np.diff`. You can read about it on http://data8.org/sp19/python-reference.html



{:.input_area}
```python
marginal_cost = np.diff(total_cost)
marginal_cost = np.append(make_array(0), marginal_cost)
marginal_cost
```




{:.input_area}
```python
individual_firm_costs = individual_firm_costs.with_column("Marginal Cost", marginal_cost)
individual_firm_costs
```


Let's look at some plots!



{:.input_area}
```python
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Fixed Cost"), marker='o')
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Variable Cost"), marker='o')
plt.plot(individual_firm_costs.column("Output"), individual_firm_costs.column("Total Cost"), marker='o')
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('TFC, TVC and TC')
plt.legend(make_array("Total Fixed Cost","Total Variable Cost","Total Cost"))

plt.show()
```




{:.input_area}
```python
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Fixed Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Variable Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Total Cost")[1:], marker='o')
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('AFC, AVC and ATC')
plt.legend(make_array("Average Fixed Cost","Average Variable Cost","Average Total Cost"))

plt.show()
```




{:.input_area}
```python
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Marginal Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Variable Cost")[1:], marker='o')
plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Total Cost")[1:], marker='o')
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('Mc, AVC and ATC')
plt.legend(make_array("Marginal Cost","Average Variable Cost","Average Total Cost"))

plt.show()
```




{:.input_area}
```python
output = individual_firm_costs.column("Output")[1:]
mc = individual_firm_costs.column("Marginal Cost")[1:]
avc = individual_firm_costs.column("Average Variable Cost")[1:]
atc = individual_firm_costs.column("Average Total Cost")[1:]

sp_mc = csaps.UnivariateCubicSmoothingSpline(output, mc, smooth=0.85)
sp_avc = csaps.UnivariateCubicSmoothingSpline(output, avc, smooth=0.85)
sp_atc = csaps.UnivariateCubicSmoothingSpline(output, atc, smooth=0.85)

output_s = np.linspace(output.min(), output.max(), 150)
mc_s = sp_mc(output_s)
avc_s = sp_avc(output_s)
atc_s = sp_atc(output_s)

plt.plot(output, mc, marker = 'o', color = 'tab:blue')
plt.plot(output_s, mc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:blue')
plt.plot(output, avc, marker = 'o', color = 'tab:green')
plt.plot(output_s, avc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:green')
plt.plot(output, atc, marker = 'o', color = 'tab:orange')
plt.plot(output_s, atc_s, alpha=0.7, lw = 2, label='_nolegend_', color = 'tab:orange')
plt.hlines(y=min(avc), xmin = 6, xmax = 8, lw=3, color='r', zorder = 10)
plt.hlines(y=min(atc), xmin = 7.5, xmax = 9.5, lw=3, color='r', zorder = 10)
plt.xlabel('Quantity')
plt.ylabel('Cost')
plt.title('MC, AVC and ATC')
plt.legend(make_array("Marginal Cost","Average Variable Cost","Average Total Cost"))

plt.show()
```


What do you notice? A company decides to produce if it the price is greater than or equal to its Average Variable Cost.

There are 3 different scenarios: they do not produce at all, they produce at a loss (minimising quantity), and they produce at a profit. Play around with the slider to see them.



{:.input_area}
```python
interact(lambda price: firm_behaviour(price, individual_firm_costs), price=widgets.IntSlider(min=20,max=60,step=1,value=25));
```


In the above example, if the price is 24, for any amount of production, the firm will lose money. In this case, they shut down and the loss is limited to its fixed costs.

If the price is above the minimum of AVC (25 in the example), for some amount of production, the firm will maximise its profits (or minimise its losses). Profits are Total Revenue minus Total Costs, where Total Revenue is Price times Quantity.

Therefore, based on the price, each firm looks at its costs and makes a decision to produce. At low prices, only the firms with the lowest production costs produce. As the price increases, firms with higher production costs find it feasible to produce and begin to supply. Thus, the market supply rises with higher prices. Firms with lower costs make extra profits. 

## An Example from EEP 147

Let's look at a real life example! This comes from **EEP 147 Regulation of Energy and the Environment**. 



{:.input_area}
```python
ESG_table = Table.read_table('ESGPorfolios_forcsv.csv').select(
    "Group", "Group_num", "UNIT NAME", "Capacity_MW", "Total_Var_Cost_USDperMWH").sort(
    "Total_Var_Cost_USDperMWH", descending = False).relabel(4, "Average Variable Cost")
```




{:.input_area}
```python
ESG_table
```


This table shows some electricity producers and their costs. You can think about the Capacity as the output the firm is capable of producing. The Average Variable Cost shows the minimum variable cost per MW produced. At a price below AVC, the firm supplies nothing. At a price above the AVC, the firm can supply upto its capacity. Being a profit maximising firm, it will try to supply its full capacity.

First, lets look at just the Big Coal producers and understand the data.



{:.input_area}
```python
selection = 'Big Coal'
Group = ESG_table.where("Group", selection)
```




{:.input_area}
```python
Group
```




{:.input_area}
```python
# Make the plot
plt.figure(figsize=(9,6))
plt.bar(new_x_group, height_group, width=width_group, edgecolor = "black")
# Add title and axis names
plt.title(selection)
plt.xlabel('Capacity_MW')
plt.ylabel('Variable Cost/Price')

plt.show()
```


This figure is the Big Coal Supply curve. It shows the price of electricity, and the quantity supplied at those prices (which depends on Variable Cost). For example, at any Variable Cost at or above 36.5, the producer FOUR CORNERS	(the one with the lowest production costs) will supply, and so on.

Lets interact with it.



{:.input_area}
```python
interact(group_plot, price=widgets.IntSlider(min=20,max=80,step=1,value=37));
```


We are going to repeat the same process, this time for all the energy sources. They have been colored according to source for reference.



{:.input_area}
```python
interact(ESG_plot, price=widgets.IntSlider(min=0,max=90,step=1,value=37));
```


 
