# script1.py (Python 2.x)

# Importing old versions of libraries
import urllib
import ConfigParser
import StringIO
import cookielib

# Sample usage of imported modules
url = 'http://example.com'
response = urllib.urlopen(url)
print "Response: ", response.read()

config = ConfigParser.ConfigParser()
config.read('config.cfg')
print "Config: ", config.sections()

cookie_jar = cookielib.LWPCookieJar()
cookie_jar.save('cookies.txt', ignore_discard=True)
