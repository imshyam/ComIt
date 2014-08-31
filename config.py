import os
import os.path
from os.path import expanduser

home = expanduser("~")
#copy run.py to home folder
runpyAtHome=home+'/run.py'
if os.path.isfile(runpyAtHome)==False:
	os.system("cp ~/Downloads/ComIt/run.py ~/")
else:
	os.system("echo '\nrun.py Already Exists At Home.\n'")


filename=home+'/.bashrc'
#checking if command already exists
if 'comit' in open(filename).read():
	os.system("echo '\nCommand \"comit\" Already Exists.\n'")
#else Create a command
else:
	f=open(filename,'a')
	f.write("\nalias comit='python ~/run.py $1 $2'")
	f.close()
	os.system(". ~/.bashrc")