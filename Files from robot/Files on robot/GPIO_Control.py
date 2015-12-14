import RPi.GPIO as GPIO
import argparse
import sys
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


parser = argparse.ArgumentParser(prog=sys.argv[0],
                           #usage="Interface from application to RPi GPIO",
                           description="Motor Control Arguments",
                           #epilog,
                           #parents,
                           #formatter_class,
                           #prefix_chars,
                           #fromfile_prefix_chars,
                           #argument_default,
                           #conflict_handler,
                           add_help=True)
    
parser.add_argument("-dir",
                    action="store",
                    nargs="?",
                    #cosnt,
                    #default,
                    type=int,
                    choices=[1,2,3,4],
                    required=True,
                    help="Which direction to move robot?",
                    metavar="dir",
                    dest="dir"
                    )
                   
args = parser.parse_args()

def TestLeds():
	GPIO.output(motor_1a,1)
	time.sleep(5)
	GPIO.output(motor_1a,0)
	GPIO.output(motor_1b,1)
	time.sleep(5)
	GPIO.output(motor_1b,0)
	GPIO.output(motor_2a,1)
	time.sleep(5)
	GPIO.output(motor_2a,0)
	GPIO.output(motor_2b,1)
	time.sleep(5)
	GPIO.output(motor_2b,0)
	print("finished")

#Move the robot forward or backward. 
def Move(dir):
   dist=.7

	#Move forward
   if args.dir == 1:
	  for x in range (0,1):
	     GPIO.output(motor_1a,1)
	     time.sleep(.04)
	     GPIO.output(motor_2a,1)
	     time.sleep(dist)
	     GPIO.output(motor_1a,0)
	     GPIO.output(motor_2a,0)
	     GPIO.output(motor_1b,1)
	     GPIO.output(motor_2b,1)	
	     time.sleep(.06)
	     GPIO.output(motor_1b,0)
	     GPIO.output(motor_2b,0)
    
    
    #Move backward
   if args.dir == 2:
	  for x in range (0,1):
	     GPIO.output(motor_1b,1)
	     time.sleep(.042)
	     GPIO.output(motor_2b,1)
	     time.sleep(dist)
	     GPIO.output(motor_1b,0)
	     GPIO.output(motor_2b,0)
	     GPIO.output(motor_1a,1)
	     GPIO.output(motor_2a,1)	
	     time.sleep(.06)
	     GPIO.output(motor_1a,0)
	     GPIO.output(motor_2a,0)
    
    
    #Rotate Right
   if args.dir == 3:
	  for x in range (0,1):
	     GPIO.output(motor_1a,1)
	     GPIO.output(motor_2b,1)
	     time.sleep(.39)
	     GPIO.output(motor_1a,0)
	     GPIO.output(motor_2b,0)
	     GPIO.output(motor_1b,1)
	     GPIO.output(motor_2a,1)	
	     time.sleep(.06)
	     GPIO.output(motor_1b,0)
	     GPIO.output(motor_2a,0)
    
    #Rotate Left
   if args.dir == 4:
	  for x in range (0,1):
	     GPIO.output(motor_1b,1)
	     GPIO.output(motor_2a,1)
	     time.sleep(.4)
	     GPIO.output(motor_1b,0)
	     GPIO.output(motor_2a,0)
	     GPIO.output(motor_1a,1)
	     GPIO.output(motor_2b,1)
	     time.sleep(.06)
	     GPIO.output(motor_1a,0)
	     GPIO.output(motor_2b,0)	
		
	#Turn off gpio
   GPIO.output(motor_1a, 0)
   GPIO.output(motor_1b, 0)
   GPIO.output(motor_2a, 0)
   GPIO.output(motor_2b, 0)
	
	
#Main execution of script
def main():


	
   Move(dir)
    #TestLeds()
    
   GPIO.cleanup()


main()
        


