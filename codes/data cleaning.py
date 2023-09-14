import sqlite3
import pandas as pd 
import  numpy as np 
from thefuzz import process
from thefuzz import fuzz
from datetime import datetime

FOHE_DB=pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\new_fohesldb5.csv')
#FOHE_DBSL=pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\FOHESLC.CSV')

df = pd.DataFrame(FOHE_DB)


FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].str.split(',').str[0]
FOHE_DB['Timestamp'] = pd.to_datetime(FOHE_DB['Timestamp'])
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].str.lower()
FOHE_DB.fillna('null',inplace=True)


#FOHE_DB['Timestamp'] = FOHE_DB['Timestamp'].astype(str)
# Corrected code for switching day and month while keeping time (including seconds)
FOHE_DB['Timestamp'] = pd.to_datetime(FOHE_DB['Timestamp'], format='%Y-%m-%d %H:%M:%S')
switched_dates = FOHE_DB['Timestamp'].dt.strftime('%d/%m/%Y %H:%M:%S')

# Print the switched dates
for date_str in switched_dates:
    print(date_str)

FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('nyc','new york')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('sf','san francisco')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('San Fransisco','san francisco')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('cdmx','mexico city')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('d.c','washington dc')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('la','los angeles')
FOHE_DB['What is the nearest big city to you?'] = FOHE_DB['What is the nearest big city to you?'].replace('d.c.','washington dc')



FOHE_DB.drop_duplicates(subset='Preferred email address', inplace=True)
duplicates = FOHE_DB.duplicated(subset = 'Preferred email address', keep = False)
duplicate_rows = FOHE_DB[duplicates]


#print(duplicate_rows['Preferred email address'])


#unique_cities = FOHE_DB['What is the nearest big city to you?'].unique()
#null_counts = df.isnull().sum()

#print(null_counts)


#FOHE_DB.to_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\new_fohesldb5.csv', index= False)



#print (FOHE_DB['What is the nearest big city to you?'])



