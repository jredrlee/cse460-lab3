import time

# motor code
from Motor import *
motor = Motor()

# Ultrasound Code
from Ultrasonic import *
ultrasonic = Ultrasonic()

#main code
if __name__ == '__main__':
	print("Hello")
	#initial_distance = ultrasonic.get_distance()
	try:
		print("Moving Forward")
		k = 100
		motor.setMotorModel(k,k,k,k)
		while True:
			distance = ultrasonic.get_distance()
			print(distance)
			error = distance - 50
			if error <= 3 and error >= -3:
				motor.setMotorModel(0,0,0,0)
				time.sleep(1)
				distance = ultrasonic.get_distance()
				print("final distance: ")
				print(distance)
				print("final distanceL")
				break
			else:
				k1 = k * error
				motor.setMotorModel(k1,k1,k1,k1)
		print("program is finished")
		print(ultrasonic.get_distance())
	except KeyboardInterrupt:
		motor.setMotorModel(0,0,0,0)
