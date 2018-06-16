#!/usr/bin/env python3


# Imports
import sys
import time
import random
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Main URL to go to
URL = "https://www.google.com"

# Term to search for
SEARCH_TERM = "test search"

# Max amount of time to wait (in seconds) for a page to load
DEFAULT_WAIT = 10

# Pretend to be Edge 41 on a Samsung Galaxy S8+ phone
USERAGENTS = [  # [useragent, platform]
                ['Mozilla/5.0 (Linux; Android 7.0; SM-G955F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 EdgA/41.0.0.1561', 'mobile'],
             ]


def getUseragents():
    """Return the list of useragents."""
    return USERAGENTS


def _isDesktopAgent(useragent):
    """Determines if the current useragent is a desktop or mobile browser."""
    return (useragent[1] == 'desktop')


def _wait_explicit(driver, maxSecs, condition):
    """
    Waits a certain number of seconds until a condition is satisfied.
    :driver:    The webdriver used to automate a webpage.
    :maxSecs:   The maximum number of seconds to wait.
    :condition: The condition to be satisfied.
    """
    try:
        WebDriverWait(driver, maxSecs).until(condition)
        time.sleep(1)
        print()
    except TimeoutException:
        print()
        print("ERROR: Page not loaded correctly after", maxSecs, "seconds.")
        print()
        driver.quit()
        exit()


def _wait_implicit(secs):
    """
    Waits a certain number of seconds and prints the number of seconds left.
    :secs: The number of seconds to wait.
    """
    _write("\t" + "( ")
    for i in range(secs, 0, -1):
        _write(str(i) + ' ')
        time.sleep(1)
    _write(")")
    print()


def _write(text):
    """
    Print text without a newline at the end.
    :text: The text to print.
    """
    sys.stdout.write(text)
    sys.stdout.flush()


def main(driver, browser, useragent):
    """
    Runs the browser automation.
    :driver:    The webdriver to use for the automation.
    :browser:   The name of the web browser being used by the driver.
    :useragent: The current useragent of the driver, as a list of [useragent, platform].
    """

    # Check if URL can be opened
    r = requests.get(URL)
    if r.status_code == 200:
        desktop = _isDesktopAgent(useragent)

        # Print status
        print()
        print("Opening browser (" + browser + ", " + useragent[1] + ")")
        print("\t" + useragent[0])
        print()

        # Open URL
        _write("Navigating to " + URL)
        driver.get(URL)
        _wait_explicit(driver, DEFAULT_WAIT, EC.title_contains("Google"))
        print("Window title:", driver.title)
        assert "Google" in driver.title

        # Perform a search
        print()
        print("Performing a search")
        if desktop:
            searchBox = driver.find_element_by_id("lst-ib")
            searchButton = driver.find_element_by_name("btnK")
        else:
            searchBox = driver.find_element_by_name("q")
            searchButton = driver.find_element_by_class_name("Tg7LZd")
        searchBox.send_keys(SEARCH_TERM)
        searchButton.click()

        # Wait
        _write("Waiting")
        _wait_implicit(random.randrange(15,30))
        print("Window title:", driver.title)
        assert SEARCH_TERM in driver.title
        
        # Close browser
        print()
        print("Closing the", useragent[1], browser, "browser")
        driver.close()
    else:
        # If URL can't be opened, print status code
        print("Can't open", URL)
        print("Status code:", r.status_code)
        exit()
    
    # End script
    print()
    print("Finished.")


if __name__ == '__main__':
    # Don't run this script by itself.
    errorMessage = "This script contains helper methods, and should not be run by itself. Please run the `Web_Automation` scripts."
    raise Exception(errorMessage)
