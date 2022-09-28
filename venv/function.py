import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn
import csv
from matplotlib.figure import Figure
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages

data = pd.read_csv("data.csv",delimiter=';',header=0)






def output(value):
    x = len(plt.get_fignums())
    #fig, ax = plt.subplots(x, 1)
    #figs = list(map(plt.figure, plt.get_fignums()))
    #print("Number of figures created: ", len(plt.get_fignums()))
    #fig, axis = plt.subplots(len(plt.get_fignums()))
    filename = "output.pdf"
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.set_dpi(value)
        fig.savefig(pp, format='pdf')
    pp.close()
    plt.savefig('my_eps_plot.eps')
    plt.show()

def chart(df, array,value):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig = plt.figure(figsize=(6, 4))
    fig.set_dpi(value)
    plt.plot(x, y, label=r'$Test$',color='red')
    plt.legend(loc="upper left")
    plt.xlabel(array[0])
    plt.ylabel(array[1])

def scatter(df,array,value):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig = plt.figure(figsize=(6, 4))
    fig.set_dpi(value)
    plt.xlabel(array[0])
    plt.ylabel(array[1])
    plt.scatter(x, y,color='red')

def hist(df,array,value):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig = plt.figure(figsize=(6, 4))
    fig.set_dpi(value)
    plt.xlabel(array[0])
    plt.ylabel(array[1])
    plt.hist(y,bins = 'auto',color='red',alpha=0.7, rwidth=0.85)

