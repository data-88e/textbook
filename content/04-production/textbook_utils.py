import pandas as pd
from datascience import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np 
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display, HTML

def cobb_douglas(A, K, L, alpha, beta = None):
    if beta is None:
        return A * K ** alpha * L ** (1 - alpha)
    else:
        return A * K ** alpha * L ** (beta)
        
def cobb_douglas_plotter_K(A, L_bar, alpha, y):
    plt.plot(np.arange(0, 1.01, 0.01), y)
    plt.title(fr"Cobb-Douglas with $\bar L$ = {L_bar}, $A$ = {A} and $\alpha$ = {alpha}", size=16)
    plt.xlabel("Capital Stock", size=16)
    plt.ylabel("Output", size=16);
    
def cobb_douglas_plotter_L(A, K_bar, alpha):
    L_s = np.arange(0, 1.01, 0.01)
    V_3 = cobb_douglas(A, K_bar, L_s, alpha)
    plt.plot(L_s, V_3)
    plt.title(fr"Cobb-Douglas with $\bar K$ = {K_bar}, $A$ = {A} and $\alpha$ = {alpha}", size=16)
    plt.xlabel("Labor Force", size=16)
    plt.ylabel("Output", size=16);
    
def plot_cobb_douglas(V, orig_V, t0label="trace 0", t1label="trace 1", filename=None):
    data = [go.Surface(z = V, contours = go.surface.Contours(z = go.surface.contours.Z(show = False, project = dict(z = True))),
                      colorscale = "Electric", showscale = False, name=t0label),
           go.Surface(z = orig_V, contours = go.surface.Contours(z = go.surface.contours.Z(show = False, project = dict(z = True))),
                     colorscale = "Viridis", showscale = False, name=t1label)]
    layout = go.Layout(title = "Cobb-Douglas Production Function", autosize=False, width=500, height=500, margin = dict(l = 65, r = 50, b = 65, t = 90),
                       scene = dict(xaxis = dict(title = 'K'), yaxis = dict(title = 'L'), zaxis = dict(title = 'Y')))
    fig = go.Figure(data = data, layout = layout)
    if filename:
        plot(fig, filename=filename, auto_open=False, include_mathjax='cdn')
    else:
        iplot(fig)
    
def orig_cobb_douglas():
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    alpha = 0.5
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    return curr_V

def change_A(A, filename=None):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    alpha = 0.5
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    plot_cobb_douglas(curr_V, orig_cobb_douglas(), fr"A = {A}", r"A = 1", filename=filename)
    
def change_alpha(alpha, filename=None):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha)
    plot_cobb_douglas(curr_V, orig_cobb_douglas(), fr"alpha = {alpha}", f"alpha = 0.5", filename=filename)

def change_alpha_beta(alpha_beta_sum, filename=None):
    L_s = np.arange(0, 10.11, 0.1)
    K_s = np.arange(0, 10.11, 0.1)
    A = 1
    alpha = alpha_beta_sum / 2
    beta = alpha_beta_sum / 2
    xx, yy = np.meshgrid(K_s, L_s)
    curr_V = cobb_douglas(A, xx, yy, alpha, beta)
    plot_cobb_douglas(curr_V, orig_cobb_douglas(), f"alpha + beta = {alpha_beta_sum}", f"alpha + beta = 1", filename=filename)

def MPK(A, K, L, alpha):
    return A * alpha * (K ** (alpha - 1)) * (L ** (1 - alpha))

def MPL(A, K, L, alpha):
    return A * (1 - alpha) * (K / L) ** alpha