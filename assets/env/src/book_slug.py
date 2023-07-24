import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("_data/books.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	# converting the Authors column to an array
	authors_array = book[3].split("; ")
	author_array = authors_array[0].split(", ")
	# the next lines create the different components of the url for the main author
	author = author_array[0]
	# the next lines create the different components of the url for the title
	title_raw = str(book[4]) 
	title_split = title_raw.split(" ")
	title_short = (title_split[:4])
	title = "-".join(title_short)

	year = str(book[2])

	url_raw = title+"-"+author+"-"+year
	
	url = slugify(url_raw) # slugify is an imported app

	print(url)