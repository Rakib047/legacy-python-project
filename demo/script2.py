# script2.py (Python 2.x)

# Importing old versions of libraries
import itertools
import cPickle
import hashlib
import simplejson

# Sample usage of imported modules
data = {'key': 'value'}
pickled_data = cPickle.dumps(data)
print "Pickled Data: ", pickled_data

hash_object = hashlib.md5(b'Hello World')
print "Hash: ", hash_object.hexdigest()

json_data = simplejson.dumps(data)
print "JSON Data: ", json_data

combinations = itertools.combinations([1, 2, 3, 4], 2)
print "Combinations: ", list(combinations)
