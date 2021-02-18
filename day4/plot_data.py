import numpy as np
import matplotlib.pyplot as plt
import os 
import fnmatch
import csv
import random


def main():
    os.chdir("./day4")
    csvFile = open("20201216cube10_4.csv", "r")
    compression_data = []
    reader = csv.reader(csvFile)
    for row in reader:
        try:
            compression_data.append([float(x) for x in row])
        except:
            None
    data_group = "cube10_"
    compression_data = np.array(compression_data)
    disp_matrix = []
    force_matrix = []
    
    for ii in range(4):
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        disp_matrix.append(compression_data[:,ii*3+2])
        force_matrix.append(compression_data[:,ii*3+1])
        plt.plot(compression_data[:,ii*3+2],compression_data[:,ii*3+1],c=color,label=data_group+str(ii))
        plt.xlabel('Compression Displacement in mm')
        plt.ylabel('Compression Force in N')
        plt.legend()
        plt.xlim(left=0)
        plt.ylim(bottom=0)

    stiffness = []
    for ii in range(4):
        ini_flag = 0
        end_flag = 0
        for jj in range(force_matrix[ii].size):
            if force_matrix[ii][jj] >= 500 and ini_flag == 0:
                ini_flag = 1
                force_ini = force_matrix[ii][jj]
                disp_ini = disp_matrix[ii][jj]
            if force_matrix[ii][jj] >= 3500 and end_flag == 0:
                end_flag = 1
                force_end = force_matrix[ii][jj]
                disp_end = disp_matrix[ii][jj]
            if ini_flag == 1 and end_flag == 1:
                stiffness.append((force_end-force_ini)/(disp_end-disp_ini))
                break

    csvFile.close()
    plt.show()
    a = 1


if __name__ == "__main__":  
    main()