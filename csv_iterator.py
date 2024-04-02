import csv
from scraper import fetch_and_parse
from comparator import compare_data
from save import save_comparison_to_file
from groupBy import groupBy
from concurrent.futures import ThreadPoolExecutor
import time

def process_csv(links, live_prefix, staging_prefix):
    output = ""
    fieldsDataTotal = []
    tasks = []
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        for row in links:
            path = row
            live_url = live_prefix + path
            staging_url = staging_prefix + path
            # Submit tasks to thread pool
            tasks.append(executor.submit(fetch_and_compare, live_url, staging_url))

        # Collect results
        for task in tasks:
            print("✅ Checked: " + path)
            compareReturn = task.result()
            output += compareReturn[0]
            fieldsDataTotal.append(compareReturn[1])

    fieldsDataTotal = groupBy(fieldsDataTotal)
    save_comparison_to_file(output, fieldsDataTotal)
    # Your code here
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'🕒 Time elapsed: {elapsed_time/60} minutes')
        
def fetch_and_compare(live_url, staging_url):
    live_data = fetch_and_parse(live_url, "site_a")
    staging_data = fetch_and_parse(staging_url, "site_b")
    return compare_data(live_data, staging_data, live_url, staging_url)