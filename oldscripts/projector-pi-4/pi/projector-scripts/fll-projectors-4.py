#!/usr/bin/env python3

from omxplayer import OMXPlayer 
import os
import pygame
import time
import random
import requests
import socket

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



usernamepw = requests.auth.HTTPBasicAuth('admin', 'wifll999')
hostname = os.uname()[1]

if hostname == 'projector-pi-1':
    cam1IP = '192.168.123.31'
    cam2IP = '192.168.123.32'
    cam3IP = '192.168.123.33'
    cam4IP = '192.168.123.34'
    stream1 = 'rtsp://admin:wifll999@192.168.123.31:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.32:554/cam/realmonitor?channel=1&subtype=0'
    stream3 = 'rtsp://admin:wifll999@192.168.123.33:554/cam/realmonitor?channel=1&subtype=0'
    stream4 = 'rtsp://admin:wifll999@192.168.123.34:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-2':
    cam1IP = '192.168.123.33'
    cam2IP = '192.168.123.34'
    stream1 = 'rtsp://admin:wifll999@192.168.123.33:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.34:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-3':
    cam1IP = '192.168.123.31'
    cam2IP = '192.168.123.32'
    stream1 = 'rtsp://admin:wifll999@192.168.123.31:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.32:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-4':
    cam1IP = '192.168.123.33'
    cam2IP = '192.168.123.34'
    stream1 = 'rtsp://admin:wifll999@192.168.123.33:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.34:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-7':
    cam1IP = '192.168.123.35'
    cam2IP = '192.168.123.36'
    cam3IP = '192.168.123.37'
    cam4IP = '192.168.123.38'
    stream1 = 'rtsp://admin:wifll999@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0'
    stream3 = 'rtsp://admin:wifll999@192.168.123.37:554/cam/realmonitor?channel=1&subtype=0'
    stream4 = 'rtsp://admin:wifll999@192.168.123.38:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-8':
    cam1IP = '192.168.123.35'
    cam2IP = '192.168.123.36'
    stream1 = 'rtsp://admin:wifll999@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-9':
    cam1IP = '192.168.123.33'
    cam2IP = '192.168.123.34'
    cam3IP = '192.168.123.37'
    cam4IP = '192.168.123.38'
    stream1 = 'rtsp://admin:wifll999@192.168.123.33:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.34:554/cam/realmonitor?channel=1&subtype=0'
    stream3 = 'rtsp://admin:wifll999@192.168.123.37:554/cam/realmonitor?channel=1&subtype=0'
    stream4 = 'rtsp://admin:wifll999@192.168.123.38:554/cam/realmonitor?channel=1&subtype=0'
elif hostname == 'projector-pi-10':
    cam1IP = '192.168.123.31'
    cam2IP = '192.168.123.32'
    cam3IP = '192.168.123.35'
    cam4IP = '192.168.123.36'
    stream1 = 'rtsp://admin:wifll999@192.168.123.31:554/cam/realmonitor?channel=1&subtype=0'
    stream2 = 'rtsp://admin:wifll999@192.168.123.32:554/cam/realmonitor?channel=1&subtype=0'
    stream3 = 'rtsp://admin:wifll999@192.168.123.35:554/cam/realmonitor?channel=1&subtype=0'
    stream4 = 'rtsp://admin:wifll999@192.168.123.36:554/cam/realmonitor?channel=1&subtype=0'
else:
    sys.exit()


ptzIP = cam1IP

UDP_PORT_NO = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Make Socket Reusable
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Allow incoming broadcasts
serverSock.setblocking(False) # Set socket to non-blocking mode
serverSock.bind(('', UDP_PORT_NO))

# Create an instance of the PyScope class
scope = pyscope()

screenX = pygame.display.Info().current_w
screenY = pygame.display.Info().current_h
screensize = (screenX, screenY)


# calculate the aspect ratio of the projector and determine how 
# much the video camera image should be vertically cropped

screenRatio = (float(screenX) / screenY)

if (screenRatio > 1.7):
    cropPercent = 76
elif (screenRatio < 1.4):
    cropPercent = 100
else:
    cropPercent = 85

# load the background image (FLL and sponsor logos
# need to modify this to load specific backgrounds based on aspect ratio
image1 = pygame.image.load('FLLLogo2022.png').convert()
image1 = pygame.transform.scale(image1, screensize)
scope.screen.blit(image1,(0,0))
pygame.display.update()

# Camera resolution
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

curView = 1

# serverSock.sendto(b'1', ('192.168.123.23',UDP_PORT_NO))
# serverSock.sendto(b'1', ('192.168.123.24',UDP_PORT_NO))
# serverSock.sendto(b'1', ('192.168.123.27',UDP_PORT_NO))
# serverSock.sendto(b'1', ('192.168.123.28',UDP_PORT_NO))
# serverSock.sendto(b'1', ('192.168.123.29',UDP_PORT_NO))
# serverSock.sendto(b'1', ('192.168.123.30',UDP_PORT_NO))

player1 = OMXPlayer(stream1, args=['--live'])
player1.set_video_crop(crop1x1, crop1y1, crop1x2, crop1y2)
player1.set_video_pos(win1x1,win1y1,win1x2,win1y2)

