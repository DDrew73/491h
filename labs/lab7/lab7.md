<link rel="stylesheet" type="text/css" href="../../assets/css/styles.css">

# Lab 7: Sensor Characterization: Ultrasonic Obstacle Detector

Ultrasonic rangefinding was one of the first techniques for mobile robot obstacle detection and avoidance. Even in a world where onboard computer vision is near ubiquitous, ultrasonic ranging provides a simple, affordable, and computationally inexpensive method of obstacle detection. A vast number of small wheeled robots still use ultrasonic and/or infrared rangefinding for autonomy. We will be developing some of the code required to interface with this new sensor, and then characterizing the sensor performance. 

## Objectives
- Be able to translate ultrasonic rangefinder readings into a physical distance
- Be able to perform a suite of experiments and collect the required data to fully characterize a novel sensor's performance
- Understand how to write your own sensor driver code

## Materials
- Arduino Nano ESP32
- USB cable
- Breadboard
- HC-SR04 ultrasonic range sensor breakout board
- Ruler
- MM jumper wires
- 10k resistor
- potentiometer

## Deliverables
- Code that continuously outputs the ultrasonic rangefinder's distance measurement in centimeters using a custom function and turns on an LED with varying intensity depending on obstacle distance

## Extensions
- Walk around the room using only your breadboard for guidance, if you dare! 

## Instructions

### Step 1: Get Started
1. Connect your Arduino Nano ESP32 to your computer.

2. Open Mu. If you have any problems detecting your board, return to Lab 1!

3. First we need the supporting library to use the IMU. Since you can't use something like `pip` on your board (it's not connected to the internet!), you will have to download the library and manually add it to your CIRCUITPY drive in the `lib` folder. [Here is a link](assets/adafruit_hcsr04.py) to download the `adafruit_hcsr04.py` file you will need. You will also need to add the entire `adafruit_bus_device` folder linked [here](assets/adafruit_bus_device.zip).

### Step 2: Wire Up The Sensor
1. This sensor is a bit tricky to use for us, because it operates at 5V while our Arduino runs at 3.3V. Luckily, the `VBUS` pin on your Arduino will pass the USB voltage (5V) directly through. Connect `VBUS` to the ultrasonic sensor's `Vcc`, and `GND` to `Gnd`. 

2. Connect `Trig` to a digital pin.

3. The `Echo` output of the ultrasonic sensor will come out at 5V, so we need to convert that to a voltage below 3.3V. Use the potentiometer and 10k resistor as a voltage divider to do this. Remember, the total resistance of our potentiometer is 10k, so we can use these together to halve the voltage. Set this circuit up and connect the Vout node to a digital pin of your Arduino. The Vin node will be the `Echo` output of the ultrasonic sensor.

4. Let's make sure we hooked it up correctly. Run this code in REPL and make sure it executes, but be sure to change the `trigger_pin` and `echo_pin` to agree with the digital pins you used earlier!

```python
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
```

### Step 3: Distance Measurements
1. Write code to continously output distance measurements in centimeters using ``sonar.distance``. 

2. Verify that this measurement is accurate using your ruler. Play around; when does the sensor struggle? When does it work really well?

3. We don't need to use external libraries for every sensor we find, we can write our own driver code! This is an important skill to develop, because sometimes external libraries won't exist or won't be compatible with your system.

4. You can find the technical datasheet for the HCSR04 [here](assets/HCSR04.pdf). The most important part for us to internalize will be the information in the **Timing diagram** section. 

5. Set up a digital pin as an output to use as the trigger pin. Set up a digital pin as an input to use as the echo pin. 

6. Write a function that initiates an ultrasonic reading by raising the trigger pin high for 10 microseconds, then waiting for the echo pin to go high, then calculating how long the echo pin remained high. The function should return the distance in centimeters by dividing the time the echo pin was high, in microseconds, by 58. <br> **Hint:** The `time.monotonic_ns()` function will return time in nanoseconds instead of seconds, for when you need this level of precision. Remember, microseconds are nanoseconds / 1000. <br> **Hint:** Based on the datasheet `we suggest to use over 60ms measurement cycle`, build in a "timeout" so you don't get errors. One way to do this is to always wait 60 ms or longer while waiting for the echo pin return, using a while loop wrapper.

7. Continously print this new measurement. Verify that this measurement is accurate using your ruler.

### Step 4: Deriving Scale Factors
1. Let's pretend the datasheet *didn't* tell us to divide the reading by 58. I'll tell you that **the duration of the `ECHO` pulse being high is proportional to the distance in centimeters.** I want you to use your ruler and the `np.polyfit` function from Lab 5 to find the slope of the duration in microseconds (y axis) and distance (centimers) curve. 

2. Collect at least five data points to construct this curve. Three ways to do this: Manually, by writing things down; programatically, by filling an array with a set delay between measurements; and with a hybrid approach, where we could try using `distance = int(input("Enter the current distance in centimeters:\n"))` and then constructing an array of (distance, pulse duration) points. I encourage you to do that last thing, because it's fun.

3. Fit a first degree polynomial to your data. What is the slope of the line? 

4. The ultrasonic wave must travel to the target then return. With this in mind, write down the equation for calculating the distance based on the speed of sound. Make the units match by converting the time to microseconds and the distance to centimeters. Notice anything? 

### Step 5: Obstacle Detector
1. Imagine this is an obstacle detector for an autonomous robot. Make the RED LED get more or less bright depending on how close you are to an object. Set the scaling up correctly so that the LED is all the way *on* at a distance of 5 cm or less, and all the way *off* at a distance of over 100 cm. 

