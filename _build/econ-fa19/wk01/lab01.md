---
interact_link: content/econ-fa19/wk01/lab01.ipynb
kernel_name: python3
title: 'Lab 1'
prev_page:
  url: /lecture-intros/wk01
  title: 'Sympy and LaTeX'
next_page:
  url: /lecture-intros/wk02
  title: 'The Supply Curve and Firm Behavior'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Lab 1: SymPy and LaTeX

Economics is in the world around us, and so is Data Science! It's in our every day lives. As we connect Data Science with Economics, we will be exploring real life datasets to illustrate how Economics concepts are shaped and how decisions lead to real-life impacts.

## Today's Lab

Some learning outcomes:
1. Navigate and use tools, such as Jupyter notebooks
2. Write and evaluate basic expressions in Python
3. Represent formulas and expressions in LaTeX
4. Write and evaluate functions, such as Supply and Demand, in SymPy
5. Calculus review 



Acknowledgement: prob140.org, opentextbc.ca

## Intro to Jupyter Notebooks

Welcome to Jupyter notebooks, a place used to write programs, write texts, and view the results.

Each rectangle is called a *cell*. There are two types of cells: text or code. Text cells, like this one, can be edited by double-clicking on them. 

To run a cell, click the "<i class="fa-step-forward fa"></i> Run" button on the top menu bar or hold `shift` + `return` (or `shift` + `enter`). 

<div class="alert alert-info">

<strong>Question 1.1:</strong> Try editing this paragraph so it only says "Economics is fun." Then click the Run or hold down <code>shift</code> + <code>return</code>. This sentence, for example, should be deleted. Edit by double-clicking this cell.

</div>

<div class="alert alert-success">
    
<strong>Answer:</strong> Economics is fun.

</div>

<div class="alert alert-info">

<strong>Question 1.2:</strong> Other cells contain code in Python 3 language. Running a cell with code will execute all the code it contains. To run the code in a code cell, first click on that cell to activate it. It'll be highlighted with a little green or blue rectangle. Run the following cells.

</div>



{:.input_area}
```python
#Run this cell
print("Hello, World!")
```


{:.output .output_stream}
```
Hello, World!

```



{:.input_area}
```python
print("Economics is fun!")
print("I love data science!")
```


{:.output .output_stream}
```
Economics is fun!
I love data science!

```

## LaTeX

A tool for presenting and formatting numeric formulas, functions, and symbols is LaTeX. To format with LaTex, place your equations and math in between dollar signs, $. 

For example, `$f(x) = 8x$`  gets formatted as  $f(x) = 8x$

Some other common operations:

Exponentials: `$x^{2}$` gets formatted as $x^{2}$

Fractions: `$\frac{x}{y}$` yields $\frac{x}{y}$

We can use LaTeX for formatting Supply and Demand curves and functions in Economics, such as $ P = 2Q + 4 $

Practice typing a few different expressions using LaTeX. 

<div class="alert alert-info">

<strong>Question 2.1:</strong> Type the Pythagorean theorem.

</div>

<div class="alert alert-success">
    
<strong>Answer:</strong> $a^2 + b^2 = c^2$  

LaTeX: <code>$a^2 + b^2 = c^2$</code>

</div>

<div class="alert alert-info">
    
<strong>Question 2.2:</strong> Type the Euclidian distance theorem.

</div>


<div class="alert alert-success">
    
<strong>Answer:</strong> $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ 

LaTeX: `$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$`

</div>

## Supply and Demand

In economics and the world around us, supply and demand make up the fundamentals. 

One assumption we make for the law of supply and law of demand is *ceteris paribus.* When we change one factor, all other variables are held constant. 

For the supply and demand curves, we plot price P goes on the vertical Y-axis and quantity Q on the horizontal X-axis. 

Note:  It is different than how conventional math classes show the 'independent variable' price P on the Y-axis.

Let's look at a real-world example of a dataset for gasoline. 



{:.input_area}
```python
#Run this cell to load the table
Table().with_columns(
    'Price (per gallon)', np.arange(1.00, 2.40, 0.2), 
    'Quantity Supplied (millions of gallons)', [500, 550, 600, 640, 680, 700, 720], 
    'Quantity Demanded (millions of gallons)', [800, 700, 600, 550, 500, 460, 420])
```





<div markdown="0" class="output output_html">
<table border="1" class="dataframe">
    <thead>
        <tr>
            <th>Price (per gallon)</th> <th>Quantity Supplied (millions of gallons)</th> <th>Quantity Demanded (millions of gallons)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1                 </td> <td>500                                    </td> <td>800                                    </td>
        </tr>
        <tr>
            <td>1.2               </td> <td>550                                    </td> <td>700                                    </td>
        </tr>
        <tr>
            <td>1.4               </td> <td>600                                    </td> <td>600                                    </td>
        </tr>
        <tr>
            <td>1.6               </td> <td>640                                    </td> <td>550                                    </td>
        </tr>
        <tr>
            <td>1.8               </td> <td>680                                    </td> <td>500                                    </td>
        </tr>
        <tr>
            <td>2                 </td> <td>700                                    </td> <td>460                                    </td>
        </tr>
        <tr>
            <td>2.2               </td> <td>720                                    </td> <td>420                                    </td>
        </tr>
    </tbody>
</table>
</div>



