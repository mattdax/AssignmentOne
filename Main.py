"""
___  ____                       _____ _____
|  \/  (_)                     |  _  /  ___|
| .  . |_ _ __ _ __ ___  _ __  | | | \ `--.
| |\/| | | '__| '__/ _ \| '__| | | | |`--. \
| |  | | | |  | | | (_) | |    \ \_/ /\__/ /
\_|  |_/_|_|  |_|  \___/|_|     \___/\____/
                                            """

#Name: Matthew Daxner
#Date: ____ (when submitted)
#Description:
"""


Mirror OS is an Operating System built to run on a Rasberry Pi that has been built into a mirror. The program has multiple
features including:

Changing Location
Automatic Location Detection
Time & Date
News Headlines, updated on a regular basis
Weather updated from your location on a regular basis
Large black background for display on a mirror
Full setup window, for an easy to use system
"""


#**********************************************************
#import statements
from tkinter import * # Imports the GUI module pre-installed with Python
# Imports the time module
import time
#Imports the urllib used to pull data from online
from urllib import request
# Imports JSON module used to gather data from json files(Ie: Websites)
import json
#Math module to round numbers up.
from math import ceil
# Imports variables from the Setup file.
from Setup import longitude, latitude, setup

#Setup Variables

#Clock
timeFormat = 12 #Change to 24 for 24 hour format

#Weather
apitoken = 'a5e364ec1db05182ba56acc45dba9db0' #login that allows the program to get the weather online
weatherurl = 'https://api.forecast.io/forecast/' # Website that is being used to request the weather
degree = chr(176) #Degree sign for weather

#News
newsurl = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=8cda9e54745d41c0951e028554d8efdd'


