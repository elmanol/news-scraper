import requests
from bs4 import BeautifulSoup
import pandas as pd
from news_sources import news_sources  # Import the news source configurations

def scrape_headlines(name, url, find_all_args):
    """
    Fetches the webpage and scrapes the headlines using Beautiful Soup.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = []
        for item in soup.find_all(**find_all_args):
            headline = item.get_text(strip=True)
            link = item.find_parent('a')['href'] if item.find_parent('a') else ''
            
            # Convert relative URLs to absolute URLs
            if link and not link.startswith('http'):
                link = f"{url}{link}" if url.endswith('/') else f"{url}/{link}"

            headlines.append({'Name': name, 'Headline': headline, 'Link': link})

        return headlines
    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []  # Return empty list if an error occurs

# Main loop to scrape headlines from multiple news sources
all_headlines = []

for source in news_sources:
    print(f"Scraping headlines from {source['name']}...")
    headlines = scrape_headlines(source['name'], source['url'], source['find_all_args'])
    all_headlines.extend(headlines)

# Save all scraped headlines to CSV
df = pd.DataFrame(all_headlines)
df.to_csv('news_headlines.csv', index=False)

print("Headlines from multiple sources saved to 'news_headlines.csv'.")