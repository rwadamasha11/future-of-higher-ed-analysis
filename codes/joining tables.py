
import pandas as pd 
import  numpy as np 



FOHE_DB=pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\new_fohesldb5.csv')
FOHE_DBSL=pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\FOHESLC.CSV')


joined_db = pd.merge( FOHE_DBSL , FOHE_DB, on='email',how = 'outer')


print (joined_db.info())


joined_db.to_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\test3.csv', index= False)
