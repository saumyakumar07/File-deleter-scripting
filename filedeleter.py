import subprocess
import os 
from colorama import Fore 

cmd = subprocess.check_output('(dir) D:\*(filetype) /S /B', shell= True).decode().split('\n') #write drive in place of dir and filetype 

#for i in cmd:      #Remove comment from line 7-13 

   # if i != '':
      #  i = i[:-1]

      #  os.remove(i)
     #   print(Fore.RED + i + 'is deleted now :))!!')
