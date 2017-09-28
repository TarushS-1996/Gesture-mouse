import pyautogui as pg
import serial
import time
ser = serial.Serial("",9600)
val = pg.size()
x = float(val[0])
y = float(val[1])
pg.moveTo(x/2,y/2)
pg.FAILSAFE = False
while True:
    val = ser.readline()
    val = val.decode("utf-8")
    #val = [float(x) for x in val.strip().split()]
    val =val.split()
    x1 = float(val[0])
    y1 = float(val[1])
    print(str(x1)+" "+str(y1))
    pg.moveTo(x1,y1) 
    
,
