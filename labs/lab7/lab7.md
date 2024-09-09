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

## Deliverables
- Code that continuously graphs the ultrasonic rangefinder's distance measurement (correctly converted), corrects for any detected nonlinearity, and turns on an LED with varying intensity depending on obstacle distance

## Extensions
- Walk around the room using only your breadboard for guidance, if you dare! 

## Instructions

### Step 1: Get Started
1. Connect your Arduino Nano ESP32 to your computer.

2. Open Mu. If you have any problems detecting your board, return to Lab 1!

3. First we need the supporting library to use the IMU. Since you can't use something like `pip` on your board (it's not connected to the internet!), you will have to download the library and manually add it to your CIRCUITPY drive in the `lib` folder. [Here is a link](assets/adafruit_mma8451.py) to download the `adafruit_mm8451.py` file you will need.

4. Hook up the IMU breakout board with the x axis (labeled on the board) pointed towards the top of your Arduino (where the USB cable connects). Connect 3.3V to VIN and GND (white shaded pin) to GND on the board. 

5. Uh oh, there are no SDA or SCL labels on your Arduino! In your REPL interface, `import board`, and check `dir(board)`.Call the `board.SCL` and `board.SDA` manually (just type them) to <u>find out what pins they correspond to</u>, then hook up your IMU! 

6. If everything was hooked up correctly and the library was successfully put on your drive, this code snippet should execute in REPL with no problem:

    ```python
    import board
    import adafruit_mma8451
    i2c = board.I2C()
    sensor = adafruit_mma8451.MMA8451(i2c)
    ```

### Step 2: Building Intuition
1. Check the acceleration measurements on the three axes using `sensor.acceleration`. <u> Based on these measurements, which one corresponds to the z axis?</u> 

2. Rotate your breadboard in 90 degree increments about the x- and y- axes (as depicted on the breakout board) and take new `sensor.acceleration` measurements so you get a sense of how these numbers work.

### Step 3. Building Out Infrastructure

1. Let's switch to writing persistent code in `code.py` if you haven't already. Write a function which converts the `sensor.acceleration` values to units of "g's" and returns them. <br> *Hint:*Remember from elementary physics that one "g" equals 9.8m/s^2. 

2. Write a function which calculates and returns three inclination angles using Equations 11, 12, and 13 in Reading 9. <br> *Hint:* `ulab.numpy` has `atan`. <br> *Hint:* It's hard to read things in radians! Convert to degrees.

3. Theta, phi, and psi are not very intuitive measurements for pose. Write a function which converts these into Euler angles: roll, pitch, and yaw. If it helps, consider the USB cable side of your Arduino the "nose" of an aircraft. "Pitch" is moving the nose up or down, "roll" is "flipping over sideways", and "yaw" is rotating about the center axis. <br> *Hint:* Rotate your breadboard in a circle around the center axis (i.e., imagine the "z" axis which points "up" from it). Do any of the readings change?

<img src="assets/euler_plane.png" alt="Euler angles labeled on an airplane" width="400"/>

4. We are interested in the angle of your *breadboard*, not the angle of the *breakout board*. If it was mounted at an angle, like if your clumsy professor soldered them weirdly, then you will get spurious readings relative to your breadboard position! Write a function which calibrates your output using some initial data taken when your breadboard is resting. 

5. You may notice significant jitter in your calculations when moving the board around, especially if you don't have any `time.sleep` built into the loop. Write a function to average multiple data points in a row to smooth this out. <br> *Hint:* While you did something like this in the prior lab, it can be hard to work with python tuples in this way. Try stuffing your `sensor.acceleration` into a numpy array using `np.array(sensor.acceleration)` for an easier time processing it.

6. You may experience catastrophic errors in your inclination angle calculation math (e.g., divide by zero) at large tilt angles. Add [try: except: blocks](https://www.w3schools.com/python/python_try_except.asp) to this function so that if there is an error, they just default to returning 0. 

7. Take a breath- that was a lot of coding! Make sure that your code works correctly by zooming your board around in the air and evaluating what prints out. Cool!

### Step 4: The Basic Tilt-a-Maze Game 

1. Implement a basic tilt-a-maze game whic has only outer perimeter walls and no goal position using these code primitives:

A basic maze geometry, where `#` is a boundary. 

```python
maze = [
    "#############",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#           #",
    "#############"
]
```

A function for printing the maze you have defined, as well as the player marker `O`. Note that you will need to pre-define a starting position for this to work. 

```python
def print_maze():
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if x == player_x and y == player_y:
                row += "O"
            else:
                row += maze[y][x]
        print(row)
```

A function for moving the player marker based on accelerometer tilt:

```python
def move_player(roll, pitch):
    global player_x, player_y

    # Convert roll and pitch into movement directions
    if pitch < -5:  # Move up
        new_y = player_y - 1
        if maze[new_y][player_x] in " ":
            player_y = new_y
    elif pitch > 5:  # Move down
        new_y = player_y + 1
        if maze[new_y][player_x] in " ":
            player_y = new_y
    if roll < -5:  # Move left
        new_x = player_x - 1
        if maze[player_y][new_x] in " ":
            player_x = new_x
    elif roll > 5:  # Move right
        new_x = player_x + 1
        if maze[player_y][new_x] in " ":
            player_x = new_x
```
2. Verify that your basic game works. Read the code carefully, especially the `move_player` function. Modify this code and your maze definition so that there is a goal position denoted by an `X`. If the player reaches the `X`, let them know they have won. <br>*Hint:* If you end up in a situation where your ball can get next to the `X` but never "enter" it, consider your allowable moves specified in the function. 

### Step 5: Adding Complexity

1. When the player wins, restart with a new maze, randomly chosen from a list of at least 3 which you create beforehand. 

2. Add dynamic sensitivity adjustment to your game using a potentiometer. There are lots of ways to do this; the simplest is to adjust the threshold of angle which counts as a "move" based on the reading. 

3. Show off your creation to your friends, professor, family, dog, etc. Nice job, you made an interactive electronic game!



