from tkinter import *
import os

longitude = 0
latitude = 0


def quitprogram():
    exit()
def getpos():
    longitude = float(longitudeentry.get())
    latitude = float(latitudeentry.get())
    return longitude, latitude



while longitude == latitude:
    setup = Tk()
    intro = Label(setup, text = "Welcome to Mirror OS, a program built to run on a mirror device.")
    intro.pack(side = TOP, pady = 10)
    websitelabel = Label(setup, text = "You can find your Longitude and Latitude here: http://en.mygeoposition.com/ Enter your city in the search bar.")
    websitelabel.pack(side = TOP, pady = 10)
    longitudelabel = Label(setup, text = "Please enter the Longitude of your current location:")
    longitudelabel.pack(side = TOP, pady = 5)
    longitudeentry = Entry(setup)
    longitudeentry.pack()
    latitudelabel = Label(setup, text = "Please enter the Latitude of your current location:", pady = 5)
    latitudelabel.pack()
    latitudeentry = Entry(setup)
    latitudeentry.pack()
    run = Button(setup, text = "Go", command = getpos)
    run.pack()
    exitsetup = Button(setup, text  = "Exit", command = quitprogram)
    exitsetup.pack(side = BOTTOM, pady = 10)
    setup.geometry('600x360')
    setup.mainloop()


print(latitude)
print(longitude)
os.system("%LOCALAPPDATA%\Programs\Python\Python35-32\Scripts\pip.exe install requests")