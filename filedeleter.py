import subprocess
import os 
from colorama import Fore 

cmd = subprocess.check_output('dir D:\*.psd /S /B', shell= True).decode().split('\n')

for i in cmd:

    if i != '':
        i = i[:-1]

        os.remove(i)
        print(Fore.RED + i + 'is deleted now :))!!')