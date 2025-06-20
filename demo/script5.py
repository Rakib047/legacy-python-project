# script5.py (Python 2.x)

# Importing old versions of libraries
import base64
import thread
import random
import wx

# Sample usage of imported modules
encoded = base64.b64encode(b'Hello World')
print "Base64 Encoded: ", encoded

def print_message():
    print "Hello from thread!"

thread.start_new_thread(print_message, ())

random_choice = random.choice([1, 2, 3, 4])
print "Random choice: ", random_choice

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Python 2.x Example")
frame.Show(True)
app.MainLoop()
