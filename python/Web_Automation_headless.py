#!/usr/bin/env python3


# Imports
from common import main, getUseragents
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# The browser to use
BROWSER = "PhantomJS"

# Get list of useragents to use
useragents = getUseragents()


def setUpWebdriver(browser, agent):
    """Set up the webdriver that will be used for the automation."""
    
    if (browser == "PhantomJS"):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = agent
        return webdriver.PhantomJS(desired_capabilities=dcap)
    else:
        print()
        raise TypeError("ERROR - unknown browser:", browser)


if __name__ == '__main__':
    for useragent in useragents:
        driver = setUpWebdriver(BROWSER, useragent[0])
        main(driver, BROWSER, useragent)
