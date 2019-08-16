from gpiozero import Button, LED
from time import sleep

switch = Button(8)
first = LED(14)
second = LED(15)
third = LED(18)
fourth = LED(23)
fifth = LED(24)
sixth = LED(25)

led_list = [first,second,third,fourth,fifth,sixth]

def arrow_sequence_2():
    for led in led_list:
        led.on()
        sleep(0.25)
    for led in led_list:
        led.off()
        sleep(0.25)

def arrow_sequence():    
    first.on()
    sleep(0.25)
    second.on()
    sleep(0.25)
    third.on()
    sleep(0.25)
    fourth.on()
    fifth.on()
    sleep(0.25)
    sixth.on()
    sleep(0.25)
    
    first.off()
    second.off()
    third.off()
    fourth.off()
    fifth.off()
    sixth.off()
    
    sleep(0.25)    
    
def arrow_flash():
    first.on()
    second.on()
    third.on()
    fourth.on()
    fifth.on()
    sixth.on()

    sleep(0.35)

    first.off()
    second.off()
    third.off()
    fourth.off()
    fifth.off()
    sixth.off()
    
    sleep(0.35)

while True:
    if switch.is_active:
        arrow_flash()
    else:
        arrow_sequence()
