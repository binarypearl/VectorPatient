from anki_vector.util import degrees, distance_mm, speed_mmps
import anki_vector
import time
import daemon

if __name__ == '__main__':
    robot.say_text("I am Vector and Im going to move in a square and wait patiently!", duration_scalar=0.8)

    # Use a "for loop" to repeat the indented code 4 times
    # Note: the _ variable name can be used when you don't need the value
    for _ in range(4):
        print("Drive Vector straight...")
        robot.behavior.drive_straight(distance_mm(200), speed_mmps(50))

        print("Turn Vector in place...")
        robot.behavior.turn_in_place(degrees(90))