#Functions/Classes
class Clock(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        # Function that displays the time on the top right corner of the screen

        # Adds time
        self.time1 = ''
        self.time = Label(self, text = self.time1,font=("Helvetica",32), fg = 'white', bg = 'black') # Creates label
        self.time.pack(side=TOP) # Packs it onto screen

        # Adds Date
        self.date1 = ''
        self.date = Label(self,text=self.date1,font=("Helvetica",20), fg = 'white', bg = 'black')
        self.date.pack(side = TOP)

        # Adds Day of week
        self.dayofweek1 = ''
        self.dayofweek = Label(self, text = self.dayofweek1,font=("Helvetica",15), fg = 'white', bg = 'black')
        self.dayofweek.pack(side = TOP)

        # calls the Time tick function to start running.
        self.timeTick()

    def timeTick(self):
        # Function that check to make sure the time is the same as the time being displayed on the window

        if timeFormat == 12: #Defined at top of the file
            time2 = time.strftime('%I:%M %p')  # Sets time as 12hr
        elif timeFormat == 24:
            time2 = time.strftime('%H:%M')  # Sets time as 24hr
        else:
            # Creates error window if problems are encountered
            error = Tk()
            errorlabel = Label(Text="ERROR: check timeFormat variable")
            errorlabel.pack()
            error.mainloop()

        dayofweek2 = time.strftime('%A') # Sets day of the week format
        date2 = time.strftime('%b %d, %Y') # Sets date format []

        # Conditional statements that run every 200 milliseconds to test if the time is the same as it is on the screen
        # If the time is different it will automatically change the time.

        # Ignore the error in time2 program still works
        if time2 != self.time1:
            self.time1 = time2
            self.time.config(text = self.time1)
        if date2 != self.date1:
            self.date1 = date2
            self.date.config(text = self.date1)
        if dayofweek2 != self.dayofweek1:
            self.dayofweek1 = dayofweek2
            self.dayofweek.config(text = self.dayofweek1)
        self.time.after(200, self.timeTick) #After function is the same as time.sleep() but works with Tkinter



class Weather(Frame):
    #Frame Function
    def __init__(self, parent):

        #Creates the Frame
        Frame.__init__(self, parent, bg='black')

        #Creates the empty variables
        self.temperature2 = ''
        self.summary2 = ''

        #Adds and packs the Temperature and the Summary
        self.info = Label(self, text=self.summary2, font=('Helvetica', 32), fg='white', bg='black')
        self.info.pack(side = BOTTOM)
        self.temp = Label(self, text = self.temperature2 , font=('Helvetica', 28),fg='white', bg='black')
        self.temp.pack(side = BOTTOM, anchor = W)

        #Calls the function that gets the weather
        self.getweather()

    #Function that pulls the weather from online.
    def getweather(self):
       #Creates the URL, with Longitude and Latitude
        self.url = weatherurl + apitoken +'/'+str(latitude).strip()+','+str(longitude).strip()

        # Pulls temperature from the online, and converts it into readable text.
        self.weather = request.urlopen(self.url).read().decode('UTF-8')
        self.weather = json.loads(self.weather)

        # Converts temperature from F -> C
        temperature1 = ceil(int((self.weather['currently']['temperature']-32)*0.5556))
        temperature1 = ceil(temperature1)

        # Pulls summary from online
        summary1 = self.weather['currently']['summary']

        # Updates the weather every 20,000 milliseconds.
        if temperature1 != self.temperature2:
            self.temperature2 = temperature1
            self.temp.config(text = str(self.temperature2)+ degree + "C") # Adds degree symbol
        if self.summary2 != summary1:
            self.summary2 = summary1
            self.info.config(text = self.summary2)

        #Do not change 20000, any faster will cap the amount of times the computer can pull the data from online.
        self.temp.after(20000, self.getweather)

#Class that pulls all the news headlines from online.
class News(Frame):
    def __init__(self, parent):

        #Creates the fram where the news will go
        Frame.__init__(self, parent, bg='black')

        #Defines empty variables
        self.headlineone = ''
        self.headlinetwo = ''
        self.headlinethree = ''
        self.headlinefour = ''
        self.headlinefive = ''

        #Creates all the labels where the headlines will go, after being pulled
        title = Label(self, text = 'News', font =('Helvetica', 28), fg = 'White', bg = 'Black')
        title.pack(side = TOP)
        self.H1 = Label(self, text = self.headlineone,font =('Helvetica', 15), fg = 'White', bg = 'Black')
        self.H2 = Label(self, text=self.headlinetwo, font=('Helvetica', 15), fg='White', bg='Black')
        self.H3 = Label(self, text=self.headlinethree, font=('Helvetica', 15), fg='White', bg='Black')
        self.H4 = Label(self, text=self.headlinefour, font=('Helvetica', 15), fg='White', bg='Black')
        self.H5 = Label(self, text=self.headlinefive, font=('Helvetica', 15), fg='White', bg='Black')
        self.H1.pack(side=TOP)
        self.H2.pack(side=TOP)
        self.H3.pack(side=TOP)
        self.H4.pack(side=TOP)
        self.H5.pack(side=TOP)

        #Calls the getnews function which pulls the information from online
        self.getnews()

    #Function that pulls news from online
    def getnews(self):

        #Connects online and converts the information into bytes then to JSON data
        news = request.urlopen(newsurl).read().decode('UTF-8')
        news = json.loads(news)

        #Using a list the headlines are pulled from the JSON data
        headlines = [
            news['articles'][0]['title'],
            news['articles'][1]['title'],
            news['articles'][2]['title'],
            news['articles'][3]['title'],
            news['articles'][4]['title']
        ]

        #Checks if the headline are the same as the ones on the display. If not updates them to the new headline
        #Note: Must all use if's and cannot use elif's because the program must check every single one.
        if headlines[0] != self.headlineone:
            self.headlineone = headlines[0]
            self.H1.config(text=self.headlineone)
        if headlines[1] != self.headlinetwo:
            self.headlinetwo = headlines[1]
            self.H2.config(text=self.headlinetwo)
        if headlines[2] != self.headlinethree:
            self.headlinethree = headlines[2]
            self.H3.config(text=self.headlinethree)
        if headlines[3] != self.headlinefour:
            self.headlinefour = headlines[3]
            self.H4.config(text=self.headlinefour)
        if headlines[4] != self.headlinefive:
            self.headlinefive = headlines[4]
            self.H5.config(text=self.headlinefive)
        #Runs the function every 20000 milliseconds
        self.H1.after(20000, self.getnews)
        self.H2.after(20000, self.getnews)
        self.H3.after(20000, self.getnews)
        self.H4.after(20000, self.getnews)
        self.H5.after(20000, self.getnews)



class MainWindow:  # Defines the class main window
    def __init__(self):  # Defines the init function which starts the whole program

        # Creates window
        self.background = Tk()

        # Config
        self.background.geometry("1920x1080")  # Sets the window size as 1920*1080
        self.background.configure(bg="Black")  # Sets the window background as Black for aesthetic purposes
        self.background.title('Smart Mirror OS')# Window Title
        self.background.iconbitmap('mirror.ico')
        self.state = FALSE

        # Frames
        self.topFrame = Frame(self.background, bg="Black")
        self.botFrame = Frame(self.background, bg="Black")
        self.topFrame.pack(side=TOP, fill=BOTH)
        self.botFrame.pack(side=BOTTOM, fill=BOTH)

        # Clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)

        # Weather
        self.weather = Weather(self.botFrame)
        self.weather.pack(side=LEFT,anchor=N ,padx= 50,pady=60)

        # News
        self.news = News(self.botFrame)
        self.news.pack(side = RIGHT, anchor =N, padx = 20)


#Saves the longitude and latitude data  
class LongitudeLatiudeCollection:
    def __init__(self):
        #Creates the File
        Location = open("Location.txt", "w")

        #Writes the Information on two lines in the file
        Location.write(str(longitude)+"\n")
        Location.write(str(latitude))


# Latitude is default set to
if latitude == 0 and longitude == 0:
    setup()

# Program Run Code


#Calls the Longitude and Latitude class, which saves the Lon and Lat in a file
LongitudeLatiudeCollection()

# Calls the class main window which is the window that all widgets will be placed on
if __name__ == '__main__':
    w = MainWindow()
    w.background.mainloop()

