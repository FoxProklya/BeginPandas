import numpy as np
import pandas as pd
import seaborn as sns
import xlsxwriter
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://(NAMEaccaunt):#########@(SERVER):(HOST)/(NAMEDB)',echo=False)
n = int(input('колличество строк: '))

df = pd.DataFrame({
				    #'Номер пробы'     : [],
				    #'Номер скважины'  : [],
				    #'гл. *** м.'      : [],
				    #'кальций-ион'     : [],
				    #'магний-ион'      : []
				    'q1'      : [],
				    'q2'      : [],
				    'q3'      : [],
				    'q4'      : [],
				    'q5'      : []
	
	}
	)
	

for i in range(n):
	#k1 = int  (input('Номер пробы: '     ))
	#k2 = int  (input('Номер скважины: '  ))
	#k3 = float(input('гл. *** м.: '      ))
	#k4 = int  (input('кальций-ион: '     ))
	#k5 = int  (input('магний-ион: '      ))
	k1 = int  (input('Номер пробы: '     ))
	k2 = int  (input('Номер скважины: '  ))
	k3 = float(input('гл. *** м.: '      ))
	k4 = int  (input('кальций-ион: '     ))
	k5 = int  (input('магний-ион: '      ))

	df.loc[i+1] = k1, k2, k3, k4, k5

import numpy as np
import pandas as pd
import seaborn as sns
import xlsxwriter
import psycopg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://artur:2011Milki532678@endiny.me:5432/artur_test',echo=False)
n = int(input('колличество строк: '))

df = pd.DataFrame({
				    #'Номер пробы'     : [],
				    #'Номер скважины'  : [],
				    #'гл. *** м.'      : [],
				   	#'кальций-ион'     : [],
				   	#'магний-ион'      : []
					'q1'      : [],
				    'q2'      : [],
				    'q3'      : [],
				   	'q4'      : [],
				   	'q5'      : [],

	
	}
	)
	

for i in range(n):
	#k1 = int  (input('Номер пробы: '     ))
	#k2 = int  (input('Номер скважины: '  ))
	#k3 = float(input('гл. *** м.: '      ))
	#k4 = int  (input('кальций-ион: '     ))
	#k5 = int  (input('магний-ион: '      ))
	k1 = int  (input('Номер пробы: '     ))
	k2 = int  (input('Номер скважины: '  ))
	k3 = float(input('гл. *** м.: '      ))
	k4 = int  (input('кальций-ион: '     ))
	k5 = int  (input('магний-ион: '      ))

	df.loc[i+1] = k1, k2, k3, k4, k5

df['q6'] = df['q3'] - df['q4'] 

print(df)

df.to_sql(name='test', con=engine, if_exists = 'replace', index=False)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

print(df)

df.to_sql(name='test', con=engine, if_exists = 'replace', index=False)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
