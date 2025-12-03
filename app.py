from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import time
import os

# Initialize Flask App
# static_folder='.' allows serving index.html from the same directory
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

# --- CONFIGURATION ---
# Replace with your actual keys or set them as environment variables
API_KEY = os.environ.get('WEATHER_API_KEY', '6c52cf1143b14faab16172745251110')

WEATHER_API_URL = 'https://api.weatherapi.com/v1/forecast.json'
CACHE_DURATION_SECONDS = 15 * 60  # 15 minutes

# In-memory cache to reduce API usage
weather_cache = {}

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Fetches weather data. 
    Checks cache -> Fetches from API -> Updates Cache -> Returns Data.
    """
    location = request.args.get('location')
    aqi = request.args.get('aqi', 'no')
    alerts = request.args.get('alerts', 'no')
    
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400
    
    # Unique cache key
    cache_key = f"{location.lower()}_{aqi}_{alerts}"

    # Check cache
    current_time = time.time()
    if cache_key in weather_cache:
        cached_entry = weather_cache[cache_key]
        if current_time - cached_entry['timestamp'] < CACHE_DURATION_SECONDS:
            print(f"Returning cached data for {location}")
            return jsonify(cached_entry['data'])

    # Fetch from API
    print(f"Fetching new data for {location}")
    params = {
        'key': API_KEY,
        'q': location,
        'days': 7,
        'aqi': aqi,
        'alerts': alerts
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        # Update cache
        weather_cache[cache_key] = {
            'data': data,
            'timestamp': current_time
        }
        
        return jsonify(data)

    except requests.exceptions.HTTPError as http_err:
        try:
            # Try to parse the WeatherAPI error message
            error_data = response.json()
            error_msg = error_data.get('error', {}).get('message', str(http_err))
        except:
            error_msg = str(http_err)
        return jsonify({"error": f"API Error: {error_msg}"}), response.status_code
        
    except requests.exceptions.RequestException as req_err:
        return jsonify({"error": f"Network Error: {req_err}"}), 503
    except Exception as e:
        return jsonify({"error": f"Server Error: {str(e)}"}), 500

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    print(f"Starting server on port 5000...")
    print(f"Weather API Key configured: {'Yes' if API_KEY else 'No'}")
    app.run(debug=True, port=5000)