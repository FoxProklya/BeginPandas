# Подключение библеотек 
import numpy as np 
import pandas as pd 
import seaborn as sns 
import xlsxwriter 
import psycopg2 
import sqlite3 

from sqlalchemy import create_engine 
#________________________________ 

#Подключение к SQL
engine = create_engine('postgresql://login:password@server:port/bazatable',echo=False) #для непадения

engine = psycopg2.connect( host='', user='', password='', dbname='') #для курсора
#________________________________

#введение колличество строк для заполнения базы 
#n = int(input('колличество строк: ')) 
klist = [] #список на будущее 

#Ввод значений
k1 = int  (input('Номер пробы: '     ))
k2 = int  (input('Номер скважины: '  ))
k3 = float(input('гл. *** м.: '      ))
k4 = int  (input('кальций-ион: '     ))
k5 = int  (input('магний-ион: ' ))
k6 = k5 - k4
#создание датафрейма, введение слобцов базы
df = pd.DataFrame({
		'Номер пробы'         : [k1],
		'Номер скважины'      : [k2],
		'гл. *** м.'          : [k3],
		'кальций-ион'         : [k4],
		'магний-ион'          : [k5],
            	'Операция вычисления' : [k6]

	
    	}
  	)
print(df)
#________________________________
#МАГИЯ
data = pd.read_sql('SELECT * FROM test', engine)
data.index = data['Номер пробы']
print(data) #Проверка таблицы

if k1 not in data.index:
  #Если нету то ИНСЕРТ
  print('В бездну список') #Проверка условия1
  cursor = engine.cursor()
  cursor.execute( 
    """
    INSERT INTO test VALUES 
    (%s, %s, %s, %s, %s, %s)
    """ ,
    (k1, k2, k3, k4, k5, k6)
  )
else:
  #Если есть то АПДАТЕ
  print('Есть в списке') #Проверка условия2
  cursor = engine.cursor()
  cursor.execute( 
    """
    UPDATE
           test
    SET 
          "Номер скважины"      = %s, 
          "гл. *** м."          = %s,
          "кальций-ион"         = %s,
          "магний-ион"          = %s,
          "Операция вычисления" = %s
    WHERE 
          "Номер пробы"         = %s
    """ , 
             (k2, k3, k4, k5, k6, k1)
  )
#____________________________

#Проверка работы со строкой
cursor = engine.cursor()
cursor.execute( 'SELECT test FROM test WHERE "Номер пробы" = %s' , [k1]) 
results = cursor.fetchall()
print(results)

#Проверка базы после махинаций
data1 = pd.read_sql('SELECT * FROM test', engine)
print(data1)
