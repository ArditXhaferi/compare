
def compare_data(live_data, staging_data, live_url, staging_url):
    comparison_results = generate_comparison_string(live_data, staging_data, live_url, staging_url)
    return comparison_results

def generate_comparison_string(live_data, staging_data, live_url, staging_url):
    comparison_results = "\n"
    comparison_results += live_url + " vs " + staging_url
    comparison_results += "\n---------------------------------\n"
    fields = ["Title", "Meta Description", "First H1", "First H2", "Second H2", "Multiple H1s", "Breadcrumbs"]
    fieldsData = {}
    for i, field in enumerate(fields):
        if field == "Multiple H1s":
            continue
        if staging_data[i] != live_data[i]:
            fieldsData[field] = live_url + ", " + staging_url
        comparison_results += "\n✅" if staging_data[i] == live_data[i] else "\n❌"
        comparison_results += " " + field + "\n\t Staging: " + staging_data[i] + "\n\t Live: " + live_data[i]
    booleanFields = ["Multiple H1s"]
    index = 0
    for i, field in enumerate(booleanFields):
        i = i + 5
        if live_data[i]:
            fieldsData[field] = live_url
        if staging_data[i]:
            fieldsData[field] = staging_url
        comparison_results += "\n✅" if not staging_data[i] and not live_data[i] else "\n❌"
        comparison_results += " " + field + "\n\t Staging: " + str(staging_data[i]) + "\n\t Live: " + str(live_data[i])
    comparison_results += "\n---------------------------------\n"
    return comparison_results, fieldsData

