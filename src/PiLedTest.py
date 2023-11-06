from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep

switch.init()
led.init()
while 1:
    if switch.read_slide_switch():
        led.set_output(0,1)
        sleep(0.1)
        led.set_output(0, 0)
        sleep(0.1)
    else:
        for i in range(0,50,1):
            led.set_output(0, 1)
            sleep(0.05)
            led.set_output(0, 0)
            sleep(0.05)
        led.set_output(0,0)
        while switch.read_slide_switch() == 0:
            pass


