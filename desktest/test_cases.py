import pyautogui
import time
import logging
from utils import take_screenshot, capture_coordinates
import pygetwindow as gw

def run_all_tests():
    """
    Run all defined test cases.
    """
    logging.info("Running all test cases...")

    # Run individual test cases with user-defined positions
    # test_button_click()
    # test_text_input()
    test_calculator_addition()
    
    logging.info("All test cases completed.")

def test_button_click():
    """
    Allows the user to define a button click interaction dynamically.
    """
    logging.info("Running test case: Button Click")
    
    try:
        # Prompt the user to specify the position of the button they want to click
        print("Move your mouse to the button you want to test, then press 'Enter'...")
        button_x, button_y = capture_coordinates()  # Capture position dynamically

        # Perform the click using the captured coordinates
        pyautogui.moveTo(button_x, button_y, duration=1)
        # take_screenshot("before_button_click.png")
        pyautogui.click()
        logging.info(f"Clicked button at ({button_x}, {button_y})")
        take_screenshot("after_button_click.png")

    except Exception as e:
        logging.error(f"Error in Button Click Test: {e}")


def test_text_input():
    """
    Allows the user to specify a text field dynamically and input text.
    """
    logging.info("Running test case: Text Input")

    try:
        # Prompt the user to specify the position of the text field
        print("Move your mouse to the text field you want to test, then press 'Enter'...")
        text_x, text_y = capture_coordinates()  # Capture position dynamically

        # Move to the text field and enter some text
        pyautogui.moveTo(text_x, text_y, duration=1)
        pyautogui.click()
        # take_screenshot("before_text_input.png")
        pyautogui.write("Hello World", interval=0.1)  # You can replace "Hello World" with any text
        logging.info(f"Entered text at ({text_x}, {text_y}): Hello World")
        take_screenshot("after_text_input.png")

    except Exception as e:
        logging.error(f"Error in Text Input Test: {e}")

def test_calculator_addition():
    """
    Test case to automate 7 + 3 = 10 calculation in the Calculator application using hardcoded coordinates.
    """
    logging.info("Running test case: Calculator Addition (7 + 3)")

    try:
        # Step 1: Bring the Calculator to the foreground
        calc_window = gw.getWindowsWithTitle('Calculator')[0]  # Look for a window with 'Calculator' in the title
        calc_window.activate()  # Bring the Calculator to the foreground

        # Step 2: Get the Calculator window's position and size
        time.sleep(1)  # Wait for the window to be active
        left, top, width, height = calc_window.left, calc_window.top, calc_window.width, calc_window.height
        logging.info(f"Calculator window position and size - Left: {left}, Top: {top}, Width: {width}, Height: {height}")

        # Step 3: Define button positions relative to the window's top-left corner
        # Adjust these values if the positions differ on your system
        button_7_pos = (left + 231, top + 6241)       # Relative position of button '7'
        button_plus_pos = (left + 637, top + 7501)   # Relative position of button '+'
        button_3_pos = (left + 494, top + 7541)       # Relative position of button '3'
        button_equal_pos = (left + 635, top + 8171)  # Relative position of button '='

        # Step 4: Perform the addition operation using these positions

        # Click on button '7'
        pyautogui.moveTo(button_7_pos, duration=0.5)
        take_screenshot("before_click_7.png")  # Screenshot before clicking '7'
        pyautogui.click()
        logging.info(f"Clicked '7' button at {button_7_pos}")
        take_screenshot("after_click_7.png")  # Screenshot after clicking '7'

        # Click on button '+'
        pyautogui.moveTo(button_plus_pos, duration=0.5)
        take_screenshot("before_click_plus.png")
        pyautogui.click()
        logging.info(f"Clicked '+' button at {button_plus_pos}")
        take_screenshot("after_click_plus.png")

        # Click on button '3'
        pyautogui.moveTo(button_3_pos, duration=0.5)
        take_screenshot("before_click_3.png")
        pyautogui.click()
        logging.info(f"Clicked '3' button at {button_3_pos}")
        take_screenshot("after_click_3.png")

        # Click on button '='
        pyautogui.moveTo(button_equal_pos, duration=0.5)
        take_screenshot("before_click_equal.png")
        pyautogui.click()
        logging.info(f"Clicked '=' button at {button_equal_pos}")
        take_screenshot("after_click_equal.png")

        logging.info("Calculator addition operation (7 + 3) executed successfully!")

    except Exception as e:
        logging.error(f"Error in Calculator Addition Test: {e}")