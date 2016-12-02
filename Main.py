
#Name: Matthew Daxner
#Date: ____ (when submitted)
#Description:

#**********************************************************
#import statements
from tkinter import * # Imports the GUI module pre-installed with Python
import time # imports the time module
import requests # Imports the request module used to open websites
import json # Imports JSON module used to gather data from json files(Ie: Websites)
from math import fabs
from Setup import longitude, latitude, setup


#Setup Variables

#Clock
timeFormat = 12 #Change to 24 for 24 hour format

#Weather
apitoken = 'fd44145b7a9f5f5d47b997586dec55bb' #login that allows the program to get the weather online
weatherurl = 'https://api.forecast.io/forecast/' # Website that is being used to request the weather
degree = chr(176) #Degree sign for weather

#News
newsurl = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=8cda9e54745d41c0951e028554d8efdd'

# Oakville Longitude and Latitude
longitude = longitude
latitude = latitude



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

    # Main window class


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
       # Creates the URL
        self.url = weatherurl + apitoken +'/'+str(latitude).strip()+','+str(longitude).strip()

        # Pulls temperature from the site
        self.weather = requests.get(self.url)
        self.weather = json.loads(self.weather.text)

        # Converts temperature from F -> C
        temperature1 = fabs(int((self.weather['currently']['temperature']-32)*0.5556))
        temperature1 = fabs(temperature1)

        # Pulls summary from online
        summary1 = self.weather['currently']['summary']

        # Updates the weather every 1/5 of a second
        if temperature1 != self.temperature2:
            self.temperature2 = temperature1
            self.temp.config(text = str(self.temperature2)+ degree + "C") # Adds degree symbol
        if self.summary2 != summary1:
            self.summary2 = summary1
            self.info.config(text = self.summary2)
        self.temp.after(200, self.getweather)


class News(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')

        self.headlineone = ''
        self.headlinetwo = ''
        self.headlinethree = ''
        self.headlinefour = ''
        self.headlinefive = ''

        title = Label(self, text = 'News', font =('Helvetica', 28), fg = 'White', bg = 'Black')
        title.pack(side = TOP)
        H1 = Label(self, text = self.headlineone,font =('Helvetica', 20), fg = 'White', bg = 'Black')
        H2 = Label(self, text=self.headlinetwo, font=('Helvetica', 20), fg='White', bg='Black')
        H3 = Label(self, text=self.headlinethree, font=('Helvetica', 20), fg='White', bg='Black')
        H4 = Label(self, text=self.headlinefour, font=('Helvetica', 20), fg='White', bg='Black')
        H5 = Label(self, text=self.headlinefive, font=('Helvetica', 20), fg='White', bg='Black')
        H1.pack(side = BOTTOM)
        H1.pack(side=BOTTOM)
        H1.pack(side=BOTTOM)
        H1.pack(side=BOTTOM)
        H1.pack(side=BOTTOM)
    def getnews(self):
        news = requests.get(newsurl)
        news = json.loads(news.text)
        headlines = [
            news['articles'][0]['title'],
            news['articles'][1]['title'],
            news['articles'][2]['title'],
            news['articles'][3]['title'],
            news['articles'][4]['title']
        ]
        if headlines[0] != self.headlineone:
            self.headlineone = headlines[0]
        elif headlines[1] != self.headlinetwo:
            self.headlinetwo = headlines[1]
        elif headlines[2] != self.headlinethree:
            self.headlinethree = headlines[2]
        elif headlines[3] != self.headlinefour:
            self.headlinefour = headlines[3]
        elif headlines[4] != self.headlinefive:
            self.headlinefive = headlines[4]




class MainWindow:  # Defines the class main window
    def __init__(self):  # Defines the init function which starts the whole program
        # Creates window
        self.background = Tk()

        # Config
        self.background.geometry("1920x1080")  # Sets the window size as 1920*1080
        self.background.configure(bg="Black")  # Sets the window background as Black for aesthetic purposes
        self.background.title('Smart Mirror OS')
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


# Program Run Code
# Calls the class main window which is the window that all widgets will be placed on
setup()
if __name__ == '__main__':
    w = MainWindow()
    w.background.mainloop()

