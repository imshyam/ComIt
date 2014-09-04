import os
import os.path
import mmap

#--------------creating an Alias-------------

#alias.cmd
exist=os.path.isfile("alias.cmd")
if not exist:
	os.system("echo.>alias.cmd")
aliasWrite=open("alias.cmd","r+")

s = mmap.mmap(aliasWrite.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('doskey') == -1:
	aliasWrite.write("doskey comit =python c:\Windows\ComIt\\runWithoutRequests.py $*")

#regAlias.reg
exist=os.path.isfile("regAlias.reg")
if not exist:
	os.system("echo.>regAlias.reg")
regAliasWrite=open("regAlias.reg","r+")
s1 = mmap.mmap(regAliasWrite.fileno(), 0, access=mmap.ACCESS_READ)
if s1.find('doskey') == -1:
	regAliasWrite.write("""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Command Processor]
\"AutoRun\"=\"c:\\\Windows\\\ComIt\\\\alias.cmd\" """)

#making dir to c:\windows\comit
os.system("mkdir c:\Windows\ComIt")
#coping from desktop to c:\Windows\ComIt
os.system("copy %userprofile%\Downloads\ComIt-master\* c:\Windows\ComIt")
#registring the command or making alias
os.system("c:\\Windows\\ComIt\\regAlias.reg")
