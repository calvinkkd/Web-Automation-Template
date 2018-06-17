#!/usr/bin/env python3


# Imports
from common import main, getUseragents
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# The browser to use
BROWSER = "Firefox"

# Get list of useragents to use
useragents = getUseragents()


def setUpWebdriver(browser, agent):
    """Set up the webdriver that will be used for the automation."""

    if (browser == "Firefox"):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", agent)
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
    elif (browser == "Chrome"):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-agent='" + agent + "'")
        options.add_argument('--disable-gpu')   # needed only on Windows
        options.set_headless(headless=True)
        driver = webdriver.Chrome(chrome_options=options)
    elif (browser == "PhantomJS"):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = agent
        driver = webdriver.PhantomJS(desired_capabilities=dcap)
    else:
        print()
        raise TypeError("ERROR - unknown browser:", browser)
    
    return driver


if __name__ == '__main__':
    for useragent in useragents:
        driver = setUpWebdriver(BROWSER, useragent[0])
        main(driver, BROWSER, useragent)
