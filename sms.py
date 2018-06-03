import zerosms
import getpass

def zerosmssend():
	user_name = "Your Username (Number)" 		#Way2SMS
	user_password = "Your Password"
	msg = "Your Message"
	send_to = "Number To Send - Give Your Number (Username)"
	zerosms.sms(phno=user_name,passwd=user_password,message=msg,receivernum=send_to)
zerosmssend()
