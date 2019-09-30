import serial
import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#initialize serial ports
arduinoComPort = "/dev/ttyACM0"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

def checkForData():
    """Delays program until arduino starts sending data"""
    while True:
        lineOfData = serialPort.readline().decode(encoding = "ascii")
        if len(lineOfData.rstrip()) > 0:
            break

def recordData():
    """Rccesses the serial ports while arduino is sending data, and oranizes it
    into lists
    Returns: lists of distances, pan angles, tilt angles, and x, y and z coordinates"""

    rhos = []
    thetas = []
    phis = []

    xs = []
    ys = []
    zs = []

    while True:
        #turn coded data from serial port into a string
        lineOfData = serialPort.readline().decode(encoding = "ascii")
        lineOfData = lineOfData.rstrip()

        #end the loop and graph when arduino stops sending data
        if len(lineOfData) == 0:
            break

        #discard line of data if there is an error in communication timing and
        #a line comes through broken
        try:
            a, b, c = (int(x) for x in lineOfData.split(','))
        except:
            pass

        #map analog input data to distance
        rho = round(((16366/(a + 46.5)) - 9.09), 3)
        #flatten out any data that is sufficiently "far away"
        if rho > 50:
            rho = 50

        theta = round(b, 3)
        phi = round(c, 3)
        print(str(rho) + ", " + str(theta) + ", " + str(phi))

        #add angles and distance to data structure
        rhos.append(rho)
        thetas.append(theta)
        phis.append(phi)

        #convert spherical data to cartesian
        x = round(rho * math.sin(phi) * math.cos(theta), 2)
        y = round(rho * math.sin(phi) * math.sin(theta), 2)
        z = round(rho * math.cos(theta), 2)

        #add cartesian coordinates to data structure
        xs.append(x)
        ys.append(y)
        zs.append(z)

    return rhos, thetas, phis, xs, ys, zs

# currently unused function
def make_graph_3d(xs, ys, zs):
    """Make a 3D graph with cartesian coordinates"""
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(xs, ys, zs);
    fig.savefig('test3d.png')

def make_graph_colored(xs, ys, zs):
    """Makes a colormapped 2D graph"""
    fig = plt.figure()
    ax = plt.axes()
    ax.set_title("3D scan")
    plt.scatter(xs, ys, c=zs, cmap='bone');
    cbar = plt.colorbar()
    cbar.set_label('Closeness to sensor (cm)')
    fig.savefig('scan.png')

checkForData()
rhos, thetas, phis, xs, ys, zs = recordData()
# uncomment this line to get a 3D graph
# make_graph_3d(xs, ys, zs)
make_graph_colored(thetas, phis, rhos)
