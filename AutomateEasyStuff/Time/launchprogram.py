#start an external program in python. ctrl-click the application and select show package 
#contents to find the executable file. 

import subprocess

calc = subprocess.Popen(['open', '/Applications/Python 2.7/IDLE.app'])

calc.poll()


print('Done')

#poll() asks your friend if they are finished with program
#wait() blocks use until the launch process has terminated