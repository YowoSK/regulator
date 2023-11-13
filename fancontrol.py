#!/usr/bin/env python3

import time

from gpiozero import OutputDevice


ON_THRESHOLD = 65  # Fan turns on if tempreture is 65 degrees
OFF_THRESHOLD = 55  # Fan turns off if tempreture is 55 degrees
SLEEP_INTERVAL = 5  # frequency of tempreture check
GPIO_PIN = 17  # GPIO pin that is used for regulator


def get_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()

    try:
        return int(temp_str) / 1000
    except (IndexError, ValueError,) as e:
        raise RuntimeError('Could not parse temperature output.') from e

if __name__ == '__main__':
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    fan = OutputDevice(GPIO_PIN)

    while True:
        temp = get_temp()
        # spins the fan
        if temp > ON_THRESHOLD and not fan.value:
            fan.on()

        # stops the fan
        elif fan.value and temp < OFF_THRESHOLD:
            fan.off()

        time.sleep(SLEEP_INTERVAL)
