import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor_1a = 17
GPIO.setup(motor_1a, GPIO.OUT)
    
motor_1b = 18
GPIO.setup(motor_1b, GPIO.OUT)
   
motor_2a = 22
GPIO.setup(motor_2a, GPIO.OUT)
    
motor_2b = 23
GPIO.setup(motor_2b, GPIO.OUT)

dist = .63

def MoveForward():
    GPIO.output(motor_1a,1)
    time.sleep(.04)
    GPIO.output(motor_2a,1)
    time.sleep(dist)
    GPIO.output(motor_2a,0)
    time.sleep(.02)
    GPIO.output(motor_1a,0)
    GPIO.output(motor_1b,1)
    GPIO.output(motor_2b,1)	
    time.sleep(.09)
    GPIO.output(motor_1b,0)
    GPIO.output(motor_2b,0)
    time.sleep(1)

def MoveBackward():
    GPIO.output(motor_1b,1)
    time.sleep(.041)
    GPIO.output(motor_2b,1)
    time.sleep(dist)
    GPIO.output(motor_1b,0)
    GPIO.output(motor_2b,0)
    GPIO.output(motor_1a,1)
    GPIO.output(motor_2a,1)	
    time.sleep(.09)
    GPIO.output(motor_1a,0)
    GPIO.output(motor_2a,0)
    time.sleep(1)

def MoveLeft():
    GPIO.output(motor_1b,1)
    GPIO.output(motor_2a,1)
    time.sleep(.33)
    GPIO.output(motor_1b,0)
    GPIO.output(motor_2a,0)
    GPIO.output(motor_1a,1)
    GPIO.output(motor_2b,1)
    time.sleep(.09)
    GPIO.output(motor_1a,0)
    GPIO.output(motor_2b,0)
    time.sleep(1)

def MoveRight():
    GPIO.output(motor_1a,1)
    GPIO.output(motor_2b,1)
    time.sleep(.33)
    GPIO.output(motor_1a,0)
    GPIO.output(motor_2b,0)
    GPIO.output(motor_1b,1)
    GPIO.output(motor_2a,1)	
    time.sleep(.09)
    GPIO.output(motor_1b,0)
    GPIO.output(motor_2a,0)
    time.sleep(1)




def main():
    
    
    num_lines = sum(1 for line in open("commands.txt"))
    #print num_lines

    time.sleep(2)
 
    f = open("commands.txt", "r")
    i = 0
    for i in range(num_lines):
        M = f.readline()
        
        if "Forward" in M:
            MoveForward()

        elif "Backward" in M:
            MoveBackward()
            
        elif "Left" in M:
            MoveLeft()
            
        elif "Right" in M:
            MoveRight()

        else:
            print "Maze Done"
            
            
            
       
main()