player2 = OMXPlayer(stream2, dbus_name='org.mpris.MediaPlayer2.omxplayer1', args=['--live'])
player2.set_video_crop(crop2x1, crop2y1, crop2x2, crop2y2)
player2.set_video_pos(win2x1,win2y1,win2x2,win2y2)

# player3 = OMXPlayer(stream3, dbus_name='org.mpris.MediaPlayer2.omxplayer2', args=['--live'])
# player3.set_video_pos(0,0,1067,599)
#
# player4 = OMXPlayer(stream4, dbus_name='org.mpris.MediaPlayer2.omxplayer3', args=['--live'])
# player4.set_video_pos(0,600,1067,1199)
#
player1.play()
player2.play()

repeat = True

while repeat:
    time.sleep(.1)
    newView = curView

    try:
        data, addr = serverSock.recvfrom(1024)
        if data:
            if (data == b'1'):
                newView = 1
            elif (data == b'2'):
                newView = 2
    except:
        pass

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                repeat = False
            elif event.key == pygame.K_SPACE:
                if (curView == 1):
                    newView = 2
                else:
                    newView = 1
            elif event.key == pygame.K_r:
                player1.quit()
                player2.quit()
                player1 = OMXPlayer(stream1, args=['--live'])
                player1.set_video_crop(crop1x1, crop1y1, crop1x2, crop1y2)
                player1.set_video_pos(win1x1,win1y1,win1x2,win1y2)
                player2 = OMXPlayer(stream2, dbus_name='org.mpris.MediaPlayer2.omxplayer1', args=['--live'])
                player2.set_video_pos(0,600,1067,1199)
                player2.set_video_crop(crop2x1, crop2y1, crop2x2, crop2y2)
                player2.set_video_pos(win2x1,win2y1,win2x2,win2y2)
            elif event.key == pygame.K_h:
                os.system('/sbin/shutdown -h now')
            # PTZ key commands
            elif event.key == pygame.K_1:
                ptzIP = cam1IP
            elif event.key == pygame.K_2:
                ptzIP = cam2IP
            elif event.key == pygame.K_UP:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=Up&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=Up&arg1=0&arg2=1&arg3=0', auth=usernamepw)
            elif event.key == pygame.K_DOWN:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=Down&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=Down&arg1=0&arg2=1&arg3=0', auth=usernamepw)
            elif event.key == pygame.K_LEFT:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=Left&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=Left&arg1=0&arg2=1&arg3=0', auth=usernamepw)
            elif event.key == pygame.K_RIGHT:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=Right&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=Right&arg1=0&arg2=1&arg3=0', auth=usernamepw)
            elif event.key == pygame.K_KP_PLUS:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=ZoomTele&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=ZoomTele&arg1=0&arg2=1&arg3=0', auth=usernamepw)
            elif event.key == pygame.K_KP_MINUS:
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=start&channel=0&code=ZoomWide&arg1=0&arg2=1&arg3=0', auth=usernamepw)
                time.sleep(0.05)
                requests.get('http://'+ptzIP+'/cgi-bin/ptz.cgi?action=stop&channel=0&code=ZoomWide&arg1=0&arg2=1&arg3=0', auth=usernamepw)

    if (newView != curView):
        curView = newView
        player1.quit()
        player2.quit()
        time.sleep(1.5)
        if (newView == 1):
            # serverSock.sendto(b'1', ('192.168.123.23',UDP_PORT_NO))
            # serverSock.sendto(b'1', ('192.168.123.24',UDP_PORT_NO))
            # serverSock.sendto(b'1', ('192.168.123.27',UDP_PORT_NO))
            # serverSock.sendto(b'1', ('192.168.123.28',UDP_PORT_NO))
            # serverSock.sendto(b'1', ('192.168.123.29',UDP_PORT_NO))
            # serverSock.sendto(b'1', ('192.168.123.30',UDP_PORT_NO))
            player1 = OMXPlayer(stream1, args=['--live'])
            player2 = OMXPlayer(stream2, dbus_name='org.mpris.MediaPlayer2.omxplayer1', args=['--live'])
        elif (newView == 2):
            # serverSock.sendto(b'2', ('192.168.123.23',UDP_PORT_NO))
            # serverSock.sendto(b'2', ('192.168.123.24',UDP_PORT_NO))
            # serverSock.sendto(b'2', ('192.168.123.27',UDP_PORT_NO))
            # serverSock.sendto(b'2', ('192.168.123.28',UDP_PORT_NO))
            # serverSock.sendto(b'2', ('192.168.123.29',UDP_PORT_NO))
            # serverSock.sendto(b'2', ('192.168.123.30',UDP_PORT_NO))
            player1 = OMXPlayer(stream3, args=['--live'])
            player2 = OMXPlayer(stream4, dbus_name='org.mpris.MediaPlayer2.omxplayer1', args=['--live'])

        player1.set_video_crop(crop1x1, crop1y1, crop1x2, crop1y2)
        player1.set_video_pos(win1x1,win1y1,win1x2,win1y2)
        player1.play()


        player2.set_video_crop(crop2x1, crop2y1, crop2x2, crop2y2)
        player2.set_video_pos(win2x1,win2y1,win2x2,win2y2)
        player2.play()

# kill the video players before exiting the program
player1.quit()
player2.quit()


print("screen: ",screenX, screenY)
print("win1: ",win1x1,win1y1,win1x2,win1y2)
print("win2: ",win2x1,win2y1,win2x2,win2y2)

