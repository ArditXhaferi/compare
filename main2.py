import argparse
from csv_iterator import process_csv
from config import load_config
from loadOrScrapeSitemaps import loadOrScrapeSitemap
from nofollow import scrape_and_check_nofollow
import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
requests.packages.urllib3.disable_warnings() 
def main():
    # Suppress only the InsecureRequestWarning
    warnings.simplefilter('ignore', InsecureRequestWarning)

    # Your code here

    # Reset the warnings filter to default (optional)
    warnings.resetwarnings()

    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Force the execution')
    args = parser.parse_args()

    config = load_config()
    paths = loadOrScrapeSitemap(config['urls']['site_a']['link'], args)
    for path in paths:
        scrape_and_check_nofollow("https://cto.test/it/" + path)

if __name__ == '__main__':
    main()
