<script src="/assets/scripts/copy-to-clipboard.js"></script>

# Lab 1: Blinking an LED

## Objective
Learn how to blink an onboard LED on the Arduino Nano ESP32 using CircuitPython.

## Materials
- Arduino Nano ESP32
- USB cable

## Instructions

### Step 1: Setup
1. Connect your Arduino Nano ESP32 to your computer.
2. Open your preferred code editor.

### Step 2: Code
```python
import time
import board
import digitalio

# Set up the onboard LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True  # Turn on the LED
    time.sleep(0.5)   # Wait for 500ms
    led.value = False # Turn off the LED
    time.sleep(0.5)   # Wait for 500ms
```
