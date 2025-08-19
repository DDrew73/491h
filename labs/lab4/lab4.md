<link rel="stylesheet" type="text/css" href="../../assets/css/styles.css">

# Lab 4: Analog Inputs and Outputs: The LED DJ Board

This lab will serve as a basic introduction to one of the most important functions of a microcontroller: interfacing with external circuitry and sensors to read in measured stimulus and convert it into a computationally-tractable form. We will also use an essential circuit topology, the voltage divider, along with an extremely common circuit element, the potentiometer, to explore turning analog inputs into pseudo-analog outputs. Finally, we'll develop our coding skills monitoring multiple discrete inputs inside a state machine. 

## Objectives
- Understand how analog inputs are read by a microcontroller
- Understand how to convert analog input values to a voltage
- Understand how a potentiometer works
- Understand how to use feedback from an analog input to control a physical output
- Understand how to map disparate ranges onto eachother logically based on software and physical limitations

## Materials
- Arduino Nano ESP32
- USB cable
- Breadboard
- Tactile switch ("button")
- 2x 10k resistor
- Potentiometer
- MM jumper wires

## Deliverables
- An "LED DJ Board" with an RGB LED that has brightness controlled by a potentiometer, switches colors when a button is pressed, and switches between blinking or steady when another button is pressed. 

## Extensions
- Add a mode selection feature so that the potentiometer can also control the speed of the LED blinking and/or the color of the LED. 

## Instructions
I think that this will be a challenging exercise in coding for many of you. Remember that Python list comprehension (e.g., `rgb = [120,0,0]` `rgb[0] = 120`) works here. A common strategy when debugging interactive code like this is to use `print()` statements liberally to figure out what the heck is going on when things aren't working well!

### Step 1: Get Started
1. Connect your Arduino Nano ESP32 to your computer.

2. Open Mu. If you have any problems detecting your board, return to Lab 1!

3. Use both of your 10k resistors to construct a voltage divider with the input from the 3.3V pin of your Nano and the output attached to A1. Don't forget to ground the bottom!

### Step 2: Taking ADC Measurements
1. Let's use the REPL interface to first explore how to take analog readings using the built-in ADC. This code will set up your A1 pin as an analog input:
    ```python
    import board
    from analogio import AnalogIn
    analog_in = AnalogIn(board.A1)
    ```

2. To read the analog input (i.e., perform a "analogRead()" in Arduino parlance), simply call `analog_in.value`. Remember that you can press the up arrow on your keyboard and press enter to re-run the last REPL command. Connect the A1 jumper wire directly to the 3.3V pin and check the `analog_in.value`. <u>Assuming that the max value is the closest power-of-two from this number, how many bits of resolution are being reported by your analog_in.value call?</u> Note that this is not the actual resolution of your ADC; the Circuitpython `analogio` library is upscaling it.

3. Return the A1 jumper wire to the output node of your voltage divider. Before you take another value, think; what should it be, approximately? Confirm this. 

4. Now we are going to modify our circuit. This may be tricky depending on how nicely you laid out the first one, so feel free to start over. Grab the potentiometer from your kit and replace the first resistor ("R1") with it. For now, leave the center pin of the potentiometer disconnected; 3.3V should be on one side, A1 and R2 on the other, nothing in the middle. 

5. Check your `analog_in.value`. Try turning your potentiometer, then checking the value again. <u>What does this tell you about the <strong>total</strong> resistance of your potentiometer?</u>

### Step 3: Dynamic Analog Inputs

1. Move the A1 wire to the center leg of the potentiometer.

2. Instead of using REPL, let's switch to constantly printing out `analog_in.value`. Modify code.py to do this. If you're confused, model your structure on prior labs. Note that you (almost) always want a sleep period after a print statement if there is no other delay. Don't forget to import the correct module to use the sleep function.

3. While your code is executing, turn the knob of the potentiometer all the way to either side. <u>What values do you see at the extremes? Think about how this relates to the circuit itself.</u> Imagine that inside the potentiometer there are actually two different resistors you can change the value of with the knob. 

