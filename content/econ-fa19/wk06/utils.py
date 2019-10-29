import matplotlib.pyplot as plt
import numpy as np
import sympy
from ipywidgets import HBox, VBox, Label, interactive_output, Accordion
import ipywidgets as widgets
from IPython.display import display
solve = lambda x,y: float(sympy.solve(x-y)[0]) if len(sympy.solve(x-y))==1 else "Not Single Solution"
plt.style.use("seaborn-muted")

Q = sympy.Symbol("Q")

create_line = lambda m, b: b + m * Q

def get_params(S_m, S_b, D_m, D_b, World_Price, Tariff):
    supply = create_line(S_m, S_b)
    demand = create_line(D_m, D_b)
    
    Q_star = solve(demand, supply)
    P_star_d = demand.subs(Q, Q_star)
    P_star_s = supply.subs(Q, Q_star)
    
    QD_FreeTrade = solve(demand, World_Price)
    QS_FreeTrade = solve(supply, World_Price)
    Imports_FreeTrade = QD_FreeTrade - QS_FreeTrade
    
    Protected_Price = World_Price + Tariff
    QD_Protected = solve(demand, Protected_Price)
    QS_Protected = solve(supply, Protected_Price)
    Imports_Protected = QD_Protected - QS_Protected
    
    Change_in_Imports = Imports_FreeTrade - Imports_Protected
    
    params_dict = {
        "supply" : supply,
        "demand" : demand,
        "Q_star" : Q_star,
        "P_star_d" : P_star_d,
        "P_star_s" : P_star_s,
        "QD_FreeTrade" : QD_FreeTrade,
        "QS_FreeTrade" : QS_FreeTrade,
        "Imports_FreeTrade" : Imports_FreeTrade, 
        "QD_Protected" : QD_Protected,
        "QS_Protected" : QS_Protected,
        "Imports_Protected" : Imports_Protected, 
        "Change_in_Imports" : Change_in_Imports,
        "World_Price" : World_Price,
        "Tariff" : Tariff,
        "Protected_Price" : World_Price + Tariff
    }
    
    return params_dict

def plot_equation(eq, p_start, p_end, **kwargs):
    plot_prices = [p_start, p_end]
    plot_quantities = [eq.subs(list(eq.free_symbols)[0],c) for c in plot_prices]
    plt.plot(plot_prices, plot_quantities, **kwargs)
    return plot_prices, plot_quantities
    
def plot_equilibrium(eq1, eq2, plot=False):
    x = solve(eq1, eq2)
    y = eq1.subs(list(eq1.free_symbols)[0], x)
    if plot:
        plt.scatter([x], [y])
    return x, y
    
def plot_intercept_tradeprice(eq, p, plot=False):
    x = solve(eq, p)
    y = p
    if plot:
        plt.scatter([x], [y])
    return x, y

