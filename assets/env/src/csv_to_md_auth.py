import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("../../../_data/books.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	authors_array = book[3].split("; ")
	for author in authors_array:
		author_array = author.split(", ")	
		url_raw = str(author_array[0])+"-"+str(author_array[1])
		url = slugify(url_raw)
		file_name = f'../../../_authors/{url}.md'
		title = str(author)

		with open(file_name, 'w', encoding="utf-8") as f:
			f.write(f'---\ntitle: {title}\n---')
			f.close()
		print(f'{file_name} saved')