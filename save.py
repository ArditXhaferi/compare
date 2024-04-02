import os
import datetime

def save_comparison_to_file(comparison_results, fields):
    # Create a folder with the current date as the folder name
    folder_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    os.makedirs(folder_name, exist_ok=True)

    # Create a file inside the folder with the specified format
    filename = folder_name + "/main.txt"

    # Write the text "main" into the file
    with open(filename, 'w') as file:
        file.write(comparison_results)

    for key in fields:
        # Create a file inside the folder with the specified format
        filename = folder_name + "/" + key + ".txt"

        # Write the text "main" into the file
        with open(filename, 'w') as file:
            file.write("\n".join(fields[key]))
