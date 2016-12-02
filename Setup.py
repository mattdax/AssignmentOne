from tkinter import *
import os
longitude = 0
latitude = 0
class setup:

    def __init__(self):
        self.setup = Tk()
        intro = Label(setup, text = "Welcome to Mirror OS, a program built to run on a mirror device.")
        intro.pack(side = TOP, pady = 10)
        websitelabel = Label(setup, text = "You can find your Longitude and Latitude here: http://en.mygeoposition.com/ Enter your city in the search bar.")
        websitelabel.pack(side = TOP, pady = 10)
        self.longitudelabel = Label(setup, text = "Please enter the Longitude of your current location:")
        self.longitudelabel.pack(side = TOP, pady = 5)
        self.longitudeentry = Entry(setup)
        self.longitudeentry.pack()
        self.latitudelabel = Label(setup, text = "Please enter the Latitude of your current location:", pady = 5)
        self.latitudelabel.pack()
        self.latitudeentry = Entry(setup)
        self.latitudeentry.pack()
        run = Button(setup, text = "Go", command = self.getpos)
        run.pack()
        exitsetup = Button(setup, text  = "Exit", command = self.quitprogram)
        exitsetup.pack(side = BOTTOM, pady = 10)
        self.setup.geometry('600x360')


    def quitprogram(self):
        exit()
    def getpos(self):
        global longitude
        global latitude
        longitude = float(self.longitudeentry.get())
        latitude = float(self.latitudeentry.get())
        os.system("%LOCALAPPDATA%\Programs\Python\Python35-32\Scripts\pip.exe install requests")
setup()




