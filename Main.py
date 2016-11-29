
#Name: Matthew Daxner
#Date: ____ (when submitted)
#Description:

#**********************************************************
#import statements
from tkinter import * #Imports the GUI module pre-installed with Python
import time #imports the time module
import requests #Imports the request module used to open websites
import json #Imports JSON module used to gather data from json files(Ie: Websites)
from math import fabs


#Setup Variables

#Clock
timeFormat = 12 #Change to 24 for 24 hour format

#Weather
apitoken = 'fd44145b7a9f5f5d47b997586dec55bb' #login that allows the program to get the weather online
weatherurl = 'https://api.forecast.io/forecast/' # Website that is being used to request the weather
degree = chr(176) #Degree sign for weather

# Oakville Longitude and Latitude
longitude = -79.6877
latitude = 43.458236



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
        # calls the tick function the first time.
        self.timeTick()

    def timeTick(self):
        # Function that keep the clock changing on the window
        if timeFormat == 12:
            time2 = time.strftime('%I:%M %p')  # Sets time as 12hr
        elif timeFormat == 24:
            time2 = time.strftime('%H:%M')  # Sets time as 24hr
        else:
            # Creates error window if something is wrong
            error = Tk()
            errorlabel = Label(Text="ERROR: check timeFormat variable")
            errorlabel.pack()
            error.mainloop()

        dayofweek2 = time.strftime('%A') # Sets day of week
        date2 = time.strftime('%b %d, %Y') # Sets date

        # Conditional statements that run every 200 miliseconds to test if the time is the same as it is on the screen
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
        self.time.after(200, self.timeTick)

    # Main window class


class Weather(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.temperature2 = ''
        self.summary2 = ''
        self.info = Label(self, text=self.summary2, font=('Helvetica', 32), fg='white', bg='black')
        self.info.pack(side = BOTTOM)
        self.temp = Label(self, text = self.temperature2 , font=('Helvetica', 28),fg='white', bg='black')
        self.temp.pack(side = BOTTOM, anchor = W)
        self.getweather()

    def getweather(self):
        self.url = weatherurl + apitoken +'/'+str(latitude).strip()+','+str(longitude).strip()
        self.weather = requests.get(self.url)
        self.weather = json.loads(self.weather.text)
        temperature1 = fabs(int((self.weather['currently']['temperature']-32)*0.5556))
        temperature1 = fabs(temperature1)
        summary1 = self.weather['currently']['summary']

        if temperature1 != self.temperature2:
            self.temperature2 = temperature1
            self.temp.config(text = str(self.temperature2)+ degree + "C")
        if self.summary2 != summary1:
            self.summary2 = summary1
            self.info.config(text = self.summary2)
        self.temp.after(200, self.getweather)


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


# Program Run Code
# Calls the class main window which is the window that all widgets will be placed on
if __name__ == '__main__':
    w = MainWindow()
    w.background.mainloop()

