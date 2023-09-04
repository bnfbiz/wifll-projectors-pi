#!/usr/bin/env python3

from omxplayer import OMXPlayer 
import os
import pygame
import time
import random

class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print("I'm running under X display = {0}".format(disp_no))
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print('Driver: {0} failed.'.format(driver))
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print("Framebuffer size: %d x %d" % (size[0], size[1]))
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
scope = pyscope()

screenX = pygame.display.Info().current_w
screenY = pygame.display.Info().current_h
screensize = (screenX, screenY)

image1 = pygame.image.load('FLLLogo5.png').convert()
image1 = pygame.transform.scale(image1, screensize)
scope.screen.blit(image1,(0,0))
pygame.display.update()


stream1 = 'rtsp://admin:wifll@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0'
stream2 = 'rtsp://admin:wifll@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0'
stream3 = 'rtsp://admin:wifll@192.168.123.37:554/cam/realmonitor?channel=1&subtype=0'
stream4 = 'rtsp://admin:wifll@192.168.123.38:554/cam/realmonitor?channel=1&subtype=0'


screenRatio = (float(screenX) / screenY)

if (screenRatio > 1.7):
    cropPercent = 76
elif (screenRatio < 1.4):
    cropPercent = 100
else:
    cropPercent = 85

camX = 1920
camY = 1080

crop1x1 = 0
crop1y1 = (camY-1) - int((camY-1) * (cropPercent/100.0))
crop1x2 = camX-1
crop1y2 = camY-1

crop2x1 = 0
crop2y1 = crop1y1
crop2x2 = 1919
crop2y2 = 1079

win1x1 = 0
win1y1 = 0
win1y2 = int((screenY-1) / 2.0)
win1x2 = int(float(win1y2) / (crop1y2-crop1y1) * (camX-1))

win2x1 = 0
win2y1 = win1y2 + 1
win2x2 = win1x2
win2y2 = screenY-1

print(win1x1,win1y1,win1x2,win1y2)
print(win2x1,win2y1,win2x2,win2y2)

# 1600x1200

player1 = OMXPlayer(stream1)
player1.set_video_crop(crop1x1, crop1y1, crop1x2, crop1y2)
player1.set_video_pos(win1x1,win1y1,win1x2,win1y2)

player2 = OMXPlayer(stream2, dbus_name='org.mpris.MediaPlayer2.omxplayer1')
player2.set_video_pos(0,600,1067,1199)
player2.set_video_crop(crop2x1, crop2y1, crop2x2, crop2y2)
player2.set_video_pos(win2x1,win2y1,win2x2,win2y2)

# player3 = OMXPlayer(stream3, dbus_name='org.mpris.MediaPlayer2.omxplayer2')
# player3.set_video_pos(0,0,1067,599)
# 
# player4 = OMXPlayer(stream4, dbus_name='org.mpris.MediaPlayer2.omxplayer3')
# player4.set_video_pos(0,600,1067,1199)
# 
player1.play()
player2.play()

repeat = True

while repeat:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                repeat = False

player1.quit()
player2.quit()

