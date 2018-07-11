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
engine = create_engine()

engine = psycopg2.connect() 
#________________________________ 

#введение колличество строк для заполнения базы 
#n = int(input('колличество строк: ')) 
klist = [] 
#создание датафрейма, введение слобцов базы 
k1 = 555 
k2 = 777
k3 = 888
k4 = 999
k5 = 1000
df = pd.DataFrame({ 
'Номер пробы' : [k1], 
'Номер скважины' : [k2], 
'гл. *** м.' : [k3], 
'кальций-ион' : [k4], 
'магний-ион' : [k5] 
# 'q1' : [], 
}) 

print(df) 




#def update_row(k1, k2, k3, k4, k5, k6):
    # read database configuration
#    db_config = read_db_config()
 
    # prepare query and data
#    query = """ UPDATE test
#                SET test
#                WHERE 'Номер пробы' = %s """
#    cursor = conn.cursor()
#    cursor.execute(query, data)
 

cursor = engine.cursor()
cursor.execute( """
UPDATE
       test
SET 
       "Номер скважины" = %s, 
       "гл. *** м."     = %s,
       "кальций-ион"    = %s,
       "магний-ион"     = %s
WHERE 
       "Номер пробы" = %s
""" , 
       (k2, k3, k4, k5, k1)
) 


cursor = engine.cursor()
cursor.execute( 'SELECT test FROM test WHERE "Номер пробы" = %s' , [k1]) 

results = cursor.fetchall() 
print(results)






#data = pd.read_sql('SELECT * FROM test', engine)

#print(data)
