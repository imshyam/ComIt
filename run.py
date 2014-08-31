import requests
import json
import sys

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '807834b1529d46b54b22f7427156bf95562db4df'

filename=sys.argv[1]
source = open(filename, 'r')
language=filename.rsplit('.',1)[1]
#C C++ Clojure Haskell C# Java Objective-C Perl PHP Python ruby
print "\nLanguage Detected : ",language.upper(),"\n"
if language.upper()=="C":
	lang="C"
elif language.upper()=="CPP":
	lang="CPP"
elif language.upper()=="PY":
	lang="PYTHON"
elif language.upper()=="CS":
	lang="CS"
elif language.upper()=="CD":
	lang="CS"
elif language.upper()=="CDF":
	lang="CDf"
else:
	print "This Is Not A Compitible Language.\n"
	sys.exit()

data = {
    'client_secret': CLIENT_SECRET,
    'async': 0,
    'source': source.read(),
    'lang': lang,
    'time_limit': 5,
    'memory_limit': 262144,
}

r = requests.post(RUN_URL, data=data)
source.close()

payload= r.json()
#print payload

run_status = payload.get('run_status')
o = run_status['output']
web=payload.get('web_link')
print "output:"
print "\t",o
print "Web Link For Code : ",web,"\n"