Supply refers to the amount of a good or service a producer is willing to supply for each given price. 

![supply](image1.png)

Demand is the amount of a good or service consumers are willing and able to purchase for each given price. 

![demand](image2.png)

In the next section, we will be exploring SymPy to find the intersection of the supply and demand curves, which marks the equilibrium point where both the price and quantity consumers are willing and able to buy at is equal to the price and quantity producers are willing to sell at.

![supply and demand](image3.png)

## SymPy

Python has many tools, such as the [SymPy library](https://docs.sympy.org/latest/tutorial/index.html) that we can use for expressing and evaluating formulas and functions in economics. 

Since SymPy helps with symbolic math, we start out by create a symbol using `Symbol`, which we assign to a variable name. Then, we can use the symbols for constructing symbolic expressions.

### Example 1



{:.input_area}
```python
x = Symbol('x')
x
```





$$x$$



Now let's try using SymPy for creating a symbolic expression for supply and demand curves.

Let's start out with an upward sloping Supply curve, where $P_S$ is price and $Q_S$ is quantity suppled. Create symbols for the variables $P_S$ and $Q$:



{:.input_area}
```python
P_S = Symbol('P_S')
P_S
```





$$P_{S}$$





{:.input_area}
```python
Q_S = Symbol('Q_S')
Q_S
```





$$Q_{S}$$





{:.input_area}
```python
#Supply curve
P_S = 2 * Q_S - 4
P_S
```





$$2 Q_{S} - 4$$



Now, use the same symbols $P_D$ and $Q_D$ to create an expression for a downward sloping Demand curve.



{:.input_area}
```python
Q_D = Symbol('Q_D')
Q_D
```





$$Q_{D}$$





{:.input_area}
```python
# Demand curve
P_D = 2 - Q_D
P_D
```





$$- Q_{D} + 2$$



Given the supply and demand curve, we set the two equations equal to each other and solve for the equilibrium price and equilibrium quantity. 



{:.input_area}
```python
P_D = P_S
```


Using SymPy, we call solve, which takes in the equation as the first argument followed by the variable we are solving for.



{:.input_area}
```python
solve(P_S, Q_S)
```





$$\left [ 2\right ]$$





{:.input_area}
```python
solve(P_S, P_D)
```





$$\left [ 0\right ]$$



The equilibrium price and quantity are 0 and 2, respectively. 

### Example 2
Let's suppose our demand function is $\text{Quantity}_{D}=-2 \cdot \text{Price}_{D} + 10$. Using SymPy, this would be




{:.input_area}
```python
q = Symbol("q")
demand = -2*q + 10
demand
```





$$- 2 q + 10$$



Suppose we have a supply function $\text{Price}_{S}=3 \cdot \text{Quantity}_{S} + 1$. Using SymPy, this would be




{:.input_area}
```python
supply = 3*q + 1
supply
```





$$3 q + 1$$



We will now try to find the market equilibrium. The market equilibrium is the price at which the quantity supplied and quantity demanded of a good or service is equal to each other. Hence, it is the point at which the demand and supply curves intersect. In the beginning of the workbook, we defined a function called solve which finds the x-value of a demand and supply curve's intersection. This point will be referred to as the equilibrium quantity, also known as $Q^*$. 




{:.input_area}
```python
def plot_equation(equation, price_start, price_end, label=None):
    plot_prices = [price_start, price_end]
    plot_quantities = [equation.subs(list(equation.free_symbols)[0], c) for c in plot_prices]
    plt.plot(plot_prices, plot_quantities, label=label)
    
def plot_intercept(eq1, eq2):
    ex = solve(eq1-eq2)[0]
    why = eq1.subs(list(eq1.free_symbols)[0], ex)
    plt.scatter([ex], [why])
    return (ex, why)
    
plot_equation(demand, 0, 5)
plot_equation(supply, 0, 5)
plt.ylim(0,20)
plot_intercept(supply, demand)
```





$$\left ( \frac{9}{5}, \quad \frac{32}{5}\right )$$




{:.output .output_png}
![png](../../images/econ-fa19/wk01/lab01_52_1.png)



## Calculus Review

Let's review partial derivatives, which is simplying taking derivatives with respect to the variable specified in the partial derivative. All other variables are treated as constants. 

For example, the partial derivative, with respect to $x$, of $2xy$ is $2y$.  Here, y is treated as a constant.

### Example 1

$\displaystyle\frac{\partial}{\partial y}(2xy) = 2x$

### Example 2

$\displaystyle\frac{\partial}{\partial x}(x^{4} + xy^{2} + x) = 4x^{3} + y^{2} + 1$

<div class="alert alert-info">

<strong>Question 3:</strong> Use LaTeX to find and display the partial derivatives.

</div>

**Question 3.1:** $\displaystyle\frac{\partial}{\partial x} (x^{2} + 8x)$

<div class="alert alert-success">
    
<strong>Answer:</strong> $2x + 8$

</div>

**Question 3.2:** $\displaystyle\frac{\partial}{\partial z} (5z^{6} + 10x^{2}yz^{2} + xyz + \ln(z))$

<div class="alert alert-success">
    
<strong>Answer:</strong> $30z^5 + 20 x^2yz + xy + \frac{1}{z}$

</div>

Congrats! You finished Lab 1! 

 
