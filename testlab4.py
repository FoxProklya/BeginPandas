# Подключение библеотек
import   numpy       as np
import   pandas      as pd
import   seaborn     as sns
import   xlsxwriter
import   psycopg2

from sqlalchemy   import create_engine
#________________________________

#Подключение к SQL
engine = create_engine
#________________________________

#введение колличество строк для заполнения базы
#n = int(input('колличество строк: '))

#создание датафрейма, введение слобцов базы
df = pd.DataFrame({
				    'Номер пробы'     : [],
				    'Номер скважины'  : [],
				    'гл. *** м.'      : [],
				   	'кальций-ион'     : [],
				   	'магний-ион'      : []
#					'q1'      : [],
#				    'q2'      : [],
#				    'q3'      : [],
#				   	'q4'      : [],
#				   	'q5'      : [],

	
	}
	)
#________________________________

#data = pd.read_sql('SELECT * FROM test', engine)

#print(data)

#вводимые данные
#for i in range(n):
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

df.index = [k1]
df.loc[i+1] = k1, k2, k3, k4, k5


df['Операция вычисления'] = df['Номер скважины'] - df['кальций-ион'] 

print(df)

#if k1 in data['Номер пробы'] :


df.to_sql(name='test', con=engine, if_exists = 'append', index=False)

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='testsheet')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