def plot_1(S_m, S_b, D_m, D_b, World_Price, Tariff):
    params = get_params(S_m, S_b, D_m, D_b, World_Price, Tariff)
    supply_params = plot_equation(params["supply"], 0, 100, color="tab:blue")
    demand_params = plot_equation(params["demand"], 0, 100, color="tab:red")
    plt.hlines(params["World_Price"], 0, 100, linestyle="--")
    plt.ylim(0,2000)
    plt.xlim(0,100)
    plt.hlines(params["Protected_Price"], 0, 100, linestyle="--")
    plt.fill_between([0, params["QD_FreeTrade"]], 
                     [float(params["demand"].subs(Q, 0)), params["World_Price"]], 
                     [params["World_Price"], params["World_Price"]], alpha=0.3, color="tab:red")
    plt.fill_between([0, params["QD_Protected"], params["QD_FreeTrade"]], 
                     [params["Protected_Price"], params["Protected_Price"], params["World_Price"]], 
                     [params["World_Price"], params["World_Price"], params["World_Price"]], 
                     color="tab:red", alpha=0.3)


    plt.vlines(params["QS_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.vlines(params["QD_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.text(98, params["Protected_Price"]+25, "World Price + Tariff", fontsize=15, horizontalalignment="right")
    plt.text(98, params["World_Price"]+25, "World Price", fontsize=15, horizontalalignment="right")
    plt.legend(["Supply", "Demand"], loc=1, framealpha=1)
    plt.title("Consumers");
    
def plot_2(S_m, S_b, D_m, D_b, World_Price, Tariff):
    params = get_params(S_m, S_b, D_m, D_b, World_Price, Tariff)
    plot_equation(params["supply"], 0, 100, color="tab:blue")
    plot_equation(params["demand"], 0, 100, color="tab:red")
    plt.hlines(params["World_Price"], 0, 100, linestyle="--")
    plt.ylim(0,2000)
    plt.xlim(0,100)
    plt.hlines(params["Protected_Price"], 0, 100, linestyle="--")
    plt.fill_between([0, params["QS_Protected"]], 
                     [params["Protected_Price"], params["Protected_Price"]], 
                     [float(params["supply"].subs(Q, 0)), params["Protected_Price"]], alpha=0.3, color="tab:red")
    plt.fill_between([0, params["QS_FreeTrade"], params["QS_Protected"]], 
                     [params["Protected_Price"], params["Protected_Price"], params["Protected_Price"]], 
                     [params["World_Price"], params["World_Price"], params["Protected_Price"]], 
                     color="tab:red", alpha=0.3)
    plt.vlines(params["QS_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.vlines(params["QD_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.text(98, params["Protected_Price"]+25, "World Price + Tariff", fontsize=15, horizontalalignment="right")
    plt.text(98, params["World_Price"]+25, "World Price", fontsize=15, horizontalalignment="right")
    plt.legend(["Supply", "Demand"], loc=1, framealpha=1)
    plt.title("Producers");
    
def plot_3(S_m, S_b, D_m, D_b, World_Price, Tariff):
    params = get_params(S_m, S_b, D_m, D_b, World_Price, Tariff)
    plot_equation(params["supply"], 0, 100, color="tab:blue")
    plot_equation(params["demand"], 0, 100, color="tab:red")
    plt.hlines(params["World_Price"], 0, 100, linestyle="--")
    plt.ylim(0,2000)
    plt.xlim(0,100)
    plt.hlines(params["Protected_Price"], 0, 100, linestyle="--")
    plt.fill_between([params["QS_Protected"], params["QD_Protected"]], 
                     [params["Protected_Price"], params["Protected_Price"]], 
                     [params["World_Price"], params["World_Price"]], color="g", alpha=0.3)
    plt.vlines(params["QS_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.vlines(params["QD_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.text(98, params["Protected_Price"]+25, "World Price + Tariff", fontsize=15, horizontalalignment="right")
    plt.text(98, params["World_Price"]+25, "World Price", fontsize=15, horizontalalignment="right")
    plt.legend(["Supply", "Demand"], loc=1, framealpha=1)
    plt.title("Government");
    
def plot_4(S_m, S_b, D_m, D_b, World_Price, Tariff):
    params = get_params(S_m, S_b, D_m, D_b, World_Price, Tariff)
    plot_equation(params["supply"], 0, 100, color="tab:blue")
    plot_equation(params["demand"], 0, 100, color="tab:red")
    plt.hlines(params["World_Price"], 0, 100, linestyle="--")
    plt.ylim(0,2000)
    plt.xlim(0,100)
    plt.hlines(params["Protected_Price"], 0, 100, linestyle="--")
    plt.fill_between([params["QS_FreeTrade"], params["QS_Protected"]], 
                     [params["World_Price"], params["Protected_Price"]], 
                     [params["World_Price"], params["World_Price"]], 
                     color="grey", alpha=0.5)
    plt.fill_between([params["QD_Protected"], params["QD_FreeTrade"]], 
                     [params["Protected_Price"], params["World_Price"]], 
                     [params["World_Price"], params["World_Price"]], 
                     color="grey", alpha=0.5)
    plt.vlines(params["QS_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.vlines(params["QD_Protected"], 0, params["Protected_Price"], linestyle="--")
    plt.text(98, params["Protected_Price"]+25, "World Price + Tariff", fontsize=15, horizontalalignment="right")
    plt.text(98, params["World_Price"]+25, "World Price", fontsize=15, horizontalalignment="right")
    plt.legend(["Supply", "Demand"], loc=1, framealpha=1)
    plt.title("Deadweight Loss");
    
def all_four_plots(S_m, S_b, D_m, D_b, World_Price, Tariff):
    plt.figure(figsize=[15, 13])
    
    plt.subplot(221)
    plot_1(S_m, S_b, D_m, D_b, World_Price, Tariff)
    
    plt.subplot(222)
    plot_2(S_m, S_b, D_m, D_b, World_Price, Tariff)
    
    plt.subplot(223)
    plot_3(S_m, S_b, D_m, D_b, World_Price, Tariff)
    
    plt.subplot(224)
    plot_4(S_m, S_b, D_m, D_b, World_Price, Tariff)
    
def four_plot_widget():
    # generate the 6 necessary sliders
    S_m = widgets.IntSlider(value=20, min=0, max=100, step=5)
    S_b = widgets.IntSlider(value=200, min=0, max=1000, step=50)
    D_m = widgets.IntSlider(value=-20, min=-100, max=0, step=5)
    D_b = widgets.IntSlider(value=1800, min=1000, max=2000, step=50)
    World_Price = widgets.IntSlider(value=400, min=0, max=1000, step=50)
    Tariff = widgets.IntSlider(value=400, min=0, max=1000, step=50)
    
    # generate the widget
    out = interactive_output(all_four_plots, {"S_m":S_m, "S_b":S_b, "D_m":D_m, 
                                              "D_b":D_b, "World_Price":World_Price, "Tariff":Tariff})
    labels = ["Supply Slope", "Supply Intercept", "Demand Slope", "Demand Intercept",
             "World Price", "Tariff"]
    sliders = [S_m, S_b, D_m, D_b, World_Price, Tariff]
    pre_boxes = [[Label(l) for l in labels[0:3]], sliders[0:3], [Label(l) for l in labels[3:]], sliders[3:]]
    vboxes = [VBox(box) for box in pre_boxes]
    ui = HBox(vboxes)
    
    # display the widget
    display(ui, out)