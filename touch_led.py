import RPi.GPIO as GPIO
import time

TOUCH_PIN = 15
LED_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

led_state = False

try:
    while True:
        if GPIO.input(TOUCH_PIN) == 1:
            led_state = not led_state
            GPIO.output(LED_PIN, led_state)
            time.sleep(0.5)  # debounce delay

except KeyboardInterrupt:
    GPIO.cleanup()
