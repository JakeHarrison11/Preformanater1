import atexit
from atexit import register
import serial
from re import split
from time import sleep
import time
from nt import write
import os
from nt import read
from os import popen
from nt import system

print("""  _____  ______ _____  ______ ____  _____  __  __          _   _       _______ ______ _____  
 |  __ \|  ____|  __ \|  ____/ __ \|  __ \|  \/  |   /\   | \ | |   /\|__   __|  ____|  __ \ 
 | |__) | |__  | |__) | |__ | |  | | |__) | \  / |  /  \  |  \| |  /  \  | |  | |__  | |__) |
 |  ___/|  __| |  _  /|  __|| |  | |  _  /| |\/| | / /\ \ | . ` | / /\ \ | |  |  __| |  _  / 
 | |    | |____| | \ \| |   | |__| | | \ \| |  | |/ ____ \| |\  |/ ____ \| |  | |____| | \ \ 
 |_|    |______|_|  \_\_|    \____/|_|  \_\_|  |_/_/    \_\_| \_/_/    \_\_|  |______|_|  \_\
                                                                                             
                                                                                             """)



cpuText = "CPU: ".encode()

ser1 = serial.Serial('COM5', 9600)
print("Initialized!")

time.sleep(3)
print("Writing to display")

while True:
    output = os.popen("""@for /f "skip=1" %p in ('wmic cpu get loadpercentage') do @echo %p%""").read()
    encodedOutput = output.encode()
    ser1.write(cpuText + encodedOutput.splitlines()[0])
    #print(output.splitlines()[0])
    time.sleep(.1)
