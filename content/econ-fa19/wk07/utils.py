import pandas as pd
from datascience import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np 

def to_table(file_name):
    data = pd.read_csv(file_name, engine = "python")
    data = Table.from_df(data.fillna(-1))
    return data
        
def all_scatter(data_table, columnX, columnY):
    country_list = data_table.group("country").column("country")
    for country in country_list:
        curr_data_table = data_table.where("country", country)
        x = curr_data_table.column(columnX)
        y = curr_data_table.column(columnY)
        plt.plot(x, y, '-o', label =  country, linewidth = 1)
    
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize = 'x-large')
    plt.xlabel(columnX)
    plt.ylabel(columnY)
    plt.axis()