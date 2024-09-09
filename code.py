import board, time
import adafruit_mma8451
import ulab.numpy as np
from analogio import AnalogIn
i2c = board.I2C()
sensor = adafruit_mma8451.MMA8451(i2c)
analog_in = AnalogIn(board.A1)

maze = [
    "##########",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "##########"
]

maze = [
    "##########",
    "#        #",
    "#        #",
    "#####    #",
    "#        #",
    "#        #",
    "#     ####",
    "#        #",
    "#       X#",
    "##########"
]

# Player's initial position
player_x = 1
player_y = 1
goal_flag = False
sens = 5

def main():
    while True:
        printer(sensor.acceleration)
        time.sleep(0.25)
        """
        roll, pitch, yaw = comp_average(5)  # Get the Euler angles
        define_sens()
        move_player(roll, pitch)
        if goal_flag == False:
            print_maze()
            time.sleep(0.25)
            print("\n"*10)
        else:
            break
        """
def print_maze():
    for y in range(len(maze)):
        row = ""
        for x in range(len(maze[0])):
            if x == player_x and y == player_y:
                row += "O"
            else:
                row += maze[y][x]
        print(row)

def move_player(roll, pitch):
    global player_x, player_y, goal_flag

    # Convert roll and pitch into movement directions
    if pitch < -sens:  # Move up
        new_y = player_y - 1
        if maze[new_y][player_x] in " X":
            player_y = new_y
    elif pitch > sens:  # Move down
        new_y = player_y + 1
        if maze[new_y][player_x] in " X":
            player_y = new_y
    if roll < -sens:  # Move left
        new_x = player_x - 1
        if maze[player_y][new_x] in " X":
            player_x = new_x
    elif roll > sens:  # Move right
        new_x = player_x + 1
        if maze[player_y][new_x] in " X":
            player_x = new_x

    # Check if the player has reached the goal
    if maze[player_y][player_x] == "X":
        print("Congratulations! You've reached the goal!")
        goal_flag = True

def define_sens():
    global sens
    sens = (45 * ((61761 - analog_in.value) / 61761))

def convert_g(accels):
    gees = [x/9.8 for x in accels]
    return gees

def inclination(gees):
    try:
        theta = rad2deg(np.atan(gees[0] / np.sqrt(gees[1]**2 + gees[2]**2)))
        psi = rad2deg(np.atan(gees[1] / np.sqrt(gees[0]**2 + gees[2]**2)))
        phi = rad2deg(np.atan(np.sqrt(gees[0]**2 + gees[1]**2) / gees[2]))
    except:
        theta = 0
        psi = 0
        phi = 0
    return (theta, psi, phi)

def euler(inc):
    return (round(inc[1])+7,round(inc[0])-2,0)

def rad2deg(rad):
    return(rad*(180/np.pi))

def end2end(val):
    return (euler(inclination(convert_g(val))))

def printer(val):
    print(inclination(convert_g(val)))

def comp_average(num):
    cumsum = np.array((0,0,0))
    for n in range(num):
        cumsum = cumsum + np.array(end2end(sensor.acceleration))
    ave = [round(x/num) for x in cumsum]
    return ave

if __name__ == '__main__':
    main()


