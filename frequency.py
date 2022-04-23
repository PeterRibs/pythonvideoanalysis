import os
import math
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt
from scipy import signal

class Frequency():

    '''
    # Parameters
    tableLocation: Location of the data table, also where the table will be saved.
    initialTable: The name of the table file will be the dataset. Example: name.txt
    frequencyTableName: The name of the table file. Example: name.txt
    frequency: Sampling frequency of the x time series.
    window: Desired window to use. Number of frames that will be the base to find the frequency.
    overlap: Number of points (Frames) to overlap between segments.
    '''

    def __init__(self, tableLocation, initialTable, frequencyTableName, frequency, window, overlap):
        self.frequencyTableName = frequencyTableName
        self.frequencyTable = open(frequencyTableName+'.dat','w+')
        self.frequencyTableList = []
        self.tableLocation = os.chdir(tableLocation)
        self.initialTable = np.loadtxt(initialTable)
        self.frequency = frequency
        self.window = window
        self.overlap = overlap
        self.frequencyTableFunction()

    def frequencyTableFunction(self):

        initialTableLen = len(self.initialTable)
        freq = self.frequency
        win = self.window
        overlap=self.overlap
        verticalCol = np.zeros(initialTableLen)
        horizontalCol = np.zeros(initialTableLen)
        verticalCol[:] = self.initialTable[:,1]
        horizontalCol[:] = self.initialTable[:,2]
        
        verticalMax=max(verticalCol)
        verticalMin=min(verticalCol)
        verticalCol=((verticalCol-verticalMin)/(verticalMax-verticalMin))
        horizontalMax=max(horizontalCol)
        horizontalMin=min(horizontalCol)
        horizontalCol=((horizontalCol-horizontalMin)/(horizontalMax-horizontalMin))

        f1, t1, S1 = signal.spectrogram(verticalCol, fs=freq, window=signal.get_window('hann', win), noverlap=overlap)

        f_size, t_size = S1.shape
        
        for k in range(0, t_size):
            larger=0.0
            for j in range(0,f_size):
                if (S1[j,k] > larger):
                    larger=S1[j,k]
                    larger_f=f1[j]
            self.frequencyTableList.append([t1[k], larger_f, larger])
            self.frequencyTable.write('%f %f %f\n' %(t1[k], larger_f, larger))  

    def graphFrequency(self):
        
        df = pd.DataFrame(self.frequencyTableList)

        fig, ax = plt.subplots()
        ax.plot(df[0], df[1])

        ax.set(xlabel='time (s)', ylabel='freq (Hz)',
                title= "Frequency Plot")
        ax.grid()

        fig.savefig('Figure_'+self.frequencyTableName+'.png')
        
        fig.show()

