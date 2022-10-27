import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ipywidgets import widgets, interactive
from charts import *
from tkinter import *
from tkinter import filedialog
import os


def count():
    x = len(plt.get_fignums())
    plotcount.config(text = x)

def setxy():

    x = xclicked.get()
    y = yclicked.get()
    xnum = float(xnumber.get())
    ynum = float(ynumber.get())
    dpi = int(entry.get())
    z = [x,y,xnum,ynum,dpi]
    return z

def open_win_diag():
   # Create a dialog box
   path=filedialog.askopenfilename(initialdir=os.getcwd())
   file = pd.read_csv(path, delimiter=';', header=0)
   return file

def update():
    win.destroy()
    os.system('python main.py')

def output(value):

    x = len(plt.get_fignums())
    #filename = "output"
    #pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.set_dpi(value[4])
    #    fig.savefig(pp, format='pdf')
    #pp.close()
    plt.show()

def selectplot():
    x = plotoption.get()
    return eval(x +"(data,setxy(),win)")


data = open_win_diag()

win=tk.Tk()
win.title('Window')
win.geometry("800x800")
win.config(bg='red')

options = data.columns.tolist()

xclicked = tk.StringVar()
yclicked = tk.StringVar()
yclicked.set("Y axis")
xclicked.set("X axis")

plotoption = tk.StringVar()

dpiwert = tk.IntVar()
varx = IntVar()
vary = IntVar()

plotnames = ['chart','scatter','hist']

# Top Frame
top = Frame(win, width=200, height=200, bg='white')
top.grid(row=1, column=0, padx=0, pady=0)

# XY Frame
xy = Frame(win, width=200, height=200, bg='white')
xy.grid(row=0, column=0, padx=0, pady=0)

# Buttom Frame
plot_bar = Frame(win, width=100, height=100,bg='white')
plot_bar.grid(row=4, column=0, padx=5, pady=5)



# Drop Down Menu
dropx = ttk.OptionMenu(xy, xclicked, options[0], *options)
dropx.grid(row = 0, column= 0,padx=50, pady=0)
dropy = ttk.OptionMenu(xy, yclicked, options[0], *options)
dropy.grid(row = 0, column= 1,padx=50, pady=0)
dropf = ttk.OptionMenu(top, plotoption,plotnames[0],*plotnames)
dropf.grid(row = 1, column= 1,padx=50, pady=0)

# Set Length of the xy axis
xnumber = ttk.Entry(xy)
xnumber.insert(END, '16')
xnumber.grid(row = 1,column= 0,padx=50, pady=10)
ynumber = ttk.Entry(xy)
ynumber.insert(END, '9')
ynumber.grid(row = 1,column= 1,padx=50, pady=10)


btn1 = ttk.Button(top, text="Choose Plot", command=lambda: selectplot())
btn1.grid(row = 1, column= 0,padx=5, pady=5)

# Display the number of plots, optional
button = ttk.Button(top, text= "Number of Plots",  command=lambda: count())
button.grid(row = 4, column= 0,padx=5, pady=5)

plotcount = ttk.Label(top)
plotcount.grid(row = 4, column= 1,padx=0, pady=5)


labeldpi = ttk.Label(top, text = "Set DPI (default = 200)")
labeldpi.grid(row = 5, column= 0,padx=0, pady=5)

entry = ttk.Entry(top)
entry.insert(END, '200')
entry.grid(row = 5, column= 1,padx=0, pady=5)

generate = ttk.Button(plot_bar, text="Generate", command=lambda: output(setxy()))
generate.grid(row = 6, column= 0,padx=5, pady=5)

change = ttk.Button(plot_bar, text="Refresh", command=lambda: update())
change.grid(row = 6, column= 1,padx=5, pady=5)

exit = ttk.Button(plot_bar, text="Close Window", command= win.quit)
exit.grid(row = 6, column= 3,padx=5, pady=5)


