import requests
import json
import sys
import os.path

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '807834b1529d46b54b22f7427156bf95562db4df'


#taking file input
#supported languages:
#C C++ Clojure Haskell C# Java Objective-C Perl PHP Python ruby
#C, CPP, CPP11, CLOJURE, CSHARP, JAVA, JAVASCRIPT, HASKELL, PERL, PHP, PYTHON, RUBY
filename=sys.argv[1]
source = open(filename, 'r')
language=filename.rsplit('.',1)[1]


#decide language
if language.upper()=="C"  or language.upper()=="H":#.c .h
	lang="C"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="CPP" or language.upper()=="CC" or language.upper()=="CXX" or language.upper()=="C++" or language.upper()=="H" or language.upper()=="HH":#.cc .cpp .cxx .c++ .h .hh 
	lang="CPP"
	print "\nLanguage Detected : ",lang ," or CPP11","\n"
elif language.upper()=="PY" or language.upper()=="PYW" or language.upper()=="PYC" or language.upper()=="PYO" or language.upper()=="PYD":#.py .pyw, .pyc, .pyo, .pyd
	lang="PYTHON"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="CLJ" or language.upper()=="EDN":#.clj .edn
	lang="CLOJURE"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="JAVA" or language.upper()=="CLASS" or language.upper()=="JAR":#.java .class .jar
	lang="JAVA"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="RB" or language.upper()=="RBW":#.rb .rbw
	lang="RUBY"
	print "\nLanguage Detected : ",lang,"\n"#.js
elif language.upper()=="JS":
	lang="JAVASCRIPT"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="HS" or language.upper()=="LHS":#.hl .hls
	lang="HASKELL"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="PL" or language.upper()=="PM" or language.upper()=="T" or language.upper()=="POD" or language.upper()=="LHS":#.pl .pm .t .pod
	lang="PERL"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="PHP" or language.upper()=="PHTML" or language.upper()=="PHP4" or language.upper()=="PHP3" or language.upper()=="PHP5" or language.upper()=="PHPS":#.php, .phtml, .php4, .php3, .php5, .phps
	lang="PHP"
	print "\nLanguage Detected : ",lang,"\n"
else:
	print "This Is Not A Compitible Language.\n"
	print "Extention Detected : ",language.upper(),"\n"
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

r = requests.post(RUN_URL, data=data)
source.close()

payload= r.json()
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
