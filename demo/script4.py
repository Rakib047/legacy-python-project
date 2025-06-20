# script4.py (Python 2.x)

# Importing old versions of libraries
import Tkinter
import smtplib
import socket
import os

# Sample usage of imported modules
root = Tkinter.Tk()
root.title("Python 2.x Example")
root.mainloop()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print "SMTP Server started."

host = socket.gethostname()
print "Hostname: ", host

os.makedirs('new_folder')
print "Folder created."
