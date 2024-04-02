import os
import requests
import csv
from bs4 import BeautifulSoup
import sys
import os

def loadOrScrapeSitemap(url, force):
    domain = url.split("//")[-1].split("/")[0]
    sitemap_folder = "sitemap"
    sitemap_path = f"{sitemap_folder}/{domain}.csv"

    if not os.path.exists(sitemap_folder):
        os.makedirs(sitemap_folder)

    if os.path.exists(sitemap_path) and not force:
        # Sitemap exists locally, load it
        with open(sitemap_path, "r") as file:
            sitemap_links = file.read().splitlines()
    else:
        # Sitemap doesn't exist locally, scrape it from the URL
        response = requests.get(url + "/sitemap.xml")
        sitemap_links = extract_links_from_html(response.text, url)

        # Save the sitemap as a CSV file
        with open(sitemap_path, "w", newline="") as file:
            file.write('\n'.join(sitemap_links))

    return sitemap_links

def extract_links_from_html(html, url):
    soup = BeautifulSoup(html, features="xml")
    links = []
    for link in soup.find_all('loc'):
        links.append(link.text.replace(url, ""))
    return links
