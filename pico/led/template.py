import machine
import utime

#GPIO PINS: GPIO0, GPIO1, GPIO2
led0 = machine.Pin('0', machine.Pin.OUT)
led1 = machine.Pin('1', machine.Pin.OUT)
led2 = machine.Pin('2', machine.Pin.OUT)

while True:
    led0.toggle() # Blink LED0
    led1.toggle() # Blink LED1
    led2.toggle() # Blink LED2
    utime.sleep(0.5) # Wait 0.5 seconds
