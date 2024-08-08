<link rel="stylesheet" type="text/css" href="../../assets/css/styles.css">

# Lab 2: RGB LED Intro

This lab will be your first chance to really exercise the Circuitpython interface to your Arduino Nano. We'll learn about using the REPL interface and about creating and modifying code which lives on your board. 

## Objective
- Learn how to interact with your board using the REPL interface 
- Learn how to write Python code which gets uploaded to your board
- Learn how to use the onboard RGB LED using the digitalio and board modules

## Materials
- Arduino Nano ESP32
- USB cable

## Deliverables
- Your onboard RGD LED blinks BLUE (using the setRGB function) at 5Hz with a 50% duty cycle. 

## Extensions
- Make the LED change color every 10 blinks.
- Make the blink speed ramp up to 50Hz, then back down to 5Hz. 

## Instructions

### Step 1: Get Started
1. Connect your Arduino Nano ESP32 to your computer.
2. Open Mu. If you have any problems detecting your board, return to Lab 1!

### Step 2: Playing with REPL
1. Before we can interact with the onboard RGB LED, we need to figure out what pin names to use. Connect to the REPL interface by clicking the *Serial* button and pressing enter.

2. We can find all the valid pin names in the `board` module. Remember, this is Python, so we start by typing `import board`. 

3. We can see the pins defined in `board` by typing `dir(board)`. <u>Find the **three** pin names which seem to logically connect with the onboard RGB LED</u>. Write them down; you can put them in commented lines (`# text`) in the `code.py` file Mu has open right now, for example. 

4. You can also copy and paste more than one line of code at a time into your REPL interface for testing. We are going to use the `digitalio` module built into Circuitpython to toggle our LED. What do you need to do before you'll be able to use `digitalio`?

5. Let's turn the red LED on. Copy the code below into your REPL interface:
    ```python
    led_red = digitalio.DigitalInOut(board.LED_R)
    led_red.direction = digitalio.Direction.OUTPUT
    ```

6. You can turn the LED on and off using `led_red.value=1` and `led_red.value=0`. <u>Which one turns the LED on, and which one turns the LED off?</u>

### Step 3: Writing Python code that lives on your Nano
1.  Your Mu editor automatically opens the `code.py` file which lives on your Nano. This is the code that will *automatically execute* whenever your board is powered on (or the reset button is pressed). If you want to change the code on the board, you can either drag a new `code.py` file to the CIRCUITPY drive, or simply edit this file in Mu and click Save.

2. Try opening the Serial interface in Mu, then pressing CTRL-D to reload. You should see `Hello World!` assuming you haven't messed with your `code.py` yet. Try editing the string that gets printed, pressing Save, then reloading. Hopefully you see the changes reflected.

3. Using the code skeleton provided below, you are now on your own to complete the lab. Check what you need to accomplish in the **Deliverables** section above. If you have time, try the **Extensions**. 

    ```python
    import time
    import board
    import digitalio

    # Setup the onboard LED
    led_red = digitalio.DigitalInOut(board.LED_R)
    led_red.direction = digitalio.Direction.OUTPUT

    led_green = digitalio.DigitalInOut(board.LED_R) #don't forget to change this to the correct pin
    led_green.direction = digitalio.Direction.OUTPUT
    
    #led_blue setup goes here
  
    # Initialize all LEDs to OFF
    led_red.value = 1
    led_blue.value = 1
    led_green.value = 1

    def main():
        while True:
            led_green.value = 0 #replace this to use the setRGB function instead
            time.sleep(1.0) #note: time.sleep is in seconds
            led_green.value = 1 #replace this to use the setRGB function instead
            time.sleep(1.0)

    def setRGB(red, green, blue):
        led_red.value = red
        led_green.value = green
        led_blue.value = blue

    if __name__ == '__main__'
        main()
    ```

4. If we overwrite the `code.py` file later, this code will all disappear. That would be a shame! We might want to build on this foundation later. Go ahead and use your chosen Python IDE to create and save a `lab2.py` file with this completed code into the directory you created back in Lab 1. 