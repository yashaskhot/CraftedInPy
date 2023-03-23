import pandas as pd
import tabula

filename=input("Enter your filepath: ")
# read the PDF file and convert it to a list of DataFrames
dfs = tabula.read_pdf(filename, pages='all')

# convert each DataFrame in the list to a Pandas DataFrame
for i in range(len(dfs)):
    dfs[i] = pd.DataFrame(dfs[i])

# concatenate all the DataFrames in the list into one DataFrame
df = pd.concat(dfs)

# save the DataFrame as a CSV file
df.to_csv('Pdf to Csv\output_file.csv', index=False)
