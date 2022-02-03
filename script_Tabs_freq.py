import os
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tk
import matplotlib.cm as cmx
import matplotlib.colors as cl
from scipy import signal
from matplotlib import transforms
from matplotlib import rc
from matplotlib.ticker import MaxNLocator

os.getcwd()

os.chdir('files_location')

plt.rc('text', usetex = True)
plt.rc('font', **{'family' : "sans-serif"})
params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)

Data_Number = 59

for i in range (1,Data_Number ):
    string_vector=[a]
    
    a1=np.loadtxt(a[i])
    a1_N=len(a1)
    freq=15; win=60; overlap=40
    
    Data_Number=1
    
    for ii in range(0,Data_Number):
        a_vert=np.zeros((a1_N))
        a_hort=np.zeros((a1_N))
        a_vert[:]=a1[:,1]
        a_hort[:]=a1[:,2]
        a_N=a1_N
    
    amax=max(a_vert)
    amin=min(a_vert)
    a_vert=((a_vert-amin)/(amax-amin))
    amax=max(a_hort)
    amin=min(a_hort)
    a_hort=((a_hort-amin)/(amax-amin))

    f1, t1, S1 = signal.spectrogram(a_vert, fs=freq, window=signal.get_window('hann',win), noverlap=overlap)

    f_size,t_size = S1.shape

    f_vector=np.zeros((t_size))

    f=open('Frequence_'+a[i]+'.dat','w+')
    
    for k in range(0,t_size):
        larger=0.0
        for j in range(0,f_size):
            if (S1[j,k] > larger):
                larger=S1[j,k]
                larger_f=f1[j]
        f.write('%f %f %f\n' %(t1[k],larger_f,larger))
    print (a[i])
