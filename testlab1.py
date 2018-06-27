import numpy as np
import pandas as pd
import seaborn as sns
import xlsxwriter

n = int(input('колличество строк: '))

listindex = [i+1 for i in range(n)]

#for i in range(n):
	#k1 = int  (input('Номер пробы: '     ))
	#k2 = int  (input('Номер скважины: '  ))
	#k3 = float(input('гл. *** м.: '      ))
	#k4 = int  (input('кальций-ион: '     ))
	#k5 = int  (input('магний-ион: '      ))


df = pd.DataFrame({
	    'Номер пробы'     : [int  (input('Номер пробы: '     )) 
							for i in range(n) ],
	    'Номер скважины'  : [int  (input('Номер скважины: '  )) 
							for i in range(n) ],
	    'гл. *** м.'      : [float(input('гл. *** м.: '      ))
							for i in range(n) ],
	   	'кальций-ион'     : [int  (input('кальций-ион: '     ))
		   					for i in range(n) ],
	   	'магний-ион'      : [int  (input('магний-ион: '      ))
		   					for i in range(n) ]
	}, 

	index = listindex

	)
	

print(df)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
