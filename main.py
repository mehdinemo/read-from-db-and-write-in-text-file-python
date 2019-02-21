import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=servser_name;DATABASE=table_name;UID=id;PWD=pass')

cursor = conn.cursor()
cursor.execute('SELECT TOP 10 word,usersCount FROM [dbo].[Twitter_GroupedWords]')
rows = cursor.fetchall()

f = open('rows.txt',mode='w',encoding='utf-8')

for row in rows:
    f.write(row[0]+'\t'+str(row[1])+'\n')
f.close()
