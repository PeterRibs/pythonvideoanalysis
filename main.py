from tracking import Tracking
from frequency import Frequency

path= "C:/example"
name_track_table = "exampleTrackTable.txt"
name_video = "exampleVideo.mp4"
name_frequency_table = "exampleFrequencyTable"


Tracking(path, name_video, name_track_table,  150, 100, 100, evolution = 1000, width=1920,height=1080, factor=10, coverPortion=0.2, step = 2)

frequency = Frequency(path, name_track_table, name_frequency_table, 15, 100, 90)

frequency.graphFrequency()