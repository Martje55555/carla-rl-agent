import os
import signal
import time
import sys
import subprocess

def kill():
    os.system("TASKKILL /F /IM CarlaUE4-Win64-Shipping.exe")
    time.sleep(10)
    os.system("TASKKILL /F /IM pygame window.exe")

def killCarla(c):
	client = "CarlaUE4"	
	try:
		# iterating through each instance of the process
		for line in os.popen("ps ax | grep " + client + " | grep -v grep"):
			fields = line.split()
			
			# extracting Process ID from the output
			pid = fields[0]
			
			# terminating process
			os.kill(int(pid), signal.SIGKILL)
		
		print("Process Successfully terminated")
		c = False
	except:
		print("Error Encountered while running script")

def killPy(p):
	name = "Python"
	try:
		# iterating through each instance of the process
		for line in os.popen("ps ax | grep " + name + " | grep -v grep"):
			fields = line.split()
			
			# extracting Process ID from the output
			pid = fields[0]
			
			# terminating process
			os.kill(int(pid), signal.SIGKILL)
		print("Process Successfully terminated")
		p = False
	except:
		print("Error Encountered while running script")

def startCarla(c):

	try:
		DETACHED_PROCESS = 0x00000008
		results = subprocess.Popen(['CarlaUE4.exe'],
								close_fds=True, creationflags=DETACHED_PROCESS)
		print(results.pid)
		c = True
		time.sleep(10)
	except:
		print("Error encountered trying to open Carla Client")

def startPy(p):
	try:
		subprocess.check_call(['python','main.py'], stdout=sys.stdout, stderr=subprocess.STDOUT)
		p = True
	except:
		print("Error trying to run main.py script")

def runningLoop():
	c = False
	p = False
	while(True):
		time.sleep(30)
		if c == True:
			killCarla(c)
		if p == True:
			killPy(p)
		if c == False:
			startCarla(c)
		if p == False:
			startPy(p)
        #kill()


def main():
    runningLoop()

if __name__ == '__main__':

    main()
