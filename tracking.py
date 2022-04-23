import os
import cv2
import numpy as np

class Tracking():
    
    '''
    # Parameters
    videoLocation: Location of the video, also where the table will be saved.
    tableName: The name of the table file. Example: name.txt
    videoName: The name of the video that will be tracked.
    rColor: The RED interger number of RGB sistem.
    gColor: The GREEN interger number of RGB sistem.
    bColor: The BLUE interger number of RGB sistem.
    evolution: Max mumber of rows in the table data. Default = 10000
    width: Width of the video screen. Default = 1920
    height: Height of the video screen. Default =1080
    factor: Video screen grid division. Default = 10
    coverPortion: Cover portion in each grid that is cover with the chosen color. Default = 0.5
    step: Frame step. Default = 1
    
    '''

    def __init__(self, videoLocation, videoName, trackTableName, rColor, gColor, bColor,evolution = 10000, width=1920, height=1080, factor=10, coverPortion=0.5, step = 1):
        self.trackTableName = trackTableName
        self.fileDataName = open(trackTableName,'w+')
        self.cap=cv2.VideoCapture(videoName)
        self.evolution = evolution
        self.width=width
        self.height=height
        self.verticalPosition=np.zeros((evolution))
        self.horizontalPosition=np.zeros((evolution))
        self.videoLocation = os.chdir(videoLocation)
        self.factor = factor
        self.step = step
        self.rColor = int(rColor)
        self.gColor = int(gColor)
        self.bColor = int(bColor)
        self.coverPortion = coverPortion
        self.videoTracking()
        self.cap.release()
        cv2.destroyAllWindows()

    def videoTracking(self):

        print("Start!")

        i=0; j=0; k=0;

        while ((self.cap.isOpened()) and (k < self.evolution)):
            time_step=i
            self.cap.set(1, (time_step))
            ret,frame=self.cap.read()
            
            if ret == False:
                break

            z=1
            k=k+1

            greater_horizontal=0; greater_vertical=0

            for l in range(int(0*self.height/6), int(6*self.height/6), self.factor):
                for ll in range(int(0*self.width/10), int(10*self.width/10), self.factor):
                    amount=0
                    for lll in range(0, self.factor):
                        for llll in range(0, self.factor):
                            if ((frame[lll+l,llll+ll,2] > self.rColor) and (frame[lll+l,llll+ll,1] < self.gColor) and (frame[lll+l,llll+ll,0] < self.bColor)):
                                amount=amount+1
                    if (amount > (self.factor*self.factor*self.coverPortion)):
                        self.verticalPosition[z-1]=l+(self.factor/2)
                        self.horizontalPosition[z-1]=ll+(self.factor/2)
                        if (self.horizontalPosition[z-1] > greater_horizontal):
                            greater_horizontal=self.horizontalPosition[z-1]
                            greater_vertical=self.verticalPosition[z-1]
                        z=z+1

            self.fileDataName.write('%d %d %d\n' %(time_step, greater_vertical, greater_horizontal))
            i+=self.step
        
        print(self.trackTableName, 'is done!')

