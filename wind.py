// Taken from https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/7

import statistics
store_speeds = []  // creates an empty list called store_speeds

while True:
    start_time = time.time()
    while time.time() - start_time <= wind_interval:
        reset_wind()
        time.sleep(wind_interval)
        final_speed = calculate_speed(wind_interval)
        store_speeds.append(final_speed)

    wind_gust = max(store_speeds)
    wind_speed = statistics.mean(store_speeds)
    print(wind_speed, wind_gust)
