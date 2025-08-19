<link rel="stylesheet" type="text/css" href="../../assets/css/styles.css">

# Lab 1: Getting Started with Circuitpython

In this first lab, you will be setting up the microcontroller toolchain which you will be using throughout this course. Just follow along with the instructions and ask for help if you need it. This lab must be completed by each student individually!

## Objective
- Learn about basic interfacing with the hardware and software sides of your microcontroller
- Learn to juggle multiple software packages for efficient progression through this course

## Materials
- Arduino Nano ESP32
- USB cable
- MM Jumper wire
- Breadboard

## Deliverables
- Mu editor connected to Nano's REPL interface

## Instructions

### Step 1: Get familiar with your kit. 
1. Receive a hardware kit from Dr. Drew, and make sure he writes down the kit number you received. 

2. Look at each component in the box and consider them. Do you know what it is already? Have you ever used one before?

### Step 2: Download Items
1. Download the Mu editor from [https://codewith.mu/en/download](https://codewith.mu/en/download).

2. Download Visual Studio Code ("VS Code") to use as your primary Python editor from [https://code.visualstudio.com/](https://code.visualstudio.com/). If you already have a favorite Python IDE, feel free to use that instead.

### Step 3: Check out Circuitpython
1. Plug your Arduino Nano ESP32 into your laptop.

2. A drive named "CIRCUITPY" should show up in your connected drives list. Open Mu, select *CircuitPython* from the list, and make sure it detects the board (no error thrown).

3. Click the *Serial* button at the top, then press enter. You should be in the Circuitpython REPL interface:
```
Adafruit CircuitPython 9.2.8 on 2025-08-25; Arduino Nano ESP32 with ESP32S3
>>> 
```

4. Try writing some Python code; `print("Hello world!")` is a good start. Once you understand how this works, press CTRL+D to exit the REPL interface.

5. Let's switch to using a (better) development environment, like VS Code. Keep your Mu window open. Open VS Code, then open the code.py file in the CIRCUITPY drive. 

6. Try pasting this code and then **saving the file**:
```python
print("This is a simple Python script.")
for i in range(5):
    print(f"Iteration {i + 1}")
print("End of script.")
```

7. Pull up your Mu window and verify that the expected serial output has arrived. Whenever you save new code, it automatically restarts your microcontroller and executes. Nifty!

8. It would be annoying to switch back and forth between Mu and VS Code every time you want to see output. Let's get a plugin for VS Code which lets us see the output directly there. Follow the [instructions here](https://learn.adafruit.com/using-the-circuitpython-extension-for-visual-studio-code/install-the-circuitpython-extension-for-vs-code) to install the Circuitpython extension for VS Code. Verify it works after!

### Step 4: Get Organized
1. Create a directory on your file system to use for this class. This will eventually look something like this:
```
>ece491h
>    ece491h/labs
>         lab2.txt
>         lab2.py
>         lab3.txt
>         lab3.py
>         -....
```
and will be helpful when you want to refer back to old code! I suggest that you *write down the answers to questions which I have underlined in the Lab writeups in a text file, or in a notebook.* They will be used in your lab quizzes.

2. Whenever you finish a lab, copy the code to your new folder (from the CIRCUITPY drive). Practice doing that now with your Lab 1 code.

## Helpful Additional References
- [The Official Arduino Nano ESP32 "Cheat Sheet"](https://docs.arduino.cc/tutorials/nano-esp32/cheat-sheet/)
- [Adafruit's CircuitPython startup guide](https://learn.adafruit.com/welcome-to-circuitpython/overview)