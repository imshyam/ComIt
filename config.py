import os
import os.path
from os.path import expanduser

home = expanduser("~")
#copy runWithoutRequests.py to home folder
runpyAtHome=home+'/runWithoutRequests.py'
if os.path.isfile(runpyAtHome)==False:
	os.system("cp runWithoutRequests.py ~/")
	os.system("echo '\nDone.\n'")
else:
	os.system("echo '\nrun.py Already Exists At Home.\n'")


filename=home+'/.bashrc'
#checking if command already exists
if 'comit' in open(filename).read():
	os.system("echo '\nCommand \"comit\" Already Exists.\n'")
#else Create a command
else:
	f=open(filename,'a')
	f.write("\nif [ -z \"$2\" ]; then alias comit='python ~/runWithoutRequests.py $1'; else alias comit='python ~/runWithoutRequests.py $1 $2'; fi")
	f.close()
	os.system(". ~/.bashrc")
	os.system("echo '\nDone With All Tasks.\n'")
