import logging
import pyautogui
import os
import time
import keyboard

def setup_logger(log_file):
    """
    Sets up the logger configuration.
    """
    logging.basicConfig(
        filename=log_file,
        filemode='w',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logging.info("Logger initialized.")

def take_screenshot(filename):
    """
    Takes a screenshot and saves it to the reports folder.
    """
    filepath = os.path.join("reports", filename)
    pyautogui.screenshot(filepath)
    logging.info(f"Screenshot saved: {filepath}")

def capture_coordinates():
    """
    Captures the current mouse position and returns it as (x, y).
    Waits for the user to press 'Enter' to capture the position.
    """
    print("Position your mouse over the target element and press 'Enter' to capture its coordinates...")
    keyboard.wait('enter')
    
    # Get the current mouse position
    x, y = pyautogui.position()
    print(f"Captured position: ({x}, {y})")
    logging.info(f"Captured mouse coordinates: ({x}, {y})")
    
    return x, y