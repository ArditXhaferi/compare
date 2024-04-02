import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
from config import load_config
import sys
from lxml import html

def fetch_and_parse(url, type):
    config = load_config()
    if("breadcrumb_xpath" in config["urls"][type]):
        breadcrumbs_xpath = config["urls"][type]['breadcrumb_xpath']
    else:
        breadcrumbs_xpath = ""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}    
    if "username" in config["urls"][type] and "password" in config["urls"][type]:
        response = requests.get(url, auth=HTTPBasicAuth(config["urls"][type]["username"], config["urls"][type]['password']), headers=headers)
    else:
        response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else ''
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        meta_desc = meta_desc['content'] if meta_desc else ''
        h1s = [h1.get_text() for h1 in soup.find_all('h1')]
        h2s = [h2.get_text() for h2 in soup.find_all('h2')]
        h1 = h1s[0].strip() if h1s else ''
        h2_0 = h2s[0].strip() if h2s else ''
        h2_1 = h2s[1].strip() if len(h2s) > 1 else ''
        tree = html.fromstring(response.content)
        breadcrumbs = [el.text_content() for el in tree.xpath(breadcrumbs_xpath)]
        breadcrumbs = [value.strip().replace('\n', '').replace(' ', '')  for value in breadcrumbs]
        return title, meta_desc, h1, h2_0, h2_1, len(h1s) > 1, " ".join(breadcrumbs).strip()
    return '', '', '', '', '', False, ''
