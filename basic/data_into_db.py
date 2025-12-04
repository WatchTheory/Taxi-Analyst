import pandas as pd
import sqlite3 # Example for SQLite
# Connect to the database
conn = sqlite3.connect('members.db')
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('fake_data.csv')
# Write the DataFrame to a SQL table
# 'if_exists' can be 'fail', 'replace', or 'append'
df.to_sql('members', conn, if_exists='replace', index=False)
# Close the database connection
conn.close()