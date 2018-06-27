import numpy as np
import pandas as pd
import seaborn as sns
import xlsxwriter

n = int(input('колличество строк: '))

df = pd.DataFrame({
	    'Номер пробы'     : [],
	    'Номер скважины'  : [],
	    'гл. *** м.'      : [],
	   	'кальций-ион'     : [],
	   	'магний-ион'      : []
	}

	)
	

for i in range(n):
	k1 = int  (input('Номер пробы: '     ))
	k2 = int  (input('Номер скважины: '  ))
	k3 = float(input('гл. *** м.: '      ))
	k4 = int  (input('кальций-ион: '     ))
	k5 = int  (input('магний-ион: '      ))
	df.loc[i+1] = k1, k2, k3, k4, k5


print(df)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
