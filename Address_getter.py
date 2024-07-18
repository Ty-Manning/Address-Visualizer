import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def extract_addresses(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)
    
    # Wait for the relevant content to load
    await page.waitForSelector('div.ml-location.ml-location-map')

    # Get the page content
    content = await page.content()

    # Close the browser
    await browser.close()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find all the relevant div elements
    location_divs = soup.find_all('div', class_='ml-location ml-location-map')

    print(f"Found {len(location_divs)} location divs.")  # Debug print

    addresses = []

    # Iterate over each div and extract the address components
    for i, div in enumerate(location_divs):
        address1 = div.get('data-address1')
        city = div.get('data-city')
        state = div.get('data-state')
        zip_code = div.get('data-zip')

        # Debug prints to check the extracted data
        print(f"Location {i}:")
        print(f"  Address1: {address1}")
        print(f"  City: {city}")
        print(f"  State: {state}")
        print(f"  Zip Code: {zip_code}")

        if address1 and city and state and zip_code:
            full_address = f"{address1}, {city}, {state} {zip_code}"
            addresses.append(full_address)

    # Write addresses to a text file
    with open('addresses.txt', 'w') as f:
        for address in addresses:
            f.write(address + '\n')

    print("Addresses written to addresses.txt")

# URL of the website to scrape
url = 'https://hcahealthcare.com/locations/'  # Replace with the actual URL

# Run the script
asyncio.run(extract_addresses(url))
