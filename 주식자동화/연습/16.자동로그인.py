from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\DAISHIN\STARTER\ncStarter.exe /prj:cp /id:kkj6369 /pwd:rlwns1! /pwdcert:rnjsrlwns1! /autostart')
time.sleep(60)