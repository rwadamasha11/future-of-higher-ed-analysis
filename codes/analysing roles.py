import sqlite3
import pandas as pd 
import  numpy as np 



joined_db = pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\test.csv')

joined_db.fillna( pd.NA , inplace=True)


ceo_mask = joined_db['What\'s your current role/job title?'].str.contains('CEO', case=False, na=False)
cto_mask = joined_db['What\'s your current role/job title?'].str.contains('CTO', case=False, na=False)
coo_mask = joined_db['What\'s your current role/job title?'].str.contains('COO', case=False, na=False)
cxo_mask = joined_db['What\'s your current role/job title?'].str.contains('CXO', case=False, na=False)
director_mask = joined_db['What\'s your current role/job title?'].str.contains('director', case=False, na=False)
founder_mask = joined_db['What\'s your current role/job title?'].str.contains('founder', case=False, na=False)
cofounder_mask = joined_db['What\'s your current role/job title?'].str.contains('cofounder', case=False, na=False)
cofounder_mask = joined_db['What\'s your current role/job title?'].str.contains('co-founder', case=False, na=False)
Student_mask = joined_db['What\'s your current role/job title?'].str.contains('student', case=False, na=False)
vp_mask = joined_db['What\'s your current role/job title?'].str.contains('VP', case=False, na=False)

ceo = ceo_mask.sum()
cto = cto_mask.sum()
coo = coo_mask.sum()
founder = founder_mask.sum()
cofounder = cofounder_mask.sum()
student = Student_mask.sum()
vp = vp_mask.sum()
director = director_mask.sum()
sum_of_all = joined_db['What\'s your current role/job title?'].count()

other = sum_of_all - (ceo + cto + coo + founder + cofounder + student + vp + director )

print ("number of ceo = ", ceo )
print ("number of cto = ", cto )
print ("number of coo = ", coo )
print ("number of founders = ", founder )
print ("number of cofounders = ", cofounder  )
print ("number of students = ", student )
print ("number of vp = ", vp )
print ("number of directors in different fields = ", director )
print ("other managing roles = ", other )
print (sum_of_all)



#joined_db.to_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\test.csv', index=False)





