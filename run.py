import requests
import json
import sys

# constants
RUN_URL = u'http://api.hackerearth.com/code/run/'

CLIENT_SECRET = '807834b1529d46b54b22f7427156bf95562db4df'

filename=sys.argv[1]
source = open(filename, 'r')
language=filename.rsplit('.',1)[1]
#supported languages:
#C C++ Clojure Haskell C# Java Objective-C Perl PHP Python ruby
#C, CPP, CPP11, CLOJURE, CSHARP, JAVA, JAVASCRIPT, HASKELL, PERL, PHP, PYTHON, RUBY

if language.upper()=="C"  or language.upper()=="H":#.c .h
	lang="C"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="CPP" or language.upper()=="CC" or language.upper()=="CXX" or language.upper()=="C++" or language.upper()=="H" or language.upper()=="HH":#.cc .cpp .cxx .c++ .h .hh 
	lang="CPP"
	print "\nLanguage Detected : ",lang "or CPP11","\n"
elif language.upper()=="PY" or language.upper()=="PYW" or language.upper()=="PYC" or language.upper()=="PYO" or language.upper()=="PYD":#.py .pyw, .pyc, .pyo, .pyd
	lang="PYTHON"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="CLJ" or language.upper()=="EDN":#.clj .edn
	lang="CLOJURE"
	print "\nLanguage Detected : ",lang,"\n"
elif language.upper()=="JAVA" language.upper()=="CLASS" or language.upper()=="JAR":#.java .class .jar
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
