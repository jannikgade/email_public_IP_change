# This script sends a email notification to a user specific email address
# when the public IP address changes.
#  
# For instructions on how to start up the script on boot please visit
# http://raspberrywebserver.com/serveradmin/run-a-script-on-start-up.html
# 
# Author: Jannik Gade
# Date: 23-07-14

import smtplib
import urllib
import time

from_addr = 'from_email@gmail.com' 
to_addr  = 'to_email@gmail.com'
old_ip = "100.100.100.100" # Insert current IP address here

# Credentials
username = 'email_username'
password = 'email_password'

while(True):
	get_ip = urllib.urlopen('http://www.whatsmyip.us/showipsimple.php') # Retrieve IP address using whatsmyip.us
	new_ip = get_ip.read()[16:-3] # Strip unwanted text from IP

	if new_ip == old_ip:
		time.sleep(3600) # Sleep one hour
	else:
		msg = ("From: %s\r\nTo: %s\r\n\r\n" % (from_addr, to_addr)) + "The new IP address is: " + new_ip # Message text
		# The actual mail
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(from_addr, to_addr, msg)
		server.quit()
		time.sleep(3600) # Sleep one hour
