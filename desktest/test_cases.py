import pyautogui
import time
import logging
from utils import take_screenshot, capture_coordinates

def run_all_tests():
    """
    Run all defined test cases.
    """
    logging.info("Running all test cases...")

    # Run individual test cases with user-defined positions
    test_button_click()
    test_text_input()
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
    Test case to perform an addition operation in the Windows Calculator.
    """
    logging.info("Running test case: Calculator Addition")

    try:
        # Prompt user to move to the '7' button and press Enter
        print("Move your mouse to the '7' button and press Enter...")
        seven_x, seven_y = capture_coordinates()

        # Prompt user to move to the '+' button and press Enter
        print("Move your mouse to the '+' button and press Enter...")
        plus_x, plus_y = capture_coordinates()

        # Prompt user to move to the '3' button and press Enter
        print("Move your mouse to the '3' button and press Enter...")
        three_x, three_y = capture_coordinates()

        # Prompt user to move to the '=' button and press Enter
        print("Move your mouse to the '=' button and press Enter...")
        equal_x, equal_y = capture_coordinates()

        # Move and click the '7' button
        pyautogui.moveTo(seven_x, seven_y, duration=1)
        take_screenshot("before_click_7.png")
        pyautogui.click()
        logging.info("Clicked '7' button")
        take_screenshot("after_click_7.png")

        # Move and click the '+' button
        pyautogui.moveTo(plus_x, plus_y, duration=1)
        take_screenshot("before_click_plus.png")
        pyautogui.click()
        logging.info("Clicked '+' button")
        take_screenshot("after_click_plus.png")

        # Move and click the '3' button
        pyautogui.moveTo(three_x, three_y, duration=1)
        take_screenshot("before_click_3.png")
        pyautogui.click()
        logging.info("Clicked '3' button")
        take_screenshot("after_click_3.png")

        # Move and click the '=' button
        pyautogui.moveTo(equal_x, equal_y, duration=1)
        take_screenshot("before_click_equal.png")
        pyautogui.click()
        logging.info("Clicked '=' button")
        take_screenshot("after_click_equal.png")

        logging.info("Calculator addition operation executed successfully!")

    except Exception as e:
        logging.error(f"Error in Calculator Addition Test: {e}")

