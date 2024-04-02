import argparse
from csv_iterator import process_csv
from config import load_config
from loadOrScrapeSitemaps import loadOrScrapeSitemap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Force the execution')
    args = parser.parse_args()

    config = load_config()
    paths = loadOrScrapeSitemap(config['urls']['site_a']['link'], args)
    process_csv(paths, config['urls']['site_a']['link'], config['urls']['site_b']['link'])

if __name__ == '__main__':
    main()
