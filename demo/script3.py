# script3.py (Python 2.x)

# Importing old versions of libraries
import urllib2
import urlparse
import time
import Queue

# Sample usage of imported modules
url = 'http://example.com'
response = urllib2.urlopen(url)
print "Response: ", response.read()

parsed_url = urlparse.urlparse(url)
print "Parsed URL: ", parsed_url

time.sleep(1)
print "Slept for 1 second."

queue = Queue.Queue()
queue.put(1)
print "Queue size: ", queue.qsize()
