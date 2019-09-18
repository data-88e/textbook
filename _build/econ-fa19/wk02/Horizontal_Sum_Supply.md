---
redirect_from:
  - "/econ-fa19/wk02/horizontal-sum-supply"
interact_link: content/econ-fa19/wk02/Horizontal_Sum_Supply.ipynb
kernel_name: python3
has_widgets: false
title: 'Horizontal Sum Supply'
prev_page:
  url: /lecture-intros/wk02.html
  title: 'The Supply Curve and Firm Behavior'
next_page:
  url: /econ-fa19/wk02/Intro_to_Production.html
  title: 'Intro to Production'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Horizontal Sum Supply



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# HIDDEN
import qgrid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

```
</div>

</div>



This Notebook will demonstrate using QGrid - a way to interact with the data in a table.  Unfortunately Qgrid works with Pandas, so this Notebook uses a pandas Dataframe as its data source. Here is the outline for this notebook:
1. First we will read in a dataframe with some Supply functions for 3 firms, they have 3 quantities they will supply at three possible prices
2. In the first part Firm C is not producing anything , and production is set at zero
3. We will create a market supply by summing the supply from Firm A and Firm B
4. When the widget is created - you can enter and edit the values of the cells




## DataFrame Widget



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
df_Market = pd.DataFrame({
    'Price' : [5, 10, 15],
    'A' : [20, 30, 40],
    'B' : [25, 35, 50], 
    'C' : [0, 0, 0],  })

df_Market['Total_Supply_ABC'] = df_Market['A'] + df_Market['B']+ df_Market['C']

qgrid_widget = qgrid.show_grid(df_Market, show_toolbar=True)
qgrid_widget

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
QgridWidget(grid_options={'fullWidthRows': True, 'syncColumnCellResize': True, 'forceFitColumns': True, 'defau…
```

</div>
</div>
</div>



So go in and play around with different values for firm C. Try $[12,17,55]$ or $[0,25,55]$.

What do we have to assume about C? It has to increase or stay the same as Price increases.



*Note - if you manipulate the data in the Qgrid widget - you need to save the dataframe - here we rename it as `updated_df`*



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df=qgrid_widget.get_changed_df()
updated_df['Total_Supply_ABC'] = updated_df['A'] + updated_df['B']+ updated_df['C']
updated_df

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>Price</th>
      <th>Total_Supply_ABC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>25</td>
      <td>0</td>
      <td>5</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30</td>
      <td>35</td>
      <td>0</td>
      <td>10</td>
      <td>65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>50</td>
      <td>0</td>
      <td>15</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



## Graphing
Now we are going to graph the individual supply curves of each firm, alongside the total Supply to crease a Market Supply



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# NO CODE
ax = plt.gca()
updated_df.plot(kind='line', y='Price', x='A', ax=ax)
updated_df.plot(kind='line', y='Price', x='B', ax=ax)
updated_df.plot(kind='line', y='Price', x='C', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_ABC', ax=ax)
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(("Quantity supplied by A","Quantity supplied by B","Quantity supplied by C", "Market Supply A+B"), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/econ-fa19/wk02/Horizontal_Sum_Supply_9_0.png)

</div>
</div>
</div>



## Thought Questions

1.  Can the individual supply lines cross?

2. Can individual supply schedules = 0, at a lower price?

3. Can lines bend backwards?




##  Market Analysis

### Supply, Demand, and New Market Entrant
Let's start again and add in
1. A demand function
2. A comparison of the supply with just firms A and B to with a third firm C
3. What happens to equilibrium Price and Quantity?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
qgrid_widget = qgrid.show_grid(updated_df, show_toolbar=True)
qgrid_widget

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
QgridWidget(grid_options={'fullWidthRows': True, 'syncColumnCellResize': True, 'forceFitColumns': True, 'defau…
```

</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
updated_df=qgrid_widget.get_changed_df()
updated_df['Total_Supply_AB'] = updated_df['A'] + updated_df['B'] 
updated_df['Total_Supply_ABC'] = updated_df['A'] + updated_df['B'] + updated_df['C']

```
</div>

</div>



Lets specify a Demand curve - prices and quantities - so we need Quantities demanded that correspond to a price of [5,10,15]



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Demand = [100,75,50]
updated_df['Demand'] = Demand
updated_df

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>Price</th>
      <th>Total_Supply_ABC</th>
      <th>Total_Supply_AB</th>
      <th>Demand</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>25</td>
      <td>0</td>
      <td>5</td>
      <td>45</td>
      <td>45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30</td>
      <td>35</td>
      <td>0</td>
      <td>10</td>
      <td>65</td>
      <td>65</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>50</td>
      <td>0</td>
      <td>15</td>
      <td>90</td>
      <td>90</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>
</div>


</div>
</div>
</div>



Now let's visualize the market supply.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# NO CODE
ax = plt.gca()
updated_df.plot(kind='line', y='Price', x='A', ax=ax)
updated_df.plot(kind='line', y='Price', x='B', ax=ax)
updated_df.plot(kind='line', y='Price', x='C', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_AB', ax=ax)
updated_df.plot(kind='line', y='Price', x='Total_Supply_ABC', ax=ax)
updated_df.plot(kind='line', y='Price', x='Demand', ax=ax)

plt.xlabel('Quantity')
plt.ylabel('Price')
plt.title('Market Supply')
plt.legend(("Quantity supplied by A","Quantity supplied by B","Quantity supplied by C", "Supply_AB","Supply_ABC", "Total Demand" ), bbox_to_anchor=(1.04,1), loc="center left")

plt.show()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](../../images/econ-fa19/wk02/Horizontal_Sum_Supply_17_0.png)

</div>
</div>
</div>



## More Thought Questions

1. What happens to the market price and quantity?  Can you eyeball the changes?
2. What happens to each individual producer - can you tell from this graph?
3. Should firm C enter the market?



 

