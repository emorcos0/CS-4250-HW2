#-------------------------------------------------------------------------
# AUTHOR: Edward Morcos
# FILENAME: scraper.py
# SPECIFICATION: Crawls the circular links section of TestingURL.dev starting from the seed URL. 
# For each crawled page, parse the retrieved HTML using BeautifulSoup and print the text contained in its <h1> element.
# Extract all hyperlinks contained in <a> tags. Convert relative URLs to absolute URLs before processing them.
# Print all URLs contained in seen.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 70 minutes
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]
seen = set()


# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    current_url = frontier.pop(0)

    # If url has already been seen, skip it
    if current_url in seen:
        continue
    seen.add(current_url)


    # Retrieving and parsing the Web page
    response = requests.get(current_url)
    soup = BeautifulSoup(response.text, "html.parser")


    # Printing the text contained in the <h1> element
    h1 = soup.find("h1")
    if h1 is not None:
        print(h1.get_text(strip=True))


    # Extracting and processing hyperlinks
    # <a> tags contain hyperlinks in the href attribute
    for link in soup.find_all("a"):
        href = link.get("href")
        if href is None:
            continue

        
        # Converting relative URLs to absolute URLs
        absolute_url = baseURL + href

        # Adding the absolute URL to the frontier if it has not been seen or added before
        if absolute_url.startswith(seed):
            if absolute_url not in seen and absolute_url not in frontier:
                frontier.append(absolute_url)


# Printing all URLs in seen
for url in seen:
    print(url)