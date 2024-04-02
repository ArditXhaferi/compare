from collections import defaultdict

def groupBy(data):

    # Group the data by key
    grouped_data = defaultdict(list)

    for item in data:
        for key, value in item.items():
            grouped_data[key].append(value)

    # Convert defaultdict to a regular dictionary
    result = dict(grouped_data)

    return result
