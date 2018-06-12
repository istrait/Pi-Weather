# From https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/6


from gpiozero import Button
import time
import math
import statistics

store_speeds = []       #Store the speeds measured in an array

wind_count = 0          # Number Half Rotations
radius_cm = 9.0         # Radius of Anemometer
wind_interval = 5       # Reporting Speed
cm_in_a_mile = 160934.0 # Convert to miles
secs_in_hour = 3600     # Seconds in hour for calculation
adjustment = 1.18       # Adjust for anemometer factor


# Spin Function, Every half rotation add one to count

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin" + str(wind_count))

# Calc Wind Speed
def calculate_speed(time_sec):
    global wind_count
    circumference_cm = (2 * math.pi) * radius_cm
    rotations = wind_count / 2.0

    # Calculated distance travelled by a cup in cm
    dist_cm = (circumference_cm * rotations) / cm_in_a_mile

    # Adjust to mph and calculate
    mps = dist_cm / time_sec
    mph = mps * secs_in_hour

    return mph * adjustment

# to reset wind count
def reset_wind():
    global wind_count
    wind_count = 0


wind_speed_sensor = Button(5)
wind_speed_sensor.when_pressed = spin


# Main sensing loop

while True:
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print("Speed = " , wind_speed, " mph  ", "Gust = ", wind_gust, " mph")

