# Web-Automation-Template

This is a template showing how to automate web actions using Python and Selenium, or using the default WebView on Android.

The scripts and the app both open the Google home page and search for "`test search`".

---

## Links
* [This repository](https://github.com/dpet23/Web-Automation-Template)
* [Latest release](../../releases/latest)

---

## Requirements
* Python scripts:
  * Python 3
  * `Requests` module
  * `Selenium` module
  * Browser driver on `PATH`
* Android app:
  * Permission to access the internet
  * The installation of apps from unknown sources is allowed

---

## Running the Python scripts
1. Install [Python 3](https://www.python.org/downloads/) and `pip`.
1. Install the [Requests](https://pypi.python.org/pypi/requests) and [Selenium](https://pypi.python.org/pypi/selenium) Python modules. This can be done using the `requirements.txt` file:
    ~~~~
    pip install -r ./requirements.txt
    ~~~~
1. If running the UI automation script, install the appropriate browser (Firefox or Chrome).
1. Download the appropriate browser driver ([`Geckodriver`](https://github.com/mozilla/geckodriver/releases) for Firefox, [`Chromedriver`](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Chrome, or [`PhantomJS`](http://phantomjs.org/download.html)) and add it to the `PATH`.
1. Run the Python script.

---

## Running the Android app
* An Android Package (APK) file is provided in the release. This can be installed on any Android device running Android 4.4 or above.
* Allowing the installation of apps from unknown sources may be necessary.
