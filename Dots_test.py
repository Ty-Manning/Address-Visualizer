import folium
import geopandas as gpd

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

# Read geocode cache
geocode_cache = read_geocode_cache('geocode_cache.txt')

# Load US states shapefile (ensure you have the shapefile in the specified path)
shapefile_path = "/home/kali/Desktop/Addresses/map_data/ne_10m_admin_1_states_provinces.shp"
print(f"Loading US states shapefile from {shapefile_path}")
us_states = gpd.read_file(shapefile_path)

# Create a folium map centered in the US
m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)  # Increased zoom level for better visualization

# Add cached addresses to the map as red dots
for address, (lng, lat) in geocode_cache.items():
    folium.Marker(location=[lat, lng], icon=folium.Icon(color='red')).add_to(m)

# Save map to an HTML file
output_file = "cached_addresses_map.html"
print(f"Saving map to {output_file}")
m.save(output_file)

print("Map saved successfully.")
