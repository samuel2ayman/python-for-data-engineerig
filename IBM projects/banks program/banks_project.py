# Importing the required libraries
import pandas as pd
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
import requests
url="https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_name="Largest_banks"
csv_path=r"C:\Users\samuel\Desktop\python screens\programs\IBM projects\banks program\exchange_rate.csv"
output_path=r"C:\Users\samuel\Desktop\python screens\programs\IBM projects\banks program\outpu_file.csv"
conn=sqlite3.connect('Banks.db')
atrr_list=['Name','MC_USD_Billion']
atr=['MC_GBP_Billion','MC_EUR_Billion','MC_INR_Billion']
def log_process(message):
    time_format="%y-%m-%d-%H-%M-%S"
    now=datetime.now()
    time_stamp=now.strftime(time_format)
    with open("code_log.txt","a") as f:
        f.write( time_stamp + " : " + message +"\n")

def extract(url,atrr):
    df = pd.DataFrame(columns=atrr)
    page=requests.get(url)
    soup=BeautifulSoup(page.content,"lxml")
    tables=soup.find_all("tbody")
    rows=tables[0].find_all("tr")
    for i in rows:
        column=i.find_all("td")
        if len(column)!=0:
            dict={"Name":column[1].find_all("a")[1]['title'],"MC_USD_Billion":float(column[2].contents[0].strip())}
            df1=pd.DataFrame(dict,index=[0])
            df=pd.concat([df,df1], ignore_index=True)
    return df
i=0
df=extract(url,atrr_list)
print(df)
def transform(data,csv_path):
    # df1= df = pd.DataFrame(columns=atr)
    rate=pd.read_csv(csv_path)
    EUR=rate.iloc[0,1]
    GBP=rate.iloc[1,1]
    INR=rate.iloc[2,1]
    data['MC_GBP_Billion']=round(data.MC_USD_Billion*GBP,2)
    data['MC_EUR_Billion']=round(data.MC_USD_Billion* EUR,2)
    data['MC_INR_Billion']=round(data.MC_USD_Billion* INR,2)
    return df
tr=transform(df,csv_path)
print(tr)

def load_to_csv(transformed_data, output_path):
    transformed_data.to_csv(output_path)

    
def load_to_db(df, conn, table_name):
    df.to_sql(table_name, conn, if_exists = 'replace', index =False)
    print('Table is ready')


#quering
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT Name FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT MC_USD_Billion FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT MC_GBP_Billion FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT MC_EUR_Billion FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

query_statement = f"SELECT MC_INR_Billion FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

log_process("initiatint ETL process")

log_process("Extract phase Started") 
extract(url,atrr_list) 
extracted_data = extract(url,atrr_list) 
log_process("Extract phase Ended") 
 
log_process("Transform phase Started") 
transformed_data = transform(df,csv_path) 
print("Transformed Data") 
print(transformed_data) 
log_process("Transform phase Ended") 
  
# Log the beginning of the Loading process 
log_process("Load  Started to csv ") 
load_to_csv(transformed_data,output_path)  
log_process("Load  to csv Ended")

log_process("Load  Started to csv ") 
load_to_db(df, conn, table_name)
log_process("Load  to csv Ended") 

# Log the completion of the ETL process 
log_process("ETL Job Ended") 