#!/usr/bin/env python3


import sys
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Main URL to go to
URL = "https://www.google.com"

# The browser to use
BROWSER = "Firefox"

# Pretend to be Edge 41 on a Samsung Galaxy S8+ phone
USERAGENTS = [  # [useragent, platform]
                ['Mozilla/5.0 (Linux; Android 7.0; SM-G955F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36 EdgA/41.0.0.1561', 'mobile'],
             ]


def wait(secs):
    """
    Waits a certain number of seconds and prints the number of seconds left.
    :secs: The number of seconds to wait.
    """
    write("( ")
    for i in range(secs, 0, -1):
        write(str(i) + ' ')
        time.sleep(1)
    write(")")
    print()


def write(text):
    """
    Print text without a newline at the end.
    :text: The text to print.
    """
    sys.stdout.write(text)
    sys.stdout.flush()


def main():
    # Check if URL can be opened
    r = requests.get(URL)
    if r.status_code == 200:

        for useragent in USERAGENTS:
            # Get useragent and platform
            agent = useragent[0]
            if (useragent[1] == 'desktop'):
                desktop = True
            else:
                desktop = False

            # Print status
            print()
            print("Opening browser (" + BROWSER + ", " + useragent[1] + ")")
            print("\t" + agent)
            print()
            
            # Set up browser
            if (BROWSER == "Firefox"):
                profile = webdriver.FirefoxProfile()
                profile.set_preference("general.useragent.override", agent)
                driver = webdriver.Firefox(firefox_profile=profile)
            elif (BROWSER == "Chrome"):
                options = webdriver.ChromeOptions()
                options.add_argument("--user-agent '" + agent + "'")
                driver = webdriver.Chrome(chrome_options=options)
            else:
                print()
                raise TypeError("ERROR - unknown browser:", BROWSER)
            time.sleep(1)

            # Open URL
            write("Navigating to " + URL + "\t")
            driver.get(URL)
            wait(5)

            # Perform a search
            print("Performing a search")
            if desktop:
                searchBox = driver.find_element_by_id("lst-ib")
                searchButton = driver.find_element_by_name("btnK")
            else:
                searchBox = driver.find_element_by_name("q")
                searchButton = driver.find_element_by_id("tsbb")
            searchBox.send_keys("test search")
            searchButton.click()

            # Wait
            write("Waiting" + "\t")
            wait(random.randrange(15,30))
            
            # Close browser
            print()
            print("Closing the", useragent[1], BROWSER, "browser")
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
    main()
