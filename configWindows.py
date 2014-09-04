import os
import os.path

#--------------creating an Alias-------------

#alias.cmd
exist=os.path.isfile("alias.cmd")
if not exist:
	os.system("echo.>alias.cmd")
aliasWrite=open("alias.cmd","r+")
if os.path.isfile("alias.cmd") and os.path.getsize("alias.cmd") == 0:
	aliasWrite.write("doskey comit =python c:\Windows\ComIt\\runWithoutRequests.py $*")

#regAlias.reg
exist=os.path.isfile("regAlias.reg")
if not exist:
	os.system("echo.>regAlias.reg")
regAliasWrite=open("regAlias.reg","r+")
if os.path.isfile("regAlias.reg") and os.path.getsize("regAlias.reg") == 0:
	regAliasWrite.write("""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Command Processor]
\"AutoRun\"=\"c:\\\Windows\\\ComIt\\\\alias.cmd\" """)

#making dir to c:\windows\comit
os.system("mkdir c:\Windows\ComIt")
#coping from desktop to c:\Windows\ComIt
os.system("copy %userprofile%\Downloads\ComIt-master\* c:\Windows\ComIt")
#registring the command or making alias
os.system("c:\\Windows\\ComIt\\regAlias.reg")
