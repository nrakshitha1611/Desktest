import os
import logging
from test_cases import run_all_tests
from utils import setup_logger

# Create the reports directory if not present
if not os.path.exists("reports"):
    os.makedirs("reports")

# Setup the logger for capturing test execution details
setup_logger('reports/gui_test_log.log')

def main():
    logging.info("Starting GUI Testing Framework...")

    # Execute all the test cases defined
    run_all_tests()

    logging.info("All test cases executed successfully!")

if __name__ == "__main__":
    main()