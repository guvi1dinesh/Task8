#(4Q) Convert the UML diagram into a python class and its methods:


##  TV class:

# TVClass - Base class
# LedTV class
# PlasmaTV class

# Part - A
#
#(1) Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.

#(2) Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.

#(3) Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.

#(4) Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).

#(5) It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".

# Part - B : LED , Plasma **
#
#(1) Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV





#                                         PartA(1 to 5):


class TV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"



                           #*

class LEDTV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"


                           #*

class PlasmaTV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"





#                                 PartB(1)LED,Plasma


#LEDTV:

class LEDTV:
    def __init(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.refreshrate = refreshrate

    def viewingangel(self,angel):
        if 180<= angel <= 90:
            self.angel =angel


    def backlight1(self,light):
        self.light = 'pink'


    def displayquality(self,rating):
        self.rating = 'UHD'

    def displaydetail1(self):
        return f"{self.screenthickness}{self.displayquality}"

    # def energyusage(self,currentinvolts):
    #     if 40 <=currentinvolts<=20:
    #       self.currentinvolts =currentinvolts

    def detailedfeatureofTV(self):
        return f"display{self.displaydetail1()},thickness {self.screenthickness},light{self.backlight1},angel{self.viewingangel()},currentconsuption{self.energyusage},durablitytime{self.lifespan},frequency{self.refreshrate}"




#PlasmaTV:


class PlasmaTV:
    def __init(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.refreshrate = refreshrate

    def viewingangel(self,angel):
        if 180<= angel <= 90:
            self.angel =angel


    def backlight1(self,light):
        self.light = 'pink'


    def displayquality(self,rating):
        self.rating = 'UHD'

    def displaydetail1(self):
        return f"{self.screenthickness}{self.displayquality}"

    # def energyusage(self,currentinvolts):
    #     if 40 <=currentinvolts<=20:
    #       self.currentinvolts =currentinvolts

    def detailedfeatureofTV(self):
        return f"display{self.displaydetail1()},thickness {self.screenthickness},light{self.backlight1},angel{self.viewingangel()},currentconsuption{self.energyusage},durablitytime{self.lifespan},frequency{self.refreshrate}"
