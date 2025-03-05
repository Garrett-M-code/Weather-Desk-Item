#    A program that displays weather data from NWS on a desk item.
#    Copyright (C) 2025  Garrett Moore
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import json
import time
import requests


MINUTE = 60
HOUR = MINUTE * 60

def get_date():
	"""A function to query the current date"""
	#TODO: Add location based time
	return time.strftime("%a %B %d, %Y")

def get_time():
	"""A function to query the current time"""
	#TODO: Add location based time
	current_time = time.strftime("%I:%M %p")
	return current_time
	
def get_correct_station(longitude, latitude):
	"""A function to get the correct weather station link for specific coordinate grids"""
	
	# Converts the floats into a string with 4 decimal places
	longitude = str("{:.4f}".format(longitude))
	latitude = str("{:.4f}".format(latitude))
	
	# Formats the URL for the specific coordinates
	url = "https://api.weather.gov/points/" + longitude + "," + latitude
	
	response = requests.get(url, stream=True)
	
	with open("data.csv", 'wb') as file:
    		for chunk in response.iter_content(chunk_size=8192):
      			file.write(chunk)
	
	print(response)
	
	return True
	
def current_forecast(hourly_forecast_link):
	"""A function to query the hourly forecast"""
	
	#TODO: Get NWS weather forecast
	
	#sunrise = specific time
	#sunset = specific time
	#windspeed = specific time
	
	
	
	projected_forecast = [[0.00], [0.00], [0.00], [0.00], [0.00], [0.00], [0.00]]
	return projected_forecast

city_1 = {
	"Name": "Atlanta",
	"Longitude": 000,
	"Latitude": 000
}

city_2 = {
	"Name": "New York",
	"Longitude": 000,
	"Latitude": 000
}


# Grabs the weather forcast on start-up
get_correct_station(39.7456, -97.0892)

# Main loop of the program dealing with updating all information
while True:
	# Represents the start of the day
	print(get_date())	
	
	# Loop to update the current time
	for i in range(0, HOUR * MINUTE):
		if (get_time() == "00:00"):
			print("The date is " + get_date())
		
		print(get_time())
		
		time.sleep(MINUTE)
	
	
	
	
	
	
	
	


