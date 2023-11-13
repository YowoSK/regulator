# regulator
This project involves the creation of an active cooling system for a Raspberry Pi. Components were carefully soldered together to form the hardware part of the cooling system. Script is responsible for regulating the temperature of the CPU
# Raspberry Pi 4 Active Cooling System Regulator

This Python script is designed to regulate an active cooling system for a Raspberry Pi 4 with 8GB RAM.

## Requirements

- Python 3
- gpiozero library

## Setup

1. Connect your fan to the GPIO 17 pin on your Raspberry Pi.
2. Set your desired temperature thresholds in the script:
   - `ON_THRESHOLD`: The temperature at which the fan turns on. Default is 65 degrees.
   - `OFF_THRESHOLD`: The temperature at which the fan turns off. Default is 55 degrees.
   - Note: `OFF_THRESHOLD` must be less than `ON_THRESHOLD`.
3. Set `SLEEP_INTERVAL` to determine how frequently the script checks the temperature. Default is 5 seconds.

## Usage

Run the script with Python 3
tutorial for step by step usage of my project is here: http://yowo.sk/regulator/index.html

```bash
python3 fan_regulator.py
