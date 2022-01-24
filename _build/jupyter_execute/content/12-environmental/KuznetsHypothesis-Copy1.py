#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
#Importing packages
from datascience import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches
get_ipython().run_line_magic('matplotlib', 'inline')


# # Environmental Kuznets Curve Hypothesis
# 
# The Environmental Kuznets curve hypothesis that the economic development of a nation is associated with a downward-facing U-shape.  The Y-axis is in terms of the level of environmental degradation (e.g pollution, water quality, deforestation.  The X-axis would be the GDP/capita.  The idea is that the environmental degradation worsens, until a certain level of income, and after which it gets better. In the US this could be seen in terms of air or water quality, where the skies or rivers were very polluted in the 1960s, until the Clean Air Act and Clean Water Act were passed and Air Quality and Water Quality improved.  Another motivation for the downward slope would be the idea that at some point a wealthier society demands environmental improvements.  
# However - could this hold for the potentially most important Pollutant C02, the main driver of anthropogenic climate change.  Controversially the impacts of global CO2 pollution are not experienced locally, but are experienced as global effects. So it is not clear whether the Environmental Kuznets hypothesis will hold.  
# 
# Today, we'll look to build an C02 Kuznets curve for an *association* between the amount of CO2 emitted per capita (t/CO2) and the growing GDP per capita (USD). This dataset is collected from Our World in Data, a great source of all sorts of data types!
# 
# 

# ![kuznets.png](kuznets.png)

# ## Building our own Environmental Kuznets Curve

# 
# We start by importing data on GDP per capita and Per Capita CO2 emissions for every country in the world for as long as it has been recorded.

# In[2]:


co2_table = Table.read_table('co2-emissions-vs-gdp.csv').drop('145446-annotations','Total population (Gapminder, HYDE & UN)','Code')
co2_table = co2_table.relabeled('Entity', 'Country')
co2_table


# ### Low Income Countries  
# Let's start by selecting a set of Low Income Countries to graph the movement of CO2 intensity

# In[3]:


#Low-Income Nations
LIH_array = make_array('Haiti', 'Afghanistan','Rwanda','Pakistan', 'Nicaragua')
LIH_table = co2_table.where('Country', are.contained_in(LIH_array))
LIH_table = LIH_table.where('GDP per capita', are.above_or_equal_to(0)).where('Per capita CO2 emissions', are.above_or_equal_to(0))
plt.figure(figsize = (8,6), dpi=250)
LIH_table.scatter('GDP per capita', 'Per capita CO2 emissions',group='Country') 


# Note that each dot represents a nation at a given level of emissions and GDP per capita
# 
# With these three countries we see a few different stories:
#  - In Afghanistan, Haiti and Rwanda we see little income growth and little CO2 intensity growth with a slight upward trend
#  - In Nicaragua we see some jumping around, in fact Nicaragua GDP per capita has gone up and down, as has CO2 per capita
#  - In Pakistan, a larger and more populous country we see strong linear upward growth in both GDP per capita and CO2 per capita, with no signs of turning down
# 
# In these countries it is hard to tell the complete story without the exact time trend.
# 

# ### BRICS  
# Lets look at the BRICS countries, the rapidly growing upper middle income countries

# In[4]:


BRICS_array = make_array('Brazil','Russia','India','China','South Africa')
BRICS_table = co2_table.where('Country', are.contained_in(BRICS_array))
BRICS_table = BRICS_table.where('GDP per capita', are.above_or_equal_to(0)).where('Per capita CO2 emissions', are.above_or_equal_to(0))
BRICS_table.scatter('GDP per capita', 'Per capita CO2 emissions',group='Country')


# The BRICS nations seem to have a variety of development pathways but all show the linear trend of increasing emissions as wealth grows.  
# - Russia has an interesting dip while GDP per capita decrease and then increase again
# - South Africa has a recent period where growth in both GDP per capita and CO2 per capita have stagnated
# - China and India show linearly increasing trends, with China both wealthier and more CO2 intensive

# ## Individual country graphs
# Lets look at some individual countries, starting with the US.   
# We can plot both total and logged quantities

# ### USA

# In[5]:


US_table = co2_table.where('Country', 'United States').where('Year', are.between(1800,2018))
US_table = US_table.with_column('LogGDP', np.log(US_table.column('GDP per capita'))).with_column('LogCO2',np.log(US_table.column('Per capita CO2 emissions')))
US_table.scatter('GDP per capita', 'Per capita CO2 emissions')
US_table.scatter('LogGDP', 'LogCO2')


# **Looks like we have a curve!**
# 
# In the case of the US it does indeed look like the C02 per capita does indeed start to deline after about $40,000
# Somewhere around 2000-2004 the CO2 emissions leveled off and then began to decline
# 

# ### China
# 
# In COP26, China has been a large part of the discussion (and emissions). Let's have a look at their curve!

# In[6]:


#China Example + LOG
NO_table = co2_table.where('Country', 'China').where('Year', are.between(1800,2018))
NO_table = NO_table.with_column('LogGDP', np.log(NO_table.column('GDP per capita'))).with_column('LogCO2',np.log(NO_table.column('Per capita CO2 emissions')))
NO_table.scatter('GDP per capita', 'Per capita CO2 emissions')
NO_table.scatter('LogGDP', 'LogCO2')


# Indeed it appears that China has an inflection point and is starting to level off in the Carbon intensity per capita
# 

# ### India
# 
# What about India?

# In[7]:


