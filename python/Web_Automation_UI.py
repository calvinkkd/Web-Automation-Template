#!/usr/bin/env python3


# Imports
from common import main, getUseragents
from selenium import webdriver

# The browser to use
BROWSER = "Firefox"

# Get list of useragents to use
useragents = getUseragents()


def setUpWebdriver(browser, agent):
    """Set up the webdriver that will be used for the automation."""

    if (browser == "Firefox"):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", agent)
        driver = webdriver.Firefox(firefox_profile=profile)
    elif (browser == "Chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-agent '" + agent + "'")
        driver = webdriver.Chrome(chrome_options=options)
    else:
        print()
        raise TypeError("ERROR - unknown browser:", browser)
    
    return driver


if __name__ == '__main__':
    for useragent in useragents:
        driver = setUpWebdriver(BROWSER, useragent[0])
        main(driver, BROWSER, useragent)
