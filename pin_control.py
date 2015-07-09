import wiringpi2 as wiringpi 
import time  
# blinking function 
def setup_pin(pin):
	wiringpi.wiringPiSetupSys()
	wiringpi.pinMode(pin, 1)

def turn_on(pin): 
	# set up GPIO output channel
	setup_pin(pin) 
	wiringpi.digitalWrite(pin, 1)
	return
# to use Raspberry Pi board pin numbers  

def turn_off(pin):
	setup_pin(pin)
	wiringpi.digitalWrite(pin, 0)
	return


if __name__ == '__main__':
	setup_pin(17)
	while True:
		turn_on(17)
		time.sleep(1)
		turn_off(17)

	