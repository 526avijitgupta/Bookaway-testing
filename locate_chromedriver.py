#!/usr/bin/python
# Filename: local_settings.py

import os
print "Locating chromedriver on your machine.."
chromedriver = os.popen("find / -name 'chromedriver' -not -name '*.*' 2>/dev/null").read()
chromedriver = str(chromedriver.split("\n")[0])
if(chromedriver):
	print ("chromedriver found! Executing Script..")
else:
	print ("Unable to find chromedriver!")
# End of local_settings.py
