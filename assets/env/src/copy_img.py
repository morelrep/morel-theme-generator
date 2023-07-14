import shutil
import os

import pandas as pd

from slugify import slugify

# Create a dataFrame from csv file
data = pd.read_csv("../../../_data/books.csv", sep=',', engine ='python', encoding="utf-8").fillna('')

# Set the titles column to a list
books = data.values.tolist()

# Loop through each name, create .md file, set contents to string
for book in books:
	# converting the Authors column to an array
	author_raw = book[3]
	title_raw = book[4]
	# the next lines create the different components of the url for the main author
	authors_array = author_raw.split("; ")
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

	file_name = str(url)+".jpg"

	# this is the shutil module to copy the files


	src = str(book[37])

	path = '../../../assets/img/'


	dst = path + file_name

	print(shutil.copyfile(src, dst))
