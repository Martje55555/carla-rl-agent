import os
import time
import sys
import subprocess

def kill():
    os.system("TASKKILL /F /IM CarlaUE4-Win64-Shipping.exe")
    time.sleep(10)
    os.system("TASKKILL /F /IM pygame window.exe")

def runningLoop():
    while(True):
        subprocess.check_call(['python','main.py'], stdout=sys.stdout, stderr=subprocess.STDOUT)
        time.sleep(10)
        kill() 

def main():
    runningLoop()

if __name__ == '__main__':

    main()