#India Example + LOG
NO_table = co2_table.where('Country', 'India').where('Year', are.between(1800,2018))
NO_table = NO_table.with_column('LogGDP', np.log(NO_table.column('GDP per capita'))).with_column('LogCO2',np.log(NO_table.column('Per capita CO2 emissions')))
NO_table.scatter('GDP per capita', 'Per capita CO2 emissions')
NO_table.scatter('LogGDP', 'LogCO2')


# ### Norway
# 
# As I'm Norwegian, I thought it might be cool to see how things are going back home as well:

# In[8]:


#Norway Example + LOG
NO_table = co2_table.where('Country', 'Norway').where('Year', are.between(1800,2018))
NO_table = NO_table.with_column('LogGDP', np.log(NO_table.column('GDP per capita'))).with_column('LogCO2',np.log(NO_table.column('Per capita CO2 emissions')))
NO_table.scatter('GDP per capita', 'Per capita CO2 emissions')
NO_table.scatter('LogGDP', 'LogCO2')


# Turns out we're ahead of the US in CO2 emissions per capita, but there's still a long way to go until our development resembles a full Kuznets curve. However, it certainly looks like something! An almost vertical linear growth in terms of per capita CO2 emissions in the early economic stages stagnated into a period of fluctuations. As of now, it looks like it’s heading in a downward trend.
# 
# Let's look at a set of other High Income Nations:

# In[9]:


HIN_array = make_array('United States', 'Netherlands', 'United Kingdom','Germany','Canada')
HIN_table = co2_table.where('Country', are.contained_in(HIN_array))
HIN_table = HIN_table.where('GDP per capita', are.above_or_equal_to(0)).where('Per capita CO2 emissions', are.above_or_equal_to(0))
HIN_table.scatter('GDP per capita', 'Per capita CO2 emissions',group='Country')


# As in the US and Norway, these nations have experienced a boom, stagnation, and now to some extent a downward trend. Let's finally plot all the previously observed nations together:

# In[10]:


ALL_array = np.append((np.append(LIH_array,BRICS_array)), HIN_array)
ALL_table = co2_table.where('Country', are.contained_in(ALL_array))
ALL_table = ALL_table.where('GDP per capita', are.above_or_equal_to(0)).where('Per capita CO2 emissions', are.above_or_equal_to(0))
ALL_table.scatter('GDP per capita', 'Per capita CO2 emissions',group='Country')
#What do we see? Can we spot the Environmental Kuznets Curve?


# Here we see evidence for an Environmental Kuznets Curve.
# 
# It seems, at least to some extent, that as nations develop economically, the level of environmental degradation reaches a peak and then declines, mapping a downward-facing U-curve. 

# ## Criticism of the Environmental Kuznets Curve Hypothesis

# Some questions we ought to ask ourselves in the end are:
# * Do all types of environmental degradation follow the curve? What if we plot Energy, Land, & Resource usage?
# * What we plotted today shows the ratio between GDP and CO2 per capita, but what about the *absolute* numbers of emissions?
# * What is the true long-term shape of the curve? Could it reshape itself to an "N" as an economy passes a certain threshold?
# * What about its applicability on a global scale? Knowing that the HINs have a habit of exporting pollution to LINs, what will happen as LIN grow economically?
# 
# These are just some questions environmental economists have asked themselves throughout the years since the curve was hypothesized in 1955. Some, including Perman and Stern (2003) conclude that the level of environmental degradation has much more to do with a constant "battle" between scale and time than income alone. As nations scale up (BRICS, for instance) the growth results in higher emissions, while countries with lower growth (LIN & HIN) seem more influenced by the "time-effect", which results in lower emissions. Others, among Krueger & Grossman, argue that there is "no evidence that environmental quality deteriorates steadily with economic growth."
# 
# More on these theories can be found in the recommended readings below.
# 
# As data scientists motivated to help heal the plant with the tools of environmental economics, we can help to find these answers!
# 

# ## What's next?

# If you are interested in this area, there are even more fascinating applications of Data Science to environmental topics such as: finding the social cost of carbon, the valuation of our environment, and the economics of emissions trading. Besides purely economical modeling, the field of environmental data science is rapidly growing as we collect more and more data on our planet and its resources. Applying the power of Satellite Imagery, Machine Learning, and Geographic Information Systems (GIS), one can follow both technology and policy-based paths, both ensured to have a positive impact in shaping a data-driven, sustainable future.

# ## Further recommended readings

# Levelized Cost of Carbon Abatement: An Improved Cost-Assessment Methodology for a Net-Zero Emissions World (also the main source of this Jupyter Notebook)
# 
# https://www.energypolicy.columbia.edu/sites/default/files/file-uploads/LCCA_CGEP-Report_101620.pdf
# 
# Dynamic vs. Static costs are described further in K.Gillingham & J.H Stock's The Cost of Reducing Greenhouse Gas Emissions (italic) from 2018. - A highly recommended reading out of scope for this class.
# 
# https://scholar.harvard.edu/files/stock/files/gillingham_stock_cost_080218_posted.pdf
# 
# Goldman Sachs Research: Carbonomics: The Future of Energy in the Age of Climate Change
#   
# https://www.goldmansachs.com/insights/pages/carbonomics.html
# 
# EPA article on the Economics of Climate Change:
# https://www.epa.gov/environmental-economics/economics-climate-change
# 
# Draw your own curve program:
# https://tamc.github.io/macc/
# 
# Abatement curve for crops:
# https://github.com/aj-sykes92/ggmacc/blob/main/README_files/figure-gfm/full-macc-1.png
# 
# 
# Aalborg University's software:
# https://github.com/matpri/EPLANoptMAC
# 
