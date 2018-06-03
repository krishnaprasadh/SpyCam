# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application

# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Type Your subject'
msg['From'] = 'from@gmail.com'
msg['To'] = 'to@gmail.com'

# The main body is just another attachment
body = email.mime.Text.MIMEText("""Type your message here""")
msg.attach(body)

# PDF attachment
filename='/path/to/image.jpg'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="jpg")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login('from@gmail.com','from email password here')
s.sendmail('from@gmail.com',['to@gmail.com'], msg.as_string())
s.quit()
