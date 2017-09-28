# Gesture-mouse
Take input from an arduino to control the cursor.
The arduino uses a mpu6050 IMU sensor and sends the value from gyrometer to the PC over a serial port.
The recieved values are taken by a python script which first splits the values and decodes it using utf-8.
The values are then written directly to the cursor using pyautogui which allows the cursor to be moved to desired location.
The system can also be fitted with a flex sensor to simulate left and right mouse click by placing the flex sensor on the required fingers of the user to allow to form a human machine interface.
