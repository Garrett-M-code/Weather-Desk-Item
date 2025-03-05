#    A program that displays weather data from NWS on a desk item.
#    Copyright (C) <year>  <name of author>
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


MINUTE = 60
HOUR = MINUTE * 60

def get_date():
	"""A method to query the current date"""
	return time.strftime("%a %B %d, %Y")

def get_time():
	"""A method to query the current time"""
	current_time = time.strftime("%I:%M %p")
	return current_time
	
def current_forecast(longitude, latitude):
	"""A method to query the hourly forecast"""
	
	city_1_forecast = [[0.00], [0.00], [0.00], [0.00], [0.00], [0.00], [0.00]]
	city_2_forecast = [[0.00], [0.00], [0.00], [0.00], [0.00], [0.00], [0.00]]
	
	projected_forecast = [city_1_forecast, city_2_forecast]
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
	
	
	
	
	
	
	
	


