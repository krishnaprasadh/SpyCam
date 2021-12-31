import cv2
import uuid
import os
from tkinter import *
root= Tk()
root.title("SpyCam - Run As Admin")

def aboutprogram():
	aboutdialog=Tk()
	aboutdialog.title("AboutSpyCam")
	aboutlabel = Label(aboutdialog, text="SpyCam --- Krishnaprasadh.R\n SpyStart.sh will run at startup. Keep all SpyCam contents in same directory (Python and .sh files) and edit the SpyStart.sh to locate Capture.py \n For example if you keep SpyCam folder at Desktop, give the location to the Desktop directory in SpyStart.sh \n SpyStart.sh will be executed during startup in the background and the snapshot will be saved in the Desktop/SpyCam directory")
	aboutdialog.resizable(False, False)
	aboutlabel.pack()
	
def removespycam():
	print (" Removing SpyCam... /etc/init.d/SpyStart.sh\n")
	os.system (" rm /etc/init.d/SpyStart.sh")
	print (" SpyCam Removed\n")
	

def installspycam():
	print (" Giving Execute Permission to SpyStart.sh")
	os.system(" chmod +x SpyStart.sh")
	print (" Copying SpyStart.sh to /etc/init.d/SpyStart.sh Startup")
	os.system(" cp SpyStart.sh /etc/init.d/SpyStart.sh")
	#os.system("update-rc.d myscript defaults")
	print (" INSTALLATION DONE!")

def testspycam():
	capture = cv2.VideoCapture(0)
	filename = str(uuid.uuid4())
	while True:
    		ret, frame = capture.read()
    		cv2.imwrite(filename+".jpg", frame)
    		break
	cv2.destroyAllWindows()
	print (" \n Image Saved \n")


exitbutton=Button(root, text="Exit",command=root.quit)
exitbutton.pack(side="right")
aboutbutton=Button(root, text="About",command=aboutprogram)
aboutbutton.pack(side="right")
activitybutton=Button(root, text="Remove",command=removespycam)
activitybutton.pack(side="right")
activitybutton=Button(root, text="Install",command=installspycam)
activitybutton.pack(side="right")
genbutton=Button(root, text="Test",command=testspycam)
genbutton.pack(side="right")

root.resizable(False, False)
root.mainloop()
