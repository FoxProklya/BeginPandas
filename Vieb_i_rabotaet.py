# Подключение библеотек
import   numpy       as np
import   pandas      as pd
import   seaborn     as sns
import   xlsxwriter
import   psycopg2

from sqlalchemy   import create_engine
#________________________________

#Подключение к SQL
engine = create_engine()
#________________________________

#введение колличество строк для заполнения базы
n = int(input('колличество строк: '))
klist = []
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
for i in range(n):
	k1 = int  (input('Номер пробы: '     ))
	k2 = int  (input('Номер скважины: '  ))
	k3 = float(input('гл. *** м.: '      ))
	k4 = int  (input('кальций-ион: '     ))
	k5 = int  (input('магний-ион: '      ))
	klist += [k1]
#k1 = int  (input('Номер пробы: '     ))
#k2 = int  (input('Номер скважины: '  ))
#k3 = float(input('гл. *** м.: '      ))
#k4 = int  (input('кальций-ион: '     ))
#k5 = int  (input('магний-ион: '      ))

#df.index = [k1]
	df.loc[i+1] = k1, k2, k3, k4, k5

#df.index = klist
df['Операция вычисления'] = df['Номер скважины'] - df['кальций-ион'] 

print(df)

#if k1 in data['Номер пробы'] :



data = pd.read_sql('SELECT * FROM test', engine)

print(data)
#КАК ВЫЕБАТЬ БАЗУ К ХУЯМ___________________________________________________
df.index = df['Номер пробы']
data.index = data['Номер пробы']

data.update(df)
for i in df.index:
	if i not in data.index:
		print(i)
		data.loc[i] = df.loc[i]
print(data)
#_________________________________________________________________________
	
data.to_sql(name='test', con=engine, if_exists = 'replace', index = False)

writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name='testsheet')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
