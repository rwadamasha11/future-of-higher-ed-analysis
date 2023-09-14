import pandas as pd 
import numpy as np 



joined_table = pd.read_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\test4.csv')



Sales_Business_Development = joined_table['top 3 challenges for next year'].str.contains('Sales / Business Development', case=False, na=False)
Talent_Hiring = joined_table['top 3 challenges for next year'].str.contains('Talent / Hiring', case=False, na=False)
outcome_studentsuc =  joined_table['top 3 challenges for next year'].str.contains('Improving outcomes / student success', case=False, na=False)
Fundraising = joined_table['top 3 challenges for next year'].str.contains('Fundraising', case=False, na=False)
aa =  joined_table['top 3 challenges for next year'].str.contains('Finding full time or consulting work', case=False, na=False)
bb =  joined_table['top 3 challenges for next year'].str.contains('Finding innovative products and vendors to solve your challenges', case=False, na=False)
cc = joined_table['top 3 challenges for next year'].str.contains('Getting counsel on strategic decisions', case=False, na=False)
dd = joined_table['top 3 challenges for next year'].str.contains('Finding innovative products and vendors to solve your challenges', case=False, na=False)

top_3_challenges = {'Sales_Business_Development': Sales_Business_Development.sum(),
                    'Talent_Hiring': Talent_Hiring.sum(),
                    'outcome_studentsuc': outcome_studentsuc.sum(),
                    'Fundraising': Fundraising.sum(), 
                    'Finding full time or consulting work':aa.sum(), 
       'Finding innovative products and vendors to solve your challenges':bb.sum(),
       'Getting counsel on strategic decisions':cc.sum(),
       'Finding innovative products and vendors to solve your challenges': dd.sum()
}
print ('overall answers' , joined_table['top 3 challenges for next year'].count())

df = pd.DataFrame(top_3_challenges, index = [''])
print (df)


df.to_csv('C:\\Users\\חנא 2\\OneDrive\\שולחן העבודה\\FOHE\\12.csv', index=False)