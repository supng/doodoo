# doodoo, a little Python program to check split names from LiveSplit.Server
# 
# made by your friendly neighbour supongo_ (https://twitch.tv/supongo_)
# https://github.com/supng/doodoo

import socket
import time
from tkinter import *

#Setting configuration
serverAddress = "localhost"
serverPort = 16834
refreshTimeInSeconds = .1
skipIntro = False
enableDelta = True
textFont = "Segoe UI"
timerFont = "Calibri Bold"
textSize = 16
timerSize = 44
cBackground = "#463F3F"
cForeground = "#93a1a1"
cForegroundTimer = "#00CC36"

root = Tk()
#root.resizable(0, 0)
root.geometry("500x400")
root.pack_propagate(0)
root.configure(background=cBackground)
root.title("doodoo, a LiveSplit.Server Receiver")

#Initialize label name variables
labelCurrentTime = StringVar()
labelCurrentTime.set('-')
labelCurrentSplit = StringVar()
labelCurrentSplit.set('-')
labelCurrentDelta = StringVar()
labelCurrentDelta.set('-')
labelPreviousSplit = StringVar()
labelPreviousSplit.set('-')

#Create actual labels
l0 = Label(root, text = "", font=("", timerSize), bg=cBackground, fg=cForeground)
l0.pack()
l1 = Label(root, textvariable = labelCurrentTime, font=(timerFont, timerSize), bg=cBackground, fg=cForegroundTimer)
l1.pack()
l2 = Label(root, textvariable = labelCurrentSplit, font=(textFont, textSize), bg=cBackground, fg=cForeground)
l2.pack()
l4 = Label(root, textvariable = labelCurrentDelta, font=(textFont, textSize), bg=cBackground, fg=cForeground)
l4.pack()
l3 = Label(root, textvariable = labelPreviousSplit, font=(textFont, textSize), bg=cBackground, fg=cForeground)
l3.pack()

#Connecting to LiveSplit.Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((serverAddress, serverPort))

def startWorking():
	print ("LiveSplit.Server Receiver is running...\n\nClose the window or Control + C to close me!")
	labelCurrentTime.set('Loading...')
	labelCurrentSplit.set('Loading...')
	getData()
def isTimerRunning():
	s.send("getcurrenttimerphase\r\n".encode())
	status = s.recv(1024)
	if "NotRunning" in status.decode():
		return False
	else:
		return True
def getSplitIndex():
	s.send("getsplitindex\r\n".encode())
	return s.recv(1024)
def getCurrentTime():
	s.send("getcurrenttime\r\n".encode())
	return s.recv(1024).decode()[:-2]
def getCurrentSplitName():
	s.send("getcurrentsplitname\r\n".encode())
	return s.recv(1024).decode()
def getPrevSplitName():
	s.send("getprevioussplitname\r\n".encode())
	return s.recv(1024).decode()
def getDelta():
	s.send("getdelta\r\n".encode())
	return s.recv(1024).decode()[:-2]
def getData():
	while 1:
		if isTimerRunning():
			current_time = getCurrentTime()
			labelCurrentTime.set(current_time)

			current_name = getCurrentSplitName()
			labelCurrentSplit.set(current_name)
			if int(getSplitIndex()) > 0:
				previous_name = getPrevSplitName()
				labelPreviousSplit.set(previous_name)
				current_delta = getDelta()
				labelCurrentDelta.set(current_delta)
			else:
				labelPreviousSplit.set('-')
				labelCurrentDelta.set('-')
		else:
			labelCurrentTime.set('Stopped')
			labelCurrentSplit.set('')
			labelPreviousSplit.set('')
			labelCurrentDelta.set('')
		root.update()
		time.sleep(refreshTimeInSeconds)

startWorking()
input()