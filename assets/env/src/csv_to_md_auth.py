import pandas as pd
from slugify import slugify

# Load the CSV file into a DataFrame
data = pd.read_csv("../../../_data/books.csv", sep=',', engine='python', encoding="utf-8").fillna('')

# Convert the DataFrame into a list of rows for processing
books = data.values.tolist()

for book in books:
    authors_array = book[3].split("; ")  # Split multiple authors

    for author in authors_array:
        author_array = author.split(", ")

        if len(author_array) >= 2:
            # Standard format: "Lastname, Firstname"
            last_name, first_name = author_array[0], author_array[1]
            url_raw = f"{last_name}-{first_name}"
        else:
            # Handle single-name authors (use the name as both first and last)
            last_name = author.strip()
            first_name = "unknown"  # Placeholder to maintain structure
            url_raw = last_name  # Use only the single name

        # Slugify the URL
        url = slugify(url_raw)
        file_name = f'../../../_authors/{url}.md'

        # Write the author details to the file
        title = author.strip()  # Use full name as title
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(f'---\ntitle: {title}\n---')

        print(f'{file_name} saved')
