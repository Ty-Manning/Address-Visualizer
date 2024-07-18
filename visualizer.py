from opencage.geocoder import OpenCageGeocode
import folium

# Your OpenCage API key
api_key = 'XXX'

# Function to read geocode cache from file
def read_geocode_cache(filename):
    cache = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    parts = line.strip().split('\t')
                    if len(parts) == 3:
                        address, lng, lat = parts
                        cache[address] = (float(lng), float(lat))
        print(f"Read {len(cache)} cached geocodes from {filename}")
    except FileNotFoundError:
        print(f"Cache file {filename} not found. Starting with empty cache.")
    except Exception as e:
        print(f"Error reading cache file {filename}: {str(e)}")
    return cache

# Function to write geocode result to cache file
def write_geocode_cache(filename, address, lng, lat):
    with open(filename, 'a') as file:
        file.write(f"{address}\t{lng}\t{lat}\n")
    print(f"Added '{address}' to cache")

# Function to Check cache and geocode
def geocode_address(address, geocoder, cache, cache_filename):
    if address in cache:
        lng, lat = cache[address]
        print(f"Using cached coordinates for '{address}': ({lng}, {lat})")
        return (lng, lat)
    else:
        print(f"Geocoding address: {address}")
        try:
            result = geocoder.geocode(address)
            if result and len(result):
                location = result[0]['geometry']
                lng, lat = location['lng'], location['lat']
                write_geocode_cache(cache_filename, address, lng, lat)  # Cache the result
                print(f"Geocoded address '{address}' to ({lng}, {lat})")
                return (lng, lat)
            else:
                print(f"Address not found: {address}")
                return None
        except Exception as e:
            print(f"Error geocoding address {address}: {str(e)}")
            return None

# Read addresses from address file
with open('addresses.txt', 'r') as file:
    addresses = [line.strip() for line in file if line.strip()]

print(f"Read {len(addresses)} addresses from file.")

# create geocoder instance
geocoder = OpenCageGeocode(api_key)

# Read geocode cache
geocode_cache = read_geocode_cache('geocode_cache.txt')

# Create a folium map centered somewhere in the US
m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)  # i have Increased zoom level for better visualization

# Add addresses to the map as red dots and draw circles (optional)
for address in addresses:
    if address not in geocode_cache:
        lng, lat = geocode_address(address, geocoder, geocode_cache, 'geocode_cache.txt')
        if lng is not None and lat is not None:
            geocode_cache[address] = (lng, lat)

    if address in geocode_cache:
        lng, lat = geocode_cache[address]
        folium.Marker(location=[lat, lng], icon=folium.Icon(color='red')).add_to(m)
        folium.Circle(
            location=[lat, lng],
            radius=96560,  # 60 miles in meters
            color='orange',
            fill=True,
            fill_color='orange',
            fill_opacity=0.05
        ).add_to(m)

# Save map to an HTML file
output_file = "us_coverage_map_with_circles_and_caching.html"
print(f"Saving map to {output_file}")
m.save(output_file)

print("Map saved successfully.")