### Step 4: PWM Outputs

1. Time for an exercise in code integration. Grab all your RGB LED code (i.e., the setup code and the setRGB function) from Lab 2, and smoosh it into this file. We're going to need to modify this code to work with PWM outputs for the LED instead of only digital ones. You will need to use the `pwmio` module and set up each pin like this: `led_x = pwmio.PWMOut(board.led_pin, frequency=5000, duty_cycle=0)`. The duty cycle can then be changed with `led_x.duty_cycle`.  

2. Practice reading some external documentation for [the pwmio module](https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/index.html) -- <u>what is the correct input range for the duty_cycle property?</u>

3. Typically [RGB "color pickers"](https://g.co/kgs/quuKt8K) are given in 8-bit values (0-255). Edit your `setRGB()` function so that it takes in values from 0-255 and correctly translates that to the range of the `led.duty_cycle` property. <br>*Hint:* For 255, what should the `led.duty_cycle` be based on your answer to the previous step? What can you multiply 255 by to get that number? 

4. Remember from Lab 2 that we learned a digital LOW turns the LED ON. You should also invert the input of your `setRGB()` function to make things more logical. For example, `setRGB(255,0,0)` should turn your red LED all the way ON. 

### Step 5: Mapping Inputs to Outputs

1. We want to connect the analog value from your potentiometer to the brightness of your LED. Let's first use just the red LED. If the LED should be off when you turn the potentiometer all the way in one direction (duty cycle = 0%), and fully bright when you turn the potentiometer all the way in the other direction (duty cycle = 100%), how should you map your `analog_in.value` to your `setRGB(r,g,b)` call? <br>*Hint:* Part of this is the inverse of what you did in the previous Step, but that's not all that you will need to do or the LED will never turn all the way off. 
<br>*Hint:* The .duty_cycle value has to be an integer, so make sure to cast your scaling output to an int with int()
<br>*Hint:* Error checking is important here because of the input range of .duty_cycle! Make sure to clamp the scaling output to the correct range.

2. Let's start adding complexity. Throw a button on your breadboard, wire it correctly, and configure it in code with an internal pullup. If you get lost doing this, refer to Lab 3. 

3. When the button is pressed, turn the LED to a random color. You will want to use the `random` module built into Circuitpython; `random.randint(min,max)` will give you an integer number between min and max. 

4. Now, the tricky part: figure out how to use the potentiometer to adjust the brightness of this new random color *while preserving the color*. <br>*Hint:* All three of the RGB values need to be scaled by the same factor to make this work. <br> *Hint:* Think about writing a separate function for scaling the initial RGB values you saved when you pressed the randomize button. 

5. Throw a second button into your circuit and configure it. When you press this button, the LED should start (or stop) blinking (you can decide the frequency and duty cycle) **while preserving its current color and brightness.** Get your lab checked off! <br>*Hint:* To make this more robust, try using the `time.monotic()` structure instead of just `time.sleep()`

6. If we overwrite the `code.py` file later, this code will all disappear. That would be a shame! We might want to build on this foundation later. Go ahead and use your chosen Python IDE to create and save a `lab4.py` file with this completed code into the directory you created back in Lab 1. 


### Some Notes on Code Structure
When we start working with this many inputs, we need to think more carefully about our code architecture. Here's an example, in pseudocode and using some standard python structure:
```
import everything

configure everything

def main():
    initialize state flag variables (e.g., "is_blinking = False")
    initialize output values (e.g., init RGB)

    while True:
        process inputs
            e.g., if button 1 is pressed, randomize color
            e.g., if button 2 is pressed, change state flag; don't forget debouncing!
        if (state 1 condition):
            implement blinking
        else:
            implement scaling RGB

define functions
    def setRGB
    def scaleRGB

if __name__ == '__main__':
    main()
```

{% include copy_clipboard.html %}