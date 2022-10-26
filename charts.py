import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn
import csv
from matplotlib.figure import Figure
from matplotlib import rc
from matplotlib.backends.backend_pdf import PdfPages

cm = 1/2.54

def chart(df, array,value,wh):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig, ax = plt.subplots(figsize=(wh[0] * cm, wh[1] * cm), tight_layout=True)
    fig.set_dpi(value)
    ax.plot(x, y, label=r'$Test Label$', color='red')
    ax.set_xlabel(r'$'+array[0]+'$')
    ax.set_ylabel(r'$'+array[1]+'$')
    ax.set_title("Test Title")
    ax.legend(loc="upper left")

def scatter(df,array,value,wh):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig, ax = plt.subplots(figsize=(wh[0] * cm, wh[1] * cm), tight_layout=True)
    fig.set_dpi(value)
    ax.scatter(x, y, label=r'$Test Label$',color='red')
    ax.set_xlabel(r'$' + array[0] + '$')
    ax.set_ylabel(r'$' + array[1] + '$')
    ax.set_title("Test Title")
    ax.legend(loc="upper left")


def hist(df,array,value,wh):
    rc('text', usetex=True)
    plt.rc('legend', frameon=False)
    x = df.loc[:, array[0]]
    y = df.loc[:, array[1]]
    fig = plt.figure(figsize=(wh[0] * cm, wh[1] * cm))
    fig.set_dpi(value)
    plt.xlabel(array[0])
    plt.ylabel(array[1])
    plt.hist(y,bins = 'auto',color='red',alpha=0.7, rwidth=0.85)

