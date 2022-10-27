import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn
import csv
from matplotlib.figure import Figure
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from gui import *

cm = 1/2.54

def chart(df,array,win):

    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig, ax = plt.subplots(figsize=(array[2] * cm, array[3] * cm), tight_layout=True)
    fig.set_dpi(array[4])
    ax.plot(x, y, label=r'$Test Label$', color='red')
    ax.set_xlabel(r'$'+array[0]+'$')
    ax.set_ylabel(r'$'+array[1]+'$')
    ax.set_title(r'$Test Title$')
    ax.legend(loc="upper left")
    canvas = FigureCanvasTkAgg(fig,master=win)
    canvas.draw()
    canvas.get_tk_widget().grid(row=8, column=0, padx=5, pady=5)
    canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5)

def scatter(df,array,win):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig, ax = plt.subplots(figsize=(array[2] * cm, array[3] * cm), tight_layout=True)
    fig.set_dpi(array[4])
    ax.scatter(x, y, label=r'$Test Label$',color='red')
    ax.set_xlabel(r'$' + array[0] + '$')
    ax.set_ylabel(r'$' + array[1] + '$')
    ax.set_title(r'$Test Title$')
    ax.legend(loc="upper left")
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().grid(row=8, column=0, padx=5, pady=5)
    canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5)

def hist(df,array,win):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig, ax = plt.subplots(figsize=(array[2] * cm, array[3] * cm), tight_layout=True)
    fig.set_dpi(array[4])
    ax.set_xlabel(r'$' + array[0] + '$')
    ax.set_ylabel(r'$' + array[1] + '$')
    ax.hist(y,label=r'$Test Label$',bins = 'auto',color='red',alpha=0.7, rwidth=0.85)
    ax.set_title(r'$Test Title$')
    ax.legend(loc="upper left")
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().grid(row=8, column=0, padx=5, pady=5)
    canvas.get_tk_widget().grid(row=9, column=0, padx=5, pady=5)


