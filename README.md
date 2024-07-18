# US Coverage Map Visualization

## Introduction

This project generates a visualization of US coverage areas based on given addresses using geospatial data and OpenCage API for geocoding. The resulting map highlights areas within a 60-mile radius of each address in blue and areas outside this radius in red.

## Requirements

1. **OpenCage API Key**: Obtain a free API key from [OpenCage](https://opencagedata.com) for geocoding addresses.
   
2. **Addresses File**: Provide a file named `addresses.txt` containing addresses to be geocoded.

## Features

- **Geocoding and Caching**: Addresses are geocoded using OpenCage API. Results are cached in `geocode_cache.txt` to speed up subsequent runs and reduce API calls.
  
- **Map Visualization**: Generates an interactive HTML map (`us_coverage_map.html`) using Folium, highlighting coverage areas within a 60-mile radius of provided addresses.

- **Included Map Data**: Utilizes general US state outlines from [Natural Earth](https://www.naturalearthdata.com) for visualizing state boundaries.

## Usage

1. **Setup**:
   - Obtain an API key from OpenCage and add it to the script (`visualizer.py`).
   - Place addresses in `addresses.txt`.

2. **Execution**:
   - Run `visualizer.py` to geocode addresses, generate coverage areas, and create the map.
   
3. **Output**:
   - The resulting `us_coverage_map.html` will display the coverage areas:
     - shaded polygons for areas within 60 miles of any address.

## Map Data Source

The map data, including US state outlines, is sourced from [Natural Earth](https://www.naturalearthdata.com).

## Credits

This project uses:
- [OpenCage](https://opencagedata.com) for geocoding services.
- [Natural Earth](https://www.naturalearthdata.com) for map data.

## License

This project is licensed under the [MIT License](LICENSE).
