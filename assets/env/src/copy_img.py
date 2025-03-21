import shutil
import os
import pandas as pd
from slugify import slugify

# Create a DataFrame from the CSV file
# This reads the CSV file containing book data and fills missing values with an empty string
data = pd.read_csv("../../../_data/books.csv", sep=',', engine='python', encoding="utf-8").fillna('')

# Convert the DataFrame into a list of rows for processing
books = data.values.tolist()

# Define the default image file to use when the source column is empty
default_image = "../../empty.png"

# Check if the default image exists to avoid errors during the script execution
if not os.path.exists(default_image):
    raise FileNotFoundError(f"Default image file not found: {default_image}")

# Loop through each row in the CSV file
for book in books:
    # Extract raw author and title from the book record
    author_raw = book[3]  # Extract the raw authors column (e.g., "Smith, John; Doe, Jane")
    title_raw = book[4]  # Extract the raw title column (e.g., "Some Great Book")
    
    # Process the authors to generate a consistent format for the first author
    authors_array = author_raw.split("; ")  # Split multiple authors by '; '
    author_array = authors_array[0].split(", ")  # Split the first author's name by ', '
    author = author_array[0]  # Take only the last name of the first author

    # Process the title to generate a shorter, slug-friendly version
    title_split = str(title_raw).split(" ")  # Split the title into words
    title_short = title_split[:4]  # Take only the first 4 words
    title = "-".join(title_short)  # Join them with hyphens for URL-friendliness

    # Extract the year and combine it with the title and author to create a unique slug
    year = str(book[2])  # Extract the year column (e.g., "2023")
    url_raw = f"{title}-{author}-{year}"  # Combine elements into a raw URL string
    url = slugify(url_raw)  # Use the slugify library to make it URL-safe
    file_name = f"{url}.jpg"  # Generate the output file name with '.jpg' extension

    # Extract the source file path from the 37th column in the book record
    src = str(book[37]).strip()  # Ensure the value is a string and strip whitespace

    # If the source path is empty, use the default image file instead
    if not src:  # Check for an empty or missing source path
        src = default_image

    # Define the destination path where the file will be copied
    dst = f"../../../assets/img/{file_name}"  # Destination folder with the new file name

    # Check if the source file exists before attempting to copy
    if not os.path.exists(src):  # Prevent errors due to missing source files
        print(f"Source file not found: {src}. Skipping {file_name}.")  # Log the missing file
        continue  # Skip to the next record

    # Attempt to copy the file from the source to the destination
    try:
        shutil.copyfile(src, dst)  # Copy the file using shutil
        print(f"Copied: {src} -> {dst}")  # Log the successful copy
    except Exception as e:
        print(f"Error copying {src} to {dst}: {e}")  # Log any errors that occur
