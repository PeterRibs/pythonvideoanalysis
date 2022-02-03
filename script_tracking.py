import os
import cv2
import math
import numpy as np
import scipy.io.wavfile as wread
import matplotlib.pyplot as plt

os.getcwd()
os.chdir('file_location')

width=1920; height=1080; FPS=2
factor=10

Evolution=1000

position_vert=np.zeros((Evolution)); position_hort=np.zeros((Evolution))

f=open('file_name_data','w+')
cap=cv2.VideoCapture('video_name')
i=0; j=0; k=0;

while ((cap.isOpened()) and (k < Evolution)):
    tempo_step=i+0
    cap.set(1, (tempo_step))
    ret,frame=cap.read()
    
    if ret == False:
        break

    z=1
    k=k+1
    maior_horizontal=0; maior_vertical=0
    for l in range(int(0*height/6),int(6*height/6),factor):
        for ll in range(int(0*width/10),int(10*width/10),factor):
            Quant=0
            for lll in range(0,factor):
                for llll in range(0,factor):
                    if ((frame[lll+l,llll+ll,2] > 150) and (frame[lll+l,llll+ll,1] < 100) and (frame[lll+l,llll+ll,0] < 100)):
                        Quant=Quant+1
            if (Quant > (factor*factor*0.2)):
                position_vert[z-1]=l+(factor/2)
                position_hort[z-1]=ll+(factor/2)
                if (position_hort[z-1] > maior_horizontal):
                    maior_horizontal=position_hort[z-1]
                    maior_vertical=position_vert[z-1]
                z=z+1

    f.write('%d %d %d\n' %(tempo_step,maior_vertical,maior_horizontal))
    print(k)
    i+=2

cap.release()
cv2.destroyAllWindows()
