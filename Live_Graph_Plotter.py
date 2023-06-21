# Live_Graph-Plotter, AYUSH VERMA

from tkinter import *
import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd

kalpana_root = Tk()
width = kalpana_root.winfo_screenwidth()
height = kalpana_root.winfo_screenheight()
kalpana_root.geometry("%dx%d" % (width, height))
f1 = Frame(kalpana_root, bg="orange")
f1.pack()

# Change the path of CSV file to check on your computer
data = pd.read_csv("D:\Kalpana\Sample Data - Software Task - Data Sheet 1.csv")
count = 0
timecount = 0
x = []
y = []


def build_temp():
    plt.figure(facecolor='orange')
    anima = animation.FuncAnimation(plt.gcf(), temp_graph, interval=1000)
    ax = plt.axes()
    ax.set_facecolor('yellow')
    plt.show()


def build_voltage():
    plt.figure(facecolor='orange')
    anima = animation.FuncAnimation(plt.gcf(), voltage_graph, interval=1000)
    ax = plt.axes()
    ax.set_facecolor('yellow')
    plt.show()


def build_altitude():
    plt.figure(facecolor='orange')
    anima = animation.FuncAnimation(plt.gcf(), altitude_graph, interval=1000)
    ax = plt.axes()
    ax.set_facecolor('yellow')
    plt.show()


def CLose():
    plt.close()
    statusvar.set("Ready")
    statusvar1.set("Current Data")
    global count
    # count = 0
    x.clear()
    y.clear()


def temp_graph(i):
    global count, timecount
    count += 1
    x.append(count)
    y.append(data['TEMP'][count])
    statusvar.set(y)
    statusvar1.set(data['TEMP'][count])
    currentime.set(data['MISSION_TIME'][count])
    plt.cla()
    plt.title("TEMPERATURE GRAPH", fontweight='bold')
    plt.xlabel("TIME (S)", fontweight='bold')
    plt.ylabel("TEMPERATURE", fontweight='bold')
    plt.scatter(x, y)
    plt.plot(x, y)


def voltage_graph(i):
    global count
    count += 1
    x.append(count)
    y.append(data['VOLTAGE'][count])
    statusvar.set(y)
    statusvar1.set(data['VOLTAGE'][count])
    currentime.set(data['MISSION_TIME'][count])
    plt.cla()
    plt.title("VOLTAGE GRAPH", fontweight='bold')
    plt.xlabel("TIME (S)", fontweight='bold')
    plt.ylabel("VOLTAGE", fontweight='bold')
    plt.scatter(x, y)
    plt.plot(x, y)


def altitude_graph(i):
    global count
    count += 1
    x.append(count)
    y.append(data['ALTITUDE'][count])
    statusvar.set(y)
    statusvar1.set(data['ALTITUDE'][count])
    currentime.set(data['MISSION_TIME'][count])
    plt.cla()
    plt.title("ALTITUDE GRAPH", fontweight='bold')
    plt.xlabel("TIME (S)", fontweight='bold')
    plt.ylabel("ALTITUDE", fontweight='bold')
    plt.scatter(x, y)
    plt.plot(x, y)


kalpana_root.title("Live Graph Plotter")
Team1_Kalpana = Label(f1, text='''Live Graph Plotter, Ayush Verma''',
                      font=("comicsansms", 30, "bold"), borderwidth=3, relief=SUNKEN
                      )
Team1_Kalpana.pack(pady=20, padx=20, fill=X)
b1 = Button(fg="green", bg="orange", text="Plot Temp Graph", font=("comicsansms", 20, "bold"), command=build_temp)
b1.pack(side=TOP, pady=20)

b2 = Button(fg="green", bg="orange", text="Plot Voltage Graph", font=("comicsansms", 20, "bold"), command=build_voltage)
b2.pack(side=TOP, pady=25)

b3 = Button(fg="green", bg="orange", text="Plot Altitude Graph", font=("comicsansms", 20, "bold"),
            command=build_altitude)
b3.pack(side=TOP, pady=30)

b4 = Button(fg="green", bg="orange", text="Quit Plotting", font=("comicsansms", 20, "bold"), command=CLose)
b4.pack(side=TOP, pady=35)

Team2_kalpana = Label(text='''Live Data fetched from CANSAT''', font=("comicsansms", 20, "bold"))
Team2_kalpana.pack(side=TOP, pady=10)

statusvar1 = StringVar()
statusvar1.set("Current Data")
sbar1 = Label(kalpana_root, textvariable=statusvar1, relief=SUNKEN, font=("comicsansms", 25, "bold"))
sbar1.pack(side=TOP, pady=10)

currentime = StringVar()
currentime.set("Time")
current = Label(kalpana_root, textvariable=currentime, relief=SUNKEN, font=("comicsansms", 25, "bold"))
current.pack(side=TOP, pady=10)

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(kalpana_root, textvariable=statusvar, relief=SUNKEN, anchor="e", font=("comicsansms", 25, "bold"))
sbar.pack(side=TOP, fill=X)

kalpana_root.mainloop()
