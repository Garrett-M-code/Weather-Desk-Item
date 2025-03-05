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
import os
import time
from datetime import date
import re


minute = 60
hour = minute * 60

def get_date():
	today = date.today()
	return today.strftime("%B %d, %Y")

def get_time():
	current_time = time.strftime("%H:%M")
	return current_time


# Main loop of the program dealing with updating all information
while True:
	# Represents the start of the day
	current_hour = 0
	print(get_date())
	
	# Loop to update the current time
	while current_hour < 24:
		print("The time currently is:")
		
		minutes_passed = 0
		while minutes_passed <= hour * minute:
			print(get_time())
			minutes_passed += 1
			time.sleep(minute)
		
		
		current_hour += 1
	
	


