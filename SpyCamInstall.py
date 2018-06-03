import cv2.cv as cv
import uuid
import os

def main():
	print"  ####  #####  #   #  ####    ##   #    # "
	print" #      #    #  # #  #    #  #  #  ##  ## "
	print"  ####  #    #   #   #      #    # # ## # "
	print"      # #####    #   #      ###### #    # "
	print" #    # #        #   #    # #    # #    #	"
	print"  ####  #        #    ####  #    # #    # \n"
	print" Version 1.0 - Krishnaprasadh.R  \n"	
	print " Welcome To SpyCam - Run As ADMIN For Installation\n"
	print " 1. TEST SPYCAM\n"
	print " 2. INSTALL SPYCAM\n"
	print " 3. INSTRUCTIONS\n"
	print " 4. REMOVE SPYCAM\n"
	print " 0. EXIT\n"
	choice = raw_input(" Enter choice: ")
	if choice == "1":
		capture()
		print " \n Image Saved \n"
		main()
	elif choice == "2":
		print " Giving Execute Permission to SpyStart.sh"
		os.system(" chmod +x SpyStart.sh")
		print " Copying SpyStart.sh to /etc/init.d/SpyStart.sh Startup"
		os.system(" cp SpyStart.sh /etc/init.d/SpyStart.sh")
		#os.system("update-rc.d myscript defaults")
		print " INSTALLATION DONE!"
		main()
	elif choice == "3":
		print " \n SpyStart.sh will run at startup. Keep all SpyCam contents in same directory (Python and .sh files) and edit the SpyStart.sh to locate Capture.py \n"
		print " For example if you keep SpyCam folder at Desktop, give the location to the Desktop directory in SpyStart.sh \n"
		print " SpyStart.sh will be executed during startup in the background and the snapshot will be saved in the Desktop/SpyCam directory \n"
		main()
	elif choice == "4":
		print " Removing SpyCam... /etc/init.d/SpyStart.sh\n"
		os.system (" rm /etc/init.d/SpyStart.sh")
		print " SpyCam Removed\n"
		main()
	else:
		print " \n GoodBye! \n"
		exit()

def capture():
	capture = cv.CaptureFromCAM(0)
	filename = str(uuid.uuid4())
	while True:
    		img = cv.QueryFrame(capture)
    		cv.SaveImage(filename+".jpg", img)
    		break
	cv.DestroyAllWindows()

main()
