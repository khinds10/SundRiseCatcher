#!/usr/bin/python
# Kevin Hinds http://www.kevinhinds.com
# License: GPL 2.0

# forecast.io API key for local weather information
weatherAPIURL = 'https://api.forecast.io/forecast/'
weatherAPIKey = 'YOUR FORECAST.IO KEY HERE'

# digole display driver settings
projectFolder = '/home/pi/'
digoleDriverFolder = projectFolder + 'display/'
digoleDriverEXE = digoleDriverFolder + "display"

# capture image settings
basewidth = 160
hsize = 128

# optional for running the remote sunrise logger
deviceLoggerAPI = 'YOUR API URL'

# search google to get the Latitude/Longitude for your home location
latitude = 42.4152778
longitude = -71.1569444