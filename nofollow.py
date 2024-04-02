import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def scrape_and_check_nofollow(url):
    warnings.simplefilter('ignore', InsecureRequestWarning)

    # Send a GET request to the URL
    response = requests.get(url, verify=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all internal links from the page
        internal_links = [a.get('href') for a in soup.find_all('a', href=True) if urlparse(a['href']).netloc == urlparse(url).netloc]

        # Open the output file in append mode
        with open(output_file, 'a') as file:
            # Iterate through internal links
            for internal_link in internal_links:
                link_soup = BeautifulSoup(internal_link, 'html.parser')
                nofollow_attribute = link_soup.get('rel', [])
                if 'nofollow' in nofollow_attribute:
                    file.write(f'The link {url} => {internal_link} has rel="nofollow" attribute.\n')

        print(f'Results appended to: {output_file}')

    else:
        print(f'Failed to fetch the main page: {url}')

# Example usage:
output_file = 'output.txt'

