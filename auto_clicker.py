import time
from pynput.keyboard import Controller, Key

def auto_clicker(interval=0.5, repetitions=10):
    """
    Automatically presses the right arrow key at a specified interval.

    :param interval: Time in seconds between each key press
    :param repetitions: Number of times the key is pressed
    """
    keyboard = Controller()
    print("Starting auto clicker...")
    time.sleep(3)  # Give the user time to switch to the desired application

    for i in range(repetitions):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        print(f"Pressed right arrow {i + 1}/{repetitions}")
        time.sleep(interval)
    
    print("Auto clicker finished!")

# Parameters: interval between clicks in seconds, and the number of repetitions
auto_clicker(interval=0.5, repetitions=20)