"""
:copyright: (c) 2014 by Shyam Sundar Choudhary.
:license: The MIT License , see LICENSE for more details.
"""
import language
#import requests
import json
import sys
import os.path
import urllib
import urllib2

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '807834b1529d46b54b22f7427156bf95562db4df'


#taking file input
#supported languages:
#C C++ Clojure Haskell C# Java Objective-C Perl PHP Python ruby
#C, CPP, CPP11, CLOJURE, CSHARP, JAVA, JAVASCRIPT, HASKELL, PERL, PHP, PYTHON, RUBY
filename=sys.argv[1]
source = open(filename, 'r')
langua=filename.rsplit('.',1)[1]


#decide language
if langua in language.DetectedLanguage:
	lang=language.DetectedLanguage[langua]
	print "\nLanguage Detected : ",lang,"\n"
else:
	print "This Is Not A Compitible Language.\n"
	print "Extention Detected : ",langua.upper(),"\n"
	sys.exit()

#taking input
if len(sys.argv)<=2:
	print "No Input Provided."
	inp=""
else:
	print "provided input : "
	input_file_name=sys.argv[2]
	inp= open(input_file_name, 'r').read()
	print inp
print

#data to be sent
data = {
	'input' : inp,
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': lang,
    'time_limit': 5,
    'memory_limit': 262144,
}

req = urllib2.Request(RUN_URL, urllib.urlencode(data))
res = urllib2.urlopen(req)

# response in JSON format
payload = json.load(res)

#if requests
#r = requests.post(RUN_URL, data=data)

#closing source file
source.close()

#if requests then
#payload= r.json()

#print payload

run_status = payload.get('run_status')
o = run_status['output']
web=payload.get('web_link')
time=run_status['time_used']
memory=run_status['memory_used']
print "output : "
print "\n",o
print "Memory Used : ",memory,"\n"
print "Time Taken : ",time,"\n"
print "Web Link For Code : ",web,"\n"
