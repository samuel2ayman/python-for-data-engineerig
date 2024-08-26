import pandas as pd
import sqlite3
conn=sqlite3.connect('practise database.db')
atrr=['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']
table_name="departments"
df=pd.read_csv(r"C:\Users\samuel\Desktop\python screens\programs\IBM projects\data base practise\Departments.csv",names=atrr)
df.to_sql(table_name,conn,if_exists='replace',index=False)
print('Table is ready')
#quering
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT DEPT_ID FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT LOC_ID FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()