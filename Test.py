from geopy.geocoders import Nominatim

# Test a single address
address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
geolocator = Nominatim(user_agent="geoapiExercises")

try:
    location = geolocator.geocode(address)
    if location:
        print(f"Address: {address}")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    else:
        print(f"Failed to geocode address: {address}")
except Exception as e:
    print(f"Error geocoding address {address}: {str(e)}")
