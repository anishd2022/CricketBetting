# import libraries
import requests  # For making HTTP requests
import json  # For handling JSON responses


# save API key:
API_Key = "752f772f-7a59-4f14-b066-d1921a4f2c64"  # this is a one week trial key


# function to make get requests and return JSON response:
def make_request_and_return_response(url):
    response = requests.get(url)  # Make the GET request
    if response.status_code == 200:  # Check if the request was successful
        return response.json()  # Return the JSON response
    else:
        return f"Error: {response.status_code}, {response.text}"  # Return an error message


# Function to get the list of sports names
def list_all_sports():
    url = f"https://api.opticodds.com/api/v3/sports?key={API_Key}"
    return make_request_and_return_response(url)

# sports = list_all_sports()
# print(json.dumps(sports, indent=2))


# Function to get list of sports books:
def list_all_sportsbooks():
    url = f"https://api.opticodds.com/api/v3/sportsbooks?key={API_Key}"
    return make_request_and_return_response(url)

# sportsbooks = list_all_sportsbooks()
# print(json.dumps(sportsbooks, indent=2))


# Function to get all live fixtures for a given sport:
def list_live_fixtures(sport_name):
    url = f"https://api.opticodds.com/api/v3/fixtures/active?key={API_Key}&sport={sport_name}"
    return make_request_and_return_response(url)

# fixtures = list_live_fixtures("cricket")
# print(json.dumps(fixtures, indent=2))
        
        
# Function to get live odds for a given fixture / game:
    # ODDS_FORMAT: Needs to be one of the following (AMERICAN, DECIMAL, PROBABILITY, MALAY, HONG_KONG, INDONESIAN). This defaults to AMERICAN.
    # sportsbooks that cover cricket are typically "1xbet" and "bet365"
def get_live_odds_for_specific_game(game_ID, sportsbook, odds_format="AMERICAN"):
    url = f"https://api.opticodds.com/api/v3/fixtures/odds?key={API_Key}&fixture_id={game_ID}&odds_format={odds_format}&sportsbook={sportsbook}"
    return make_request_and_return_response(url)

# live_odds = get_live_odds_for_specific_game("2025022818E291B5", "bet365")
# print(json.dumps(live_odds, indent=2))


# Function to get historical odds for a given fixture / game:
def get_historical_odds_for_specific_game(game_ID, sportsbook="1xbet", odds_format="AMERICAN"):
    url = f"https://api.opticodds.com/api/v3/fixtures/odds/historical?key={API_Key}&fixture_id={game_ID}&sportsbook={sportsbook}&odds_format={odds_format}"
    return make_request_and_return_response(url)

# historical_odds = get_historical_odds_for_specific_game("2025022662FAA85C")
# print(json.dumps(historical_odds, indent=2))


# Function to list all historical fixtures for a specific sport within a given time frame:
    #  Start and end time follow ISO 8601 convention: ex: 2025-02-23T00:00:00Z
def list_historical_fixtures_within_given_time_frame(sport_name, start_time, end_time):
    url = f"https://api.opticodds.com/api/v3/fixtures?key={API_Key}&sport={sport_name}&start_date_after={start_time}&start_date_before={end_time}"
    return make_request_and_return_response(url)

# historical_fixtures = list_historical_fixtures_within_given_time_frame("cricket", "2025-02-23T00:00:00Z", "2025-02-27T00:00:00Z")
# print(json.dumps(historical_fixtures, indent=2))


# Function to get time_series historical odds for a specific fixture / game:
# this function returns null because they may not have timeseries data for cricket (check with OpticOdds people)
def get_timeseries_historical_odds_for_specific_game(game_ID, sportsbook="1xbet"):
    url = f"https://api.opticodds.com/api/v3/fixtures/odds/historical?key={API_Key}&sportsbook={sportsbook}&fixture_id={game_ID}&include_timeseries=True"
    return make_request_and_return_response(url)

