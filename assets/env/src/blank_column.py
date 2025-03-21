import pandas as pd

# Define the path to the input CSV file
input_file = '../../../_data/books.csv'

# Define the path to the output CSV file
output_file = '../../../_data/books.csv'

# Add a blank column at the beginning of the CSV file
def add_blank_column(input_file, output_file):
    # Read the input CSV file into a DataFrame
    df = pd.read_csv(input_file, dtype={'Edition': object})

    # Insert a blank column at the beginning with empty values
    df.insert(0, 'Blank Column', '')

    # Write the DataFrame to the output CSV file
    df.to_csv(output_file, index=False)

    print("Blank column added successfully.")

# Call the function to add the blank column
add_blank_column(input_file, output_file)
