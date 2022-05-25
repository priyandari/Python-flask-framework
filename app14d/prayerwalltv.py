#!/usr/bin/python
# -*- coding: utf-8 -*-

import pywapi
import pprint
import pygame
import string
import os
import time
import datetime
from praytimes import PrayTimes
# -*- coding: utf-8 -*-

installPath = "/home/pi/prayerwall/"

# convert mph = kpd / kphToMph
kphToMph = 1.60934400061

from umalqurra.hijri_date import HijriDate
#Get Prayer Times
#--------------------
lat = 9.327531
long = 8.086139

class pitft :
    screen = None;
    colourBlack = (0, 0, 0)

        def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer" http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        os.putenv('SDL_FBDEV', '/dev/fb0')

        # Select frame buffer driver Make sure that SDL_VIDEODRIVER is set
        driver = 'fbcon'
        if not os.getenv('SDL_VIDEODRIVER'):
            os.putenv('SDL_VIDEODRIVER', driver)
        try:
            pygame.display.init()
        except pygame.error:
            print 'Driver: {0} failed.'.format(driver)
            exit(0)

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()
    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

                
# Create an instance of the PyScope class
mytft = pitft() 
pygame.mouse.set_visible(False)
# set up the fonts choose the font
fontpath = pygame.font.match_font('arial')
# set up 2 sizes
font = pygame.font.Font(fontpath, 20)
fontSm = pygame.font.Font(fontpath, 18)
fontLg = pygame.font.Font(fontpath, 60)
fontCn = pygame.font.Font(fontpath, 100)
fontMd = pygame.font.Font(fontpath, 42)
#fontLg.set_bold(True)
colourWhite = (255, 255, 255) 
colourBlack = (0, 0, 0)
colourYellow = (255, 255, 0)
colourRed = (255, 0, 0)
colourBlue = (0, 0, 255)
colourGreen = (0, 255, 0)


# update interval
updateRate = 600 # seconds 


weatherDotComLocationCode = 'KUXX1118'
# -*- coding: utf-8 -*-

while True:
        weather_com_result = pywapi.get_weather_from_weather_com(weatherDotComLocationCode)
     
        today = weather_com_result['forecasts'][0]['day_of_week'][0:3] + " " \
                + weather_com_result['forecasts'][0]['date'][4:] + " " \
                + weather_com_result['forecasts'][0]['date'][:3]
        windSpeed = int(weather_com_result['current_conditions']['wind']['speed']) / kphToMph
        
        currWind = "{:.0f}mph ".format(windSpeed) + weather_com_result['current_conditions']['wind']['text']
        currTemp = weather_com_result['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
        currPress = weather_com_result['current_conditions']['barometer']['reading'][:-3] + "mb"
        uv = "UV {}".format(weather_com_result['current_conditions']['uv']['text'])
        humid = "Hum {}%".format(weather_com_result['current_conditions']['humidity'])
                
        # extract forecast data
        forecastDays = {}
        forecaseHighs = {}
        forecaseLows = {}
        forecastPrecips = {}
        forecastWinds = {}
            
        start = 0
        try:
                test = float(weather_com_result['forecasts'][0]['day']['wind']['speed'])
        except ValueError:
                start = 1
            
        for i in range(start, 5):
                
                if not(weather_com_result['forecasts'][i]):
                    break
                forecastDays[i] = weather_com_result['forecasts'][i]['day_of_week'][0:3]
                forecaseHighs[i] = weather_com_result['forecasts'][i]['high'] + u'\N{DEGREE SIGN}' + "C"
                forecaseLows[i] = weather_com_result['forecasts'][i]['low'] + u'\N{DEGREE SIGN}' + "C"
                forecastPrecips[i] = weather_com_result['forecasts'][i]['day']['chance_precip'] + "%"
                forecastWinds[i] = "{:.0f}".format(int(weather_com_result['forecasts'][i]['day']['wind']['speed'])  / kphToMph) + \
                        weather_com_result['forecasts'][i]['day']['wind']['text']       
                
        now = datetime.datetime.now()
        um = HijriDate(now.year,now.month,now.day,gr=True)

        Islamicdate=str(int(um.day))
        Islamicmonth=str(int(um.month))
        Islamicyear=str(int(um.year))

        PT = PrayTimes('Makkah')
        times = PT.getTimes((now.year,now.month,now.day), (lat, long), 3,0)
        try:
                currTemp = weather_com_result['current_conditions']['temperature'] + u'\N{DEGREE SIGN}' + "C"
        except KeyError:
                print("Maybe net down")
                        
        try:
                humid = "{}%".format(weather_com_result['current_conditions']['humidity'])
        except KeyError:
                print("Maybe net down")
                
        # blank the screen
        mytft.screen.fill(colourBlack)
                
        # Render the weather logo at 0,0
        icon = installPath+ (weather_com_result['current_conditions']['icon']) + ".png"
        logo = pygame.image.load(icon).convert()
        mytft.screen.blit(logo, (0, 0))
                
        # set the anchor for the current weather data text
        textAnchorX = 156
        textAnchorY = 5
        textYoffset = 64
                
        # add current weather data text artifacts to the screen
        text_surface = fontLg.render(today, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(currTemp, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(currWind, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(currPress, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(uv, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(humid, True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
           
        # set X axis text anchor for the forecast text
        textAnchorX = 10
        textXoffset = 150
                
        # add each days forecast text
        for i in forecastDays:
                textAnchorY = 450
                text_surface = fontMd.render(forecastDays[int(i)], True, colourWhite)
                mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
                textAnchorY+=textYoffset
                text_surface = fontMd.render(forecaseHighs[int(i)], True, colourWhite)
                mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
                textAnchorY+=textYoffset
                text_surface = fontMd.render(forecaseLows[int(i)], True, colourWhite)
                mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
                textAnchorY+=textYoffset
                text_surface = fontMd.render(forecastPrecips[int(i)], True, colourWhite)
                mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
                textAnchorY+=textYoffset
                text_surface = fontMd.render(forecastWinds[int(i)], True, colourWhite)
                mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
                textAnchorX+=textXoffset        
                
        # set the anchor for the current Islamic date text
        textAnchorX = 612
        textAnchorY = 5
        

        # add current Islamicdate text artifacts to the screen
        text_surface = fontLg.render(Islamicdate+"."+Islamicmonth+"."+Islamicyear+"H", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        # set the anchor for the current Prayer time text
        textAnchorX = 868
        textAnchorY = 128
        textYoffset = 128

        # add current Prayer data text artifacts to the screen
        text_surface = fontLg.render(times['fajr'], True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(times['dhuhr'], True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(times['asr'], True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(times['maghrib'], True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render(times['isha'], True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))

        # set the anchor for the current Prayer time text
        textAnchorX = 612
        textAnchorY = 128
        textYoffset = 128

        # add current Prayer data text artifacts to the screen
        text_surface = fontLg.render("Fajr", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render("Dhuhr", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render("Asr", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render("Maghrib", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))
        textAnchorY+=textYoffset
        text_surface = fontLg.render("Isha", True, colourWhite)
        mytft.screen.blit(text_surface, (textAnchorX, textAnchorY))


        pygame.display.update()
                
        # Wait
        time.sleep(updateRate)
        
