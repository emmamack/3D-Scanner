import math
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# data = []
# cartesian_coords = []

#while lineOfData != "":
    #lineOfData = serialPort.readline().decode(encoding = "ascii")
    # print(lineOfData)
    #
    # if len(lineOfData) > 0:
        # a, b, c = (int(x) for x in lineOfData.split(','))
        # distance = (16366/(a + 46.5)) - 9.09
        #

#distance, h_angle, v_angle
data = [512,21,80,
511,22,80,
515,23,80,
516,24,80,
513,25,80,
511,26,80,
512,27,80,
601,28,80,
503,29,80,
506,30,80,
504,31,80,
505,32,80,
509,33,80,
508,34,80,
502,35,80,
502,36,80,
598,37,80,
512,38,80,
514,39,80,
509,40,80,
541,41,80,
532,42,80,
505,43,80,
505,44,80,
513,45,80,
612,46,80,
512,47,80,
516,48,80,
515,49,80,
516,50,80,
523,51,80,
548,52,80,
516,53,80,
515,54,80,
628,55,80,
523,56,80,
522,57,80,
515,58,80,
515,59,80,
516,60,80,
517,61,80,
520,62,80,
547,63,80,
620,64,80,
516,65,80,
519,66,80,
518,67,80,
520,68,80,
518,69,80,
519,70,80,
516,71,80,
517,72,80,
615,73,80,
542,74,80,
509,75,80,
512,76,80,
512,77,80,
512,78,80,
512,79,80,
512,80,80,
505,81,80,
607,82,80,
514,83,80,
515,84,80,
512,85,80,
524,86,80,
509,87,80,
509,88,80,
509,89,80,
508,90,80,
523,90,90,
522,89,90,
583,88,90,
514,87,90,
516,86,90,
547,85,90,
516,84,90,
609,83,90,
512,82,90,
512,81,90,
516,80,90,
516,79,90,
516,78,90,
519,77,90,
520,76,90,
520,75,90,
643,74,90,
515,73,90,
515,72,90,
515,71,90,
520,70,90,
518,69,90,
519,68,90,
516,67,90,
515,66,90,
617,65,90,
518,64,90,
522,63,90,
540,62,90,
512,61,90,
512,60,90,
512,59,90,
512,58,90,
508,57,90,
608,56,90,
509,55,90,
509,54,90,
512,53,90,
535,52,90,
530,51,90,
512,50,90,
512,49,90,
511,48,90,
607,47,90,
508,46,90,
510,45,90,
509,44,90,
510,43,90,
523,42,90,
527,41,90,
512,40,90,
512,39,90,
614,38,90,
508,37,90,
508,36,90,
510,35,90,
508,34,90,
509,33,90,
505,32,90,
506,31,90,
516,30,90,
650,29,90,
540,28,90,
519,27,90,
519,26,90,
519,25,90,
519,24,90,
518,23,90,
518,22,90,
519,21,90,
619,20,90,
522,19,90,
530,18,90,
543,17,90,
515,16,90,
516,15,90,
516,14,90,
515,13,90,
512,12,90,
612,11,90,
512,10,90,
519,9,90,
522,8,90,
548,7,90,
516,6,90,
516,5,90,
519,4,90,
519,3,90,
606,2,90,
511,1,90,
509,0,90]

def get_data_tuples():
    data_tuples = []
    index = 0
    while index <= (len(data)-3):
        #this line converts voltage to distance, and it works!
        distance = (16366/(data[index] + 46.5)) - 9.09
        theta = math.radians(data[index+1])
        phi = math.radians(data[index+1])
        data_tuple = (distance, theta, phi)
        data_tuples.append(data_tuple)
        index += 3
    return data_tuples

def spherical_to_cartesian(spherical_coords):
    cartesian_coords = []
    for spherical_coord in spherical_coords:
        rho = spherical_coord[0]
        theta = spherical_coord[1]
        phi = spherical_coord[2]
        x = round(rho * math.sin(phi) * math.cos(theta), 2)
        y = round(rho * math.sin(phi) * math.sin(theta), 2)
        z = round(rho * math.cos(theta), 2)
        cartesian_coords.append((x,y,z))
    return(cartesian_coords)



spherical_coords = get_data_tuples()
cartesian_coords = spherical_to_cartesian(spherical_coords)
print(cartesian_coords)
