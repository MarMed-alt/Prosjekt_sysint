import serial, time
import tkinter
import os






def smarthub():
    os.system('clear')
    serialcmd = input("TV command H, L or Q: ")
    ser.write (serialcmd.encode())
    
    if serialcmd != 'Q':
        time.sleep(0.5)
        smarthub()

    if serialcmd == 'Q':
    
        print('Program terminated.')





ser = serial.Serial()
os.system('clear')
ser.port = "/dev/cu.usbmodem141401"
ser.baudrate = 9600
ser.open()
time.sleep(0.25)
smarthub()












