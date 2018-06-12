# From https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/9

from gpiozero import Button

rain_sensor = Button(6)   # Connected to GPIO pin 6
bucket_size = .011        # Size in inches
count = 0                 # Times tipped

# Up count when bucket is tipped
def bucket_tipped():
    global count
    count = count +1
    print (count * bucket_size)

#reset count to 0
def reset_rainfall():
    global count
    count = 0


rain_sensor.when_pressed = bucket_tipped
