#Name: Matthew Daxner
#Date: ____ (when submitted)
#Description:
#The setup file of the program. Used to take inputs from user for location. Also offers a reopen option from the same
#place as you left off.

#**********************************************************


# Imports required modules
from tkinter import *
from urllib import request
import json
import os

#Defines empty variables
longitude = 0
latitude = 0

#Functions and Classes

# Creates the main setup window and creates the setup definitions
class setup:


    def __init__(self): #Window function, creates text and buttons

        #Creates window
        self.setup = Tk()
        self.setup.wm_title("Setup")
        self.setup.iconbitmap('mirror.ico') #Sets Icon Image


        # Mirror.ico was created by Molly Cobb in Grade 10



        #First textbox
        intro = Label(self.setup, text = "Welcome to Mirror Operating System, an OS built to be displayed on a mirror.")
        intro.pack(side = TOP, pady = 10)

        #Second textbox
        websitelabel = Label(self.setup, text = "You can find your Longitude and Latitude here: http://en.mygeoposition.com/ Enter your city in the search bar.\n "
                                                "Or the second button will automatically find your location using your IP. Clicking the second button\n"
                                                "will give permissions to the application to access you IP address")
        websitelabel.pack(side = TOP, pady = 10)

        # Longitude label and entry b ox
        self.longitudelabel = Label(self.setup, text = "Please enter the Longitude of your current location(Must be a number):")
        self.longitudelabel.pack(side = TOP, pady = 5)
        self.longitudeentry = Entry(self.setup)
        self.longitudeentry.pack()

        # Latitude label and entry box
        self.latitudelabel = Label(self.setup, text="Please enter the Latitude of your current location(Must be a number):", pady=5)
        self.latitudelabel.pack()
        self.latitudeentry = Entry(self.setup)
        self.latitudeentry.pack()

        # Creates the manual button, for users who wish to manually enter longitude and latitude
        manual = Button(self.setup, text = "Go", command = self.getpos)
        manual.pack()

        # Creates automatic button for automatic use
        automaticrun = Button(self.setup,text="Do it for me",command = self.automatic)
        automaticrun.pack(pady = 10)

        #Creates exit button
        exitsetup = Button(self.setup, text="Exit", command = self.quitprogram)
        exitsetup.pack(side = BOTTOM, pady=10)

        #Sets window size
        self.setup.geometry('600x360')

        #Loops the window, so it is constantly refreshing
        self.setup.mainloop()

    #Closes window, runs after the longitude and latitude are entered.
    def closesetup(self):
        self.setup.destroy()
    #Closes the program
    def quitprogram(self):
        exit()


    def getpos(self):

        #Allows the variabels to be changed globally within just the function
        global longitude
        global latitude


        #If values can be converted to a number it runs the Try:
        try:
            # Reassigns the variables from the numbers entered in the box.
            longitude = float(self.longitudeentry.get())
            latitude = float(self.latitudeentry.get())
        #If a Value error is returned executes an error box
        except ValueError:
            #Creates error window
            self.error = Tk()
            self.error.wm_title("Error")

            #Displays Error Label
            L1= Label(self.error ,text= "You did not enter a number")
            L1.pack()
            #Closes window after being pressed.


            self.error.mainloop()

        #Closes window in preparation for main window
        self.closesetup()


    def automatic(self):

        #Allows the variables to be globally assigned from within the function
        global longitude
        global latitude

        #Sets the URL where location is automatically determined
        url = 'http://ip-api.com/json'

        #Pulls the information from online, converts it to bytes then to json data
        jsonurl = request.urlopen(url).read().decode('UTF-8')
        jsonurl = json.loads(jsonurl)

        #The required data is taken from the pulled data
        longitude = jsonurl["lon"]
        latitude = jsonurl['lat']

        #Closes the window after info is pulled and variables are reassigned
        self.closesetup()
    def closeerror(self):
        self.error.destroy()

#Class that asks the user if they would like to return to the same location.
class Reopen:
    def __init__(self):

        #Creates window, assigns name and icon
        self.reboot = Tk()
        self.reboot.wm_title("Reboot")
        self.reboot.iconbitmap("mirror.ico")

        #Text box creation
        self.Intro = Label(self.reboot,text="Would you like to Reopen from the same location?")
        self.Intro.pack()

        #Buttons creation
        self.yes = Button(self.reboot,text="Yes",command = self.reopen)
        self.no = Button(self.reboot,text="No",command = self.dontreopen)
        self.yes.pack()
        self.no.pack()

        #Window Loop
        self.reboot.mainloop()

    #If user chooses to reopen from where the left off this function is ran
    def reopen(self):

        #Globalizes Long and Lat variables, to be reassigned within the function
        global longitude
        global latitude

        #Opens the text file where the Long and Lat are saved
        location = open("Location.txt")

        #Reads and reassigns the textfile
        longitude = location.readline()
        latitude = location.readline()

        #Deletes the window, in  preparation for Main window
        self.closereopen()

        #Function that runs if the user chooses "No"
    def closereopen(self):
        self.reboot.destroy()
    def dontreopen(self):
        #Runs the main setup
        setup()
        self.closereopen()

        #Deletes the Location.txt file where data is stored
        os.remove('Location.txt')

        #Deletes the window, in preparation for Setup Window
        self.closereopen()


#Program Run Code

#Checks if Location.txt is a file, if so runs Reopen class
if os.path.isfile("Location.txt") == True:

    #Runs Reopen Class
    Reopen()

#Else the normal setup is ran
else:
    setup()
