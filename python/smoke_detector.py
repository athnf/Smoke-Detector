import serial
import time

arduino = serial.Serial('COM3', 9600)  

while True:
    data = arduino.readline().decode().strip()
    
    print("Smoke Value:", data)
    
    if int(data) > 500:  
        print("Detected Smoke! Take action.")
    else:
        print("No smoke detected.")
    
    time.sleep(1) 
