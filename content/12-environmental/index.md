## What is Environmental Economics?

![windmills.png](attachment:windmills.png)

In a broad sense, the field of Environmental Economics aims to relate and apply economic concepts (many of whom you're familiar with already) with the environment.
 
Central to Environmental Economics is the claim that the usage or degradation resources in the environment, our "environmental amenities", have an intrinsic value to humans that goes unaccounted for in the current market model. These unaccounted costs are considered *market failures* and carry *negative externalities*.
 
A great example of a negative externality is the emission of greenhouse gases (carbon dioxide, methane, nitrous oxide) from the combustion of hydrocarbons (gasoline, diesel, oil). The *true cost*  is not reflected in the lower price one pays at e.g the gas station. Consequently, the equilibrium quantity consumed is higher than the *socially optimal quantity*. As environmental economists, we're thus faced with the question: How could we reduce the quantity to the social optimum and weight in the *costs and benefits* of such a reduction? This is often a truly tricky question to answer!
 
As a result, a major proportion of research and work within the field is devoted to building tools to reveal, address, and evaluate economic policies aimed at *internalizing* these externalities. Here, your knowledge from data science comes in handy! Very often, these tools are applied by a government which interferes with the market to a varying degree. Hence, we tend to divide the environmental economic policies into two subfields:
 
* **Prescriptive**: When the government manually controls a negative externality, e.g letting each emitter in the market emit a fixed amount of GHG gases.
 
* **Market-based**: Where the government sets an emission goal, then introduces incentives or subsidies to alter market behaviour. It is left to each market actor to decide how much to emit. A carbon tax and a cap-and-trade (carbon quotas) are examples of marked-based interventions.
 
A commonly used environmental economic tool is **The McKinsey Marginal Abatement Cost Curve (MAC)** which aims to reveal the *cost of abatement* (not emitting) greenhouse gases from the atmosphere using various strategies. It stems from the McKinsey 2009 "Pathways to a Low Carbon Economy" and is a splendid example of the applications of Environmental Economics in Data Science. In this notebook, we'll walk through the concepts of it and build one of our own! In another notebook, we'll attempt creating the **Environmental Kuznets Curve Hypothesis** through data, and look at reasons why it might be both wrong and right!
 
As you read through this, remember: This is just the tip of the iceberg in the applications of data science in environmental economics, and there is much more to explore if you chose to follow this exciting path.

## Learning objectives

* An introductory understanding of what the field of Environmental Economics is and what it aims to accomplish.
* A thorough understanding of The McKinsey Greenhouse Gas (GHG) Abatement Cost Curve and its data science application.
* A familiarity of the Marginal Abatement Curve's limitations and the concept of Capital Intensity.
* An understanding of the important difference between static and dynamic cost.
* An understanding of the Environmental Kuznets Curve Hypothesis and its data science applications.