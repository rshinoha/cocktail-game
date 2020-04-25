# Ryoh Shinohara
# get-all-id.py
# ===================================================================
# This script parses the CocktailDB drinks objects to obtain all
# unique IDs found in the database. To prevent overusage, the script
# takes a short break after each call as well as an extended break
# after 5 API calls. It also will only run until a given time of day.

from random import randrange
from time import sleep
from datetime import datetime
import requests

# First ID in CocktailDB
FIRST_ID = '11000'
# Script stops after MAX_NULL_COUNT under the assumption that there
# are no more drinks in the database
MAX_NULL_COUNT = 5
# Number of non-null objects the script reads before extended break
NUM_NON_NULL_READ = 5
# Minimum number of Seconds the script sleeps in between calls where
# drinks object is null
WAIT_BETWEEN_NULLS = 5
# Minimum number of seconds the script sleeps after a non-null drinks
# object is found
MIN_SEC = 10
# Minimum number of minutes the script sleeps after 
MIN_MIN = 5
# Hour of day where we stop script (in military time)
END_TIME = 21
# Randrange stopping criteria to add on to sleep time
RAND_STOP = 11
# File that contains last ID checked
LAST_ID_FILE = 'last-id.txt'
# File containing all IDs
ALL_ID_FILE = 'all-id-list.csv'
# API call URL
CALL_URL = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}"

# Current id
cur_id = ''
# Temporary list of IDs to add to ALL_ID_FILE during extended break
id_list = []
# Counter for checking number of consecutive null drinks object
null_count = 0
# Counter for checking number of non-null drinks object IDs read
# before extended break
count = 0
# Current hour of the day
cur_hour = datetime.now().hour

# Opens last-id.txt to find last id checked by script
# If empty, assumes that we need to start on 11000
with open(LAST_ID_FILE, 'r') as reader:
    temp_str = reader.read()
    if temp_str == '':
        cur_id = FIRST_ID
    else:
        cur_id = temp_str

# Loop stops if one of these conditions are fulfilled:
# * When the number of consecutive drinks object with drinks set as
# null exceeds MAX_NULL_COUNT
# * When current hour exceeds END_TIME
while null_count < MAX_NULL_COUNT and cur_hour < END_TIME:
    # Saves response received from API request
    response = requests.get(CALL_URL.format(cur_id))
    print(datetime.now())
    if response.json()['drinks'] is None:
        null_count += 1
        sleep(WAIT_BETWEEN_NULLS + randrange(RAND_STOP))
    else:
        count += 1
        id_list.append(response.json()['drinks'][0]['idDrink'])
        sleep(MIN_SEC + randrange(RAND_STOP))
        print(id_list)
    print(datetime.now())

    break

