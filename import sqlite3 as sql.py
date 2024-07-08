import sqlite3 as sql
import os


curr_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(curr_dir, 'amin_category.db')

conn = sql.connect(db_path)
cursor = conn.cursor()
        
select_query = '''SELECT *FROM CATEGORY'''
cursor.execute(select_query) 
rows = cursor.fetchall()
conn.commit()

print(rows)

text_category_xl = 'home'
check_query = '''SELECT category FROM CATEGORY WHERE category = ?'''
cursor.execute(check_query, (text_category_xl, )) 
resault = cursor.fetchall()
conn.commit()

print(resault)
if not resault:
    print('Hellow')

cursor.close()
conn.close()