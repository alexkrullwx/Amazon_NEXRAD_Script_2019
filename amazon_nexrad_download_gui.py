#########################################################
#Python program to download NEXRAD data
#From the Amazon Archive
#Created by: Alex Krull, NWS WFO Des Moines, IA
#Date Created: 20190424
#GUI Works with Python 2.7 on Windows 
#########################################################

import nexradaws
conn = nexradaws.NexradAwsInterface()
from datetime import datetime
import pytz
import Tkinter as tk
from Tkinter import *

def callback():
    radar_id = "%s" %(e10.get())
    start = datetime(int(e0.get()),int(e1.get()),int(e2.get()),int(e3.get()),int(e4.get()))
    end = datetime(int(e5.get()),int(e6.get()),int(e7.get()),int(e8.get()),int(e9.get()))
    print 'Begin Radar Data Query'
    scans = conn.get_avail_scans_in_range(start, end, radar_id)
    results = conn.download(scans, "%s" %(e11.get()))
    print 'Script Finished'

master = Tk()
Label(master, text="Amazon NEXRAD Download\n All Times Are UTC").grid(row=0, columnspan=2)
Label(master, text="Start Year (YYYY)").grid(row=1)
Label(master, text="Start Month (MM)").grid(row=2)
Label(master, text="Start Day (DD)").grid(row=3)
Label(master, text="Start Hour (HH)").grid(row=4)
Label(master, text="Start Minute (MM)").grid(row=5)

Label(master, text="End Year (YYYY)").grid(row=6)
Label(master, text="End Month (MM)").grid(row=7)
Label(master, text="End Day (DD)").grid(row=8)
Label(master, text="End Hour (HH)").grid(row=9)
Label(master, text="End Minute (MM)").grid(row=10)

Label(master, text="Radar ID, ALL CAPS, Include K").grid(row=11)
Label(master, text="Absolute File Path\n Directory Must Created\n Before Running").grid(row=12)

e0 = Entry(master) #Start Year
e1 = Entry(master) #Start Month
e2 = Entry(master) #Start Day
e3 = Entry(master) #Start Hour
e4 = Entry(master) #Start Minute
e5 = Entry(master) #End Year
e6 = Entry(master) #End Month
e7 = Entry(master) #End Day
e8 = Entry(master) #End Hour
e9 = Entry(master) #End Minute
e10 = Entry(master) #Radar ID
e11 = Entry(master) #File Directory Path




e0.grid(row=1, column=1, pady=5)
e1.grid(row=2, column=1, pady=5)
e2.grid(row=3, column=1, pady=5)
e3.grid(row=4, column=1, pady=5)
e4.grid(row=5, column=1, pady=5)
e5.grid(row=6, column=1, pady=5)
e6.grid(row=7, column=1, pady=5)
e7.grid(row=8, column=1, pady=5)
e8.grid(row=9, column=1, pady=5)
e9.grid(row=10, column=1, pady=5)
e10.grid(row=11, column=1, pady=5)
e11.grid(row=12, column=1, pady=5)

Button(master, text='Download', command=callback).grid(row=13, column=0, sticky=W, padx=75, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=13, column=1, sticky=W, padx=4, pady=4)


mainloop()
