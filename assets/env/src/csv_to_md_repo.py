import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("../../../_data/books.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	if book[31] != "":
		title = str(book[31])
		url = slugify(title)
		file_name = f'../../../_repositories/{url}.md'

		with open(file_name, 'w', encoding="utf-8") as f:
			f.write(f'---\ntitle: "{title}"\n---')
			f.close()
		print(f'{file_name} saved')