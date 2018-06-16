# Web-Automation-Template

This is a template showing how to automate web actions using Python and Selenium, or using the default WebView on Android.

The script and the app both open the Google home page and search for "`test search`".

---

## Links
* [This repository](https://github.com/dpet23/Web-Automation-Template)
* [Latest release](../../releases/latest)

---

## Requirements
* Python script:
  * Python 3
  * `Requests` module
  * `Selenium` module
  * Firefox or Chrome browser
  * Browser driver on `PATH`
* Android app:
  * Permission to access the internet
  * The installation of apps from unknown sources is allowed

---

## Running the Python script
1. Install [Python 3](https://www.python.org/downloads/) and `pip`
1. Install the [Requests](https://pypi.python.org/pypi/requests) and [Selenium](https://pypi.python.org/pypi/selenium) Python modules. This can be done using the `requirements.txt` file:
    ~~~~
    pip install -r ./requirements.txt
    ~~~~
1. Install the appropriate browser (Firefox or Chrome)
1. Download the appropriate browser driver (`Geckodriver` for Firefox or `Chromedriver` for Chrome) from [SeleniumHQ](http://www.seleniumhq.org/download/) and add it to the `PATH`
1. Run the Python script

---

## Running the Android app
* An Android Package (APK) file is provided in the release. This can be installed on any Android device running Android 4.4 or above.
* Allowing the installation of apps from unknown sources may be necessary.
