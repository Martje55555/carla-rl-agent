import os
import time
import sys
import subprocess

cmd = 'C:\\CARLA\\CARLA_0.9.13\\WindowsNoEditor\\CarlaUE4.exe'

def kill():
    os.system("TASKKILL /F /IM CarlaUE4-Win64-Shipping.exe")
    time.sleep(10)
    os.system("TASKKILL /F /IM pygame window.exe")


def killCarla():
    print("I am in the kill carla function")

    try:
        print("doing it")
        os.system('wmic process where name="CarlaUE4-Win64-Shipping.exe" delete')
        return False
    except:
        print("not doing it")
        print("Did not find process carla")

def killPy():
    print("I am in the kill python function")

    try:
        print("doing it")
        os.system('wmic process where name="Python" delete')
        return False
    except:
        print("not doing it")
        print("Did not find process python")

def startCarla():
    print("Starting Carla Client")

    try:
        DETACHED_PROCESS = 0x00000008
        results = subprocess.Popen(cmd,
                                   close_fds=True, creationflags=DETACHED_PROCESS)
        print(results.pid)
        return True

    except:
        print("Error encountered trying to open Carla Client")


def startPy():
    print("Starting Python Script")
    try:
        subprocess.check_call(['python', 'main.py'],
                              stdout=sys.stdout, stderr=subprocess.STDOUT)
        return True
    except:
        print("Error trying to run main.py script")


def runningLoop():
    c = False
    p = False
    while(True):
        if p or c == False:
            c = startCarla()
            p = startPy()
            time.sleep(30)
        else:
            c = killCarla()
            p = killPy()    


def main():
    runningLoop()

if __name__ == '__main__':

    main()
