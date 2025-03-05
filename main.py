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
from datetime import date


MINUTE = 60
HOUR = MINUTE * 60

def get_date():
	"""A method to query the current date"""
	today = date.today()
	return today.strftime("%B %d, %Y")

def get_time():
	"""A method to query the current time"""
	current_time = time.strftime("%H:%M")
	return current_time
	
def current_forecast(longitude, latitude):
	"""A method to query the hourly forecast"""
	projected_forecast = [[0.00], [0.00], [0.00], [0.00], [0.00], [0.00], [0.00]]
	return projected_forecast


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
	
	
	
	
	
	
	
	


