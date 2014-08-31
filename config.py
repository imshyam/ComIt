import os

f=open('.bashrc','r+')
f.write("alias comit='python ~/run.py $1 $2'")
f.close()
os.system(". ~/.bashrc")