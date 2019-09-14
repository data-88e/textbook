from datascience import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches

def firm_behaviour(price, individual_firm_costs):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])

    plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Variable Cost")[1:],marker='o')
    plt.plot(individual_firm_costs.column("Output")[1:], individual_firm_costs.column("Average Total Cost")[1:], marker='o')
    plt.xlabel('Quantity')
    plt.ylabel('Cost')
    plt.title('Production')
    plt.ylim(15, 105)
    plt.axhline(y=price, color='k', linewidth = 2)
    plt.legend(make_array("Average Variable Cost", "Average Total Cost", "price"))

    min_avc = min(individual_firm_costs.column("Average Variable Cost")[1:])
    min_atc = min(individual_firm_costs.column("Average Total Cost")[1:])
    output = max(individual_firm_costs.where("Marginal Cost", are.below_or_equal_to(price)).column("Output"))
    atc_at_output = individual_firm_costs.where("Output", output).column("Average Total Cost").item(0)
    if price < min_avc:
        print("No production")
    elif price >= min_avc and price<min_atc:
        print("Production at loss minimising quantity")
        ax.add_patch(patches.Rectangle((0, price),
                                       output, atc_at_output-price,
                                       color ='red', alpha=.3, zorder=1000))
    elif price >= min_atc:
        print("Production at a profit")
        ax.add_patch(patches.Rectangle((0, price),
                                       output, atc_at_output-price,
                                       color ='green', alpha=.3, zorder=1000))

def find_x_pos(widths):
    cumulative_widths = [0]
    cumulative_widths.extend(np.cumsum(widths))
    half_widths = [i/2 for i in widths]
    x_pos = []
    for i in range(0, len(half_widths)):
        x_pos.append(half_widths[i] + cumulative_widths[i])
    return x_pos

ESG_table = Table.read_table('ESGPorfolios_forcsv.csv').select(
    "Group", "Group_num", "UNIT NAME", "Capacity_MW", "Total_Var_Cost_USDperMWH").sort(
    "Total_Var_Cost_USDperMWH", descending = False).relabel(4, "Average Variable Cost")

selection = 'Big Coal'
Group = ESG_table.where("Group", selection)

width_group = Group.column("Capacity_MW")
height_group = Group.column("Average Variable Cost")
new_x_group = find_x_pos(width_group)

def production(price, table):
    if price < min(table.column(4)):
        print("No production")
    else:
        production = table.where(4, are.below_or_equal_to(price))
        total_production = sum(production.column(3))
        suppliers = production.column(2)
        print("Total Production/Market Supply: ", total_production)
        print("")
        print("Suppliers: ", suppliers)

def group_plot(price):
    production(price, Group)
    plt.figure(figsize=(9,6))
    plt.bar(new_x_group, height_group, width=width_group, edgecolor = "black")
    plt.title(selection)
    plt.xlabel('Capacity_MW')
    plt.ylabel('Variable Cost')
    plt.axhline(y=price, color='r', linewidth = 2)
    
width = ESG_table.column("Capacity_MW")
height = ESG_table.column("Average Variable Cost")
new_x = find_x_pos(width)

energy_colors_dict = {}
count = 0
colors = ['#EC5F67', '#F29056', '#F9C863', '#99C794', '#5FB3B3', '#6699CC', '#C594C5']
for i in set(ESG_table['Group']):
    energy_colors_dict[i] = colors[count]
    count += 1
    
colors_mapped = list(pd.Series(ESG_table['Group']).map(energy_colors_dict))
ESG_table = ESG_table.with_column('Color', colors_mapped)

def ESG_plot(price):
    production(price, ESG_table)
    plt.figure(figsize=(9,6))
    plt.bar(new_x, height, width=width, color=ESG_table['Color'], edgecolor = "black")
    plt.title('All Energy Sources')
    plt.xlabel('Capacity_MW')
    plt.ylabel('Variable Cost')
    plt.axhline(y=price, color='r', linewidth = 2)

    plt.figure(figsize=(5,1))
    plt.bar(energy_colors_dict.keys(), 1, color = energy_colors_dict.values())
    plt.xticks(rotation=60)
    plt.title('Legend')
