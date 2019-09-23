import serial
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

arduinoComPort = "/dev/ttyACM0"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

#don't start adding data to the structure until arduino is sending real data
def checkForData():
    while True:
        lineOfData = serialPort.readline().decode(encoding = "ascii")
        if len(lineOfData.rstrip()) > 0:
            break

def recordData():
    rhos = []
    thetas = []
    phis = []

    xs = []
    ys = []
    zs = []

    while True:
        lineOfData = serialPort.readline().decode(encoding = "ascii")
        lineOfData = lineOfData.rstrip()
        print(lineOfData)

        if len(lineOfData) == 0:
            break

        a, b, c = (int(x) for x in lineOfData.split(','))

        rho = round(((16366/(a + 46.5)) - 9.09), 3)
        theta = round(math.radians(b), 3)
        phi = round(math.radians(c), 3)
        print(str(rho) + ", " + str(theta) + ", " + str(phi))
        rhos.append(rho)
        thetas.append(theta)
        phis.append(phi)

        x = round(rho * math.sin(phi) * math.cos(theta), 2)
        y = round(rho * math.sin(phi) * math.sin(theta), 2)
        z = round(rho * math.cos(theta), 2)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return rhos, thetas, phis, xs, ys, zs

def make_graph_3d(xs, ys, zs):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, zs);
    fig.savefig('test3d.png')

def make_graph_2d(rhos, thetas, phis):
    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(thetas,phis);
    fig.savefig('test2d.png')

checkForData()
rhos, thetas, phis, xs, ys, zs = recordData()
# make_graph_2d(rhos, thetas, phis)
make_graph_3d(rhos, thetas, phis)
