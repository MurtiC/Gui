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

def sel():

    xscale = str(width.get())
    yscale = str(height.get())
    x = int(float(xscale))
    y = int(float(yscale))
    wh = [x,y]
    return wh
    #scalelabel.config(text = z)



def setxy():
    x = xclicked.get()
    y = yclicked.get()
    z = [x,y]
    return z

def setdpi():
    y = int(entry.get())
    return y

def open_win_diag():
   # Create a dialog box
   path=filedialog.askopenfilename(initialdir=os.getcwd())
   print(path)
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
        fig.set_dpi(value)

    #    fig.savefig(pp, format='pdf')

    #pp.close()
    plt.show()


data = open_win_diag()

win=tk.Tk()
win.title('Window')
win.geometry("800x800")
win.config(bg='red')

options = data.columns.tolist()

xclicked = tk.StringVar()
xclicked.set("X axis")
yclicked = tk.StringVar()
yclicked.set("Y axis")

dpiwert = tk.IntVar()
varx = IntVar()
vary = IntVar()






# Top Frame
top = Frame(win, width=200, height=200, bg='blue')
top.grid(row=1, column=0, padx=0, pady=0)

# XY Frame
xy = Frame(win, width=200, height=200, bg='green')
xy.grid(row=0, column=0, padx=0, pady=0)

# Buttom Frame
plot_bar = Frame(win, width=100, height=100,bg='yellow')
plot_bar.grid(row=4, column=0, padx=5, pady=5)




# Drop Down Menu
dropx = ttk.OptionMenu(xy, xclicked, options[0], *options)
dropx.grid(row = 0, column= 0,padx=50, pady=0)
dropy = ttk.OptionMenu(xy, yclicked, options[0], *options)
dropy.grid(row = 0, column= 1,padx=50, pady=0)




width = Scale(xy,from_= 1, to=30, orient=HORIZONTAL, variable= varx)
width.grid(row = 1,column= 0,padx=50, pady=10)
height = Scale(xy,from_= 1, to=30, orient=HORIZONTAL, variable= vary)
height.grid(row = 1,column= 1,padx=50, pady=10)

scalebtn = Button(top, text="Get Scale Value", command= sel)
scalebtn.grid(row = 0, column= 0,padx=50, pady=0)

scalelabel = Label(top)
scalelabel.grid(row = 0, column= 4,padx=50, pady=0)




#btn1 = Button(top, text="Normaler Plot", command=lambda: plot_name.set("chart"))
btn1 = ttk.Button(top, text="Normaler Plot", command=lambda: chart(data,setxy(),setdpi(),sel()))
btn1.grid(row = 1, column= 0,padx=5, pady=5)

#btn2 = Button(top, text="Scatter Plot", command=lambda: plot_name.set("scatter"))
btn2 = ttk.Button(top, text="Scatter Plot", command=lambda: scatter(data,setxy(),setdpi()))
btn2.grid(row = 2, column= 0,padx=5, pady=5)

#btn3 = Button(top, text="Hist Plot", command=lambda: plot_name.set("hist"))
btn3 = ttk.Button(top, text="Hist Plot", command=lambda: hist(data,setxy(),setdpi()))
btn3.grid(row = 3, column= 0,padx=5, pady=5)

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


generate = ttk.Button(plot_bar, text="Generate", command=lambda: output(setdpi()))
generate.grid(row = 6, column= 0,padx=5, pady=5)

change = ttk.Button(plot_bar, text="Change File", command=lambda: update())
change.grid(row = 6, column= 1,padx=5, pady=5)

exit = ttk.Button(plot_bar, text="Close Window", command= win.quit)
exit.grid(row = 6, column= 3,padx=5, pady=5)


#resetbtn= Button(plot_bar, text="Reset", command=lambda: reset())
#resetbtn.grid(row = 6, column= 1,padx=5, pady=5)

#Directory

















#btn1 = Button(plot_bar, text="Normaler Plot", command=lambda: simplechart(data, setxy()))
#btn1.grid(row = 3, column= 0,padx=5, pady=5)
#btn2 = Button(plot_bar, text="Scatter Plot", command=lambda: scatter(data, setxy()))
#btn2.grid(row = 4, column= 0,padx=5, pady=5)
#btn3 = Button(plot_bar, text="Hist Plot", command=lambda: hist(data, setxy()))
#btn3.grid(row = 5, column= 0,padx=5, pady=5)

################################

fig = plt.Figure(figsize=(6,4), dpi=50)
bar1 = FigureCanvasTkAgg(fig, win)
bar1.get_tk_widget().grid(row=8, column=0, ipadx=40, ipady=20)
canvas = FigureCanvasTkAgg(fig, master=win)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().grid(row=8, column=0, ipadx=40, ipady=20)
toolbarFrame = Frame(master=win)
toolbarFrame.grid(row=9,column=0)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

