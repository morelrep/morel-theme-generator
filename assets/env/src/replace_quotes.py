import os

command = "/home/morel/content-creator/assets/env/bin/clevercsv standardize --output ../../../_data/books.csv ../../../assets/data/books_zotero.csv"
print(f"Running: {command}")  # Debugging

exit_code = os.system(command)
print(f"Exit Code: {exit_code}")  # Check if it runs successfully